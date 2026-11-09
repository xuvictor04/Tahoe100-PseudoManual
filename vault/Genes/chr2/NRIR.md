---
symbol: "NRIR"
type: "gene"
col: 13498
ensembl_id: "ENSG00000225964"
name: "negative regulator of interferon response"
location: "2p25.2"
module: 32
arm: "+"
pooled_cpm: 3.26
n_lines_expressing: 36
n_dd_up: 12
n_dd_down: 30
n_dd_up_clean: 7
n_dd_down_clean: 25
in_vector_space: true
direction_upstream: 32
direction_downstream: 58
tags: ["gene", "module/032"]
generated_by: "tahoemap"
---

# NRIR

*negative regulator of interferon response* — 2p25.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 3.04× (z +7.8, q 4e-12, up in 0 of 6 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Cobimetinib (drug)]] 5 µM: 2.13× (z +5.3, q 3e-05, up in 16 of 23 measured lines).
> Pooled over the cell lines (median), lowered significantly by 30 drug-doses (5 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.195× (z -11.9, q 5e-30, down in 28 of 31 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FBXO39]] (+0.90, fdr 7e-06), [[CMPK2]] (+0.88, fdr 7e-06, ⚠ same locus), [[OAS2]] (+0.87, fdr 7e-06), [[IFI44]] (+0.86, fdr 7e-06).
> It is in [[Module 032]], a single-armed module (interferon alpha response).
> Probable direction (from the cell lines, not proof of direct regulation): 32 arrows point to it, the strongest [[GBP4]] → it (grade B ⚠); 58 go from it, the strongest it → [[HERC6]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 5 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13498.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.04×** | +7.8 | 4e-12 | 0/6 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.43×** | +6.0 | 7e-07 | 1/11 (NCI-H460) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Cobimetinib (drug)]] 5 µM |  | **2.13×** | +5.3 | 3e-05 | 16/23 (LoVo, KATO III, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.66×** | +5.2 | 3e-05 | 7/21 (LS 180, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.05×** | +5.0 | 5e-05 | 12/24 (NCI-H460, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.96×** | +4.9 | 9e-05 | 2/14 (HEC-1-A, NCI-H460) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.94×** | +4.6 | 3e-04 | 3/16 (SK-MEL-2, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.49×** | +4.1 | 0.003 | 8/31 (NCI-H2347, NCI-H460, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.72×** | +3.9 | 0.005 | 12/29 (NCI-H460, SK-MEL-2, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **1.39×** | +3.4 | 0.042 | 4/32 (NCI-H460, NCI-H1573, …) | rises with dose | position effect removed |
| [[Binimetinib (drug)]] 5 µM |  | **1.55×** | +3.3 | 0.054 | 7/32 (LoVo, COLO 205, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.56×** | +3.1 | 0.085 | 7/26 (SNU-423, LoVo, …) | top dose only |  |
| [[Trametinib (drug)]] 0.05 µM |  | 1.35× | +3.0 | 0.11 | 10/31 (SK-MEL-2, LoVo, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 5 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 30 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13498.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.195×** | -11.9 | 5e-30 | 28/31 (LoVo, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~11% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.237×** | -10.5 | 2e-23 | 26/29 (LoVo, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Tofacitinib (drug)]] 5 µM |  | **0.394×** | -9.6 | 1e-19 | 24/30 (LoVo, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Tofacitinib (citrate) (drug)]] 5 µM |  | **0.406×** | -9.3 | 2e-18 | 21/30 (COLO 205, RPMI-7951, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **0.320×** | -8.3 | 1e-14 | 23/31 (COLO 205, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.340×** | -7.9 | 3e-13 | 24/31 (LoVo, RPMI-7951, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.401×** | -6.7 | 2e-09 | 19/31 (A-172, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Selinexor (drug)]] 5 µM |  | **0.532×** | -6.5 | 4e-09 | 21/30 (LoVo, NCI-H1573, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.409×** | -6.5 | 4e-09 | 19/31 (RPMI-7951, NCI-H1573, …) | all doses, stronger at high dose | composition shift |
| [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | **0.442×** | -6.0 | 1e-07 | 17/24 (NCI-H1573, KATO III, …) | all doses, stronger at high dose |  |
| [[Tofacitinib (drug)]] 0.5 µM |  | **0.449×** | -5.8 | 3e-07 | 20/27 (RPMI-7951, COLO 205, …) | all doses, stronger at high dose |  |
| [[Brivudine (drug)]] 5 µM |  | **0.253×** | -5.2 | 8e-06 | 19/27 (COLO 205, LoVo, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.496×** | -5.1 | 1e-05 | 17/28 (RPMI-7951, NCI-H1573, …) | inconsistent across doses | position effect removed |
| [[Mebendazole (drug)]] 5 µM |  | **0.492×** | -5.0 | 3e-05 | 12/31 (CFPAC-1, BT-474, …) | top dose only | position effect removed |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.622×** | -4.9 | 3e-05 | 16/30 (BT-474, CHP-212, …) | rises with dose |  |
| [[NG25 (drug)]] 5 µM |  | **0.337×** | -4.1 | 0.001 | 13/19 (NCI-H1573, BT-474, …) | top dose only | cell-cycle shift (explains ~20% here); noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.569×** | -4.1 | 0.001 | 16/21 (LoVo, KATO III, …) | rises with dose | cell-cycle shift (explains ~12% here); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.24 per unit of S-phase module lfc, -0.39 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13498. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[RPMI-7951 (line)]] | alt | 15.0 | 0 | 10 (3 ⚠) | — | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM 0.0371× (z -11.2) |
| [[LoVo (line)]] | wt | 10.9 | 0 | 8 (2 ⚠) | — | [[Tofacitinib (drug)]] 5 µM 0.0807× (z -14.2) |
| [[NCI-H1573 (line)]] | alt | 7.31 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0415× (z -14.6) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Tofacitinib (citrate) (drug)]] 0.5 µM 0.0223× (z -12.4) |
| [[A-172 (line)]] | wt | 9.58 | 0 | 5 | — | [[Panobinostat (drug)]] 0.5 µM 0.0393× (z -12.0) |
| [[COLO 205 (line)]] | alt | 12.4 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.0328× (z -10.3) |
| [[BT-474 (line)]] | alt | 9.24 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0324× (z -13.2) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.0338× (z -9.2) |
| [[KATO III (line)]] | alt | 11.9 | 0 | 3 | — | [[Tofacitinib (citrate) (drug)]] 0.5 µM 0.0280× (z -12.0) |
| [[A498 (line)]] | wt | 2.65 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0483× (z -9.1) |
| [[CFPAC-1 (line)]] | alt | 4.16 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.0357× (z -9.9) |
| [[NCI-H460 (line)]] | wt | 6.22 | 1 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 5.57× (z +11.6) ⚠ cell-cycle shift, would explain all of this change | [[Belinostat (drug)]] 5 µM 0.127× (z -9.8) |
| [[SNU-423 (line)]] | alt | 4.76 | 0 | 2 | — | [[Tofacitinib (citrate) (drug)]] 0.5 µM 0.0454× (z -9.2) |
| [[HEC-1-A (line)]] | alt | 2.99 | 0 | 1 | — | [[Malotilate (drug)]] 0.5 µM 0.0692× (z -9.6) |
| [[A-427 (line)]] | wt | 0.939 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.31 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 0.573 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 1.33 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.51 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.20 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 8.60 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 0.920 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.452 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 4.14 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 0.396 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.27 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.43 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.448 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.364 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.447 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.768 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.53 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.742 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 1.19 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 0.437 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 3.79 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.567 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 3.33 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.27 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.536 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 3.62 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.322 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.98 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.49 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 6.76 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.63 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.56 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.22 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.96 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.803 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.82 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 0.233 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13498), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FBXO39]] | +0.90 | +0.83 / +0.89 | both halves | 7e-06 | **novel candidate** |
| [[CMPK2]] | +0.88 | +0.84 / +0.90 | both halves | 7e-06 | ⚠ same locus (0.1 kb, same strand: neighbours can correlate without regulation) |
| [[OAS2]] | +0.87 | +0.79 / +0.91 | both halves | 7e-06 |  |
| [[RSAD2]] | +0.87 | +0.85 / +0.87 | both halves | 7e-06 | ⚠ same locus (25.1 kb: neighbours can correlate without regulation) |
| [[IFI44]] | +0.86 | +0.81 / +0.90 | both halves | 7e-06 |  |
| [[MX1]] | +0.85 | +0.76 / +0.88 | both halves | 7e-06 |  |
| [[XAF1]] | +0.84 | +0.78 / +0.86 | both halves | 7e-06 |  |
| [[HERC6]] | +0.84 | +0.75 / +0.85 | both halves | 7e-06 |  |
| [[IFI44L]] | +0.84 | +0.73 / +0.89 | both halves | 7e-06 |  |
| [[OAS1]] | +0.83 | +0.79 / +0.87 | both halves | 7e-06 |  |
| [[USP18]] | +0.83 | +0.73 / +0.85 | both halves | 7e-06 |  |
| [[PLSCR1]] | +0.82 | +0.72 / +0.87 | both halves | 7e-06 |  |
| [[PARP14]] | +0.82 | +0.68 / +0.85 | both halves | 7e-06 |  |
| [[DDX60L]] | +0.82 | +0.70 / +0.85 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*32 arrows, 32 of them with an alert ⚠; grade A 0, B 30, C 2. Shown: the 12 strongest; 20 more arrows (20 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GBP4]] | B | GBP4 activity raises NRIR's level | lines that do not express GBP4 (20) vs lines expressing it (30) | 2.12× lower at baseline in the lines without GBP4 | 0.001 | ⚠ within organs, on part of the lines; also absent: SAMD9L, CD5L, GBP1 |
| [[OAS2]] | B | OAS2 activity raises NRIR's level | lines that do not express OAS2 (14) vs lines expressing it (36) | 2.37× lower at baseline in the lines without OAS2 | 0.002 | ⚠ within organs, on part of the lines; also absent: OAS1, CMPK2, MX1 |
| [[ETV7]] | B | ETV7 activity raises NRIR's level | lines that do not express ETV7 (13) vs lines expressing it (37) | 2.02× lower at baseline in the lines without ETV7 | 0.005 | ⚠ within organs, on part of the lines; also absent: TUBA4A, AGMAT, ANO9; maybe low, not absent |
| [[RSAD2]] | B | RSAD2 activity raises NRIR's level | lines that do not express RSAD2 (14) vs lines expressing it (36) | 2.42× lower at baseline in the lines without RSAD2 | 0.006 | ⚠ within organs, on part of the lines; also absent: SH3TC1, IFI27, SRMS |
| [[RASGRP3]] | B | RASGRP3 activity raises NRIR's level | lines that do not express RASGRP3 (16) vs lines expressing it (34) | 2.15× lower at baseline in the lines without RASGRP3 | 0.007 | ⚠ within organs, on part of the lines; also absent: IFI6, SLC15A3, GBP4; maybe low, not absent |
| [[CCDC194]] | B | CCDC194 activity raises NRIR's level | lines that do not express CCDC194 (19) vs lines expressing it (31) | 2.13× lower at baseline in the lines without CCDC194 | 0.007 | ⚠ within organs, on part of the lines; also absent: BST2, DEPP1, TRIM22 |
| [[OAS1]] | B | OAS1 activity raises NRIR's level | lines that do not express OAS1 (13) vs lines expressing it (37) | 2.29× lower at baseline in the lines without OAS1 | 0.010 | ⚠ within organs, on part of the lines; also absent: OAS2, TRIM22, IFI27; maybe low, not absent |
| [[TRIM22]] | B | TRIM22 activity raises NRIR's level | lines that do not express TRIM22 (18) vs lines expressing it (32) | 1.89× lower at baseline in the lines without TRIM22 | 0.012 | ⚠ within organs, on part of the lines; also absent: CD5L, XAF1, IFITM1 |
| [[SAMD9L]] | B | SAMD9L activity raises NRIR's level | lines that do not express SAMD9L (18) vs lines expressing it (32) | 1.96× lower at baseline in the lines without SAMD9L | 0.013 | ⚠ within organs, on part of the lines; also absent: GBP4, CD5L, TRIM22 |
| [[IFI44]] | B | IFI44 activity raises NRIR's level | lines that do not express IFI44 (12) vs lines expressing it (38) | 2.03× lower at baseline in the lines without IFI44 | 0.017 | ⚠ within organs, on part of the lines; also absent: SAMD9, GBP1, BMP2 |
| [[GBP1]] | B | GBP1 activity raises NRIR's level | lines that do not express GBP1 (16) vs lines expressing it (34) | 1.95× lower at baseline in the lines without GBP1 | 0.018 | ⚠ within organs, on part of the lines; also absent: GBP4, GBP2, SAMD9 |
| [[PLAAT4]] | B | PLAAT4 activity raises NRIR's level | lines that do not express PLAAT4 (21) vs lines expressing it (29) | 1.60× lower at baseline in the lines without PLAAT4 | 0.020 | ⚠ within organs, on part of the lines; also absent: PTPRB, TNFSF10, EPSTI1 |

### Downstream of this gene

*58 arrows, 58 of them with an alert ⚠; grade A 0, B 56, C 2. Shown: the 12 strongest; 46 more arrows (46 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HERC6]] | B | NRIR activity raises HERC6's level | lines that do not express NRIR (14) vs lines expressing it (36) | 2.43× lower at baseline in the lines without NRIR | 0.001 | ⚠ within organs, on part of the lines; also absent: CMPK2, TSPAN7 |
| [[PARP10]] | B | NRIR activity raises PARP10's level | lines that do not express NRIR (14) vs lines expressing it (36) | 1.76× lower at baseline in the lines without NRIR | 0.002 | ⚠ within organs, on part of the lines; also absent: CMPK2, TSPAN7 |
| [[NLRC5]] | B | NRIR activity raises NLRC5's level | lines that do not express NRIR (14) vs lines expressing it (36) | 2.09× lower at baseline in the lines without NRIR | 0.002 | ⚠ within organs, on part of the lines; also absent: CMPK2, TSPAN7 |
| [[MX2]] | B | NRIR activity strengthens MX2's drug response | lines that do not express NRIR (9) vs lines expressing it (24) | the lines without NRIR respond 0.63× as strongly (z diff +3.24); strongest at Fedratinib (hydrochloride hydrate) 5 µM: 0.47x vs 0.15x (z diff +6.0) | 0.003 | ⚠ within organs, on part of the lines; also absent: CMPK2, TSPAN7; target measured in part of the lines; artifact flags |
| [[SAMD9L]] | B | NRIR activity raises SAMD9L's level | lines that do not express NRIR (14) vs lines expressing it (36) | 3.75× lower at baseline in the lines without NRIR | 0.003 | ⚠ within organs, on part of the lines; also absent: CMPK2, TSPAN7 |
| [[RSAD2]] | B | NRIR activity raises RSAD2's level | lines that do not express NRIR (14) vs lines expressing it (36) | 4.13× lower at baseline in the lines without NRIR | 0.004 | ⚠ within organs, on part of the lines; also absent: CMPK2, TSPAN7 |
| [[TDRD7]] | B | NRIR activity raises TDRD7's level | lines that do not express NRIR (14) vs lines expressing it (36) | 1.72× lower at baseline in the lines without NRIR | 0.006 | ⚠ within organs, on part of the lines; also absent: CMPK2, TSPAN7 |
| [[PARP10]] | B | NRIR activity strengthens PARP10's drug response | lines that do not express NRIR (13) vs lines expressing it (33) | the lines without NRIR respond 0.42× as strongly (z diff +2.47); strongest at Belinostat 5 µM: 0.52x vs 0.27x (z diff +3.5) | 0.006 | ⚠ within organs, on part of the lines; also absent: CMPK2, TSPAN7; target measured in part of the lines; artifact flags |
| [[DDX60]] | B | NRIR activity raises DDX60's level | lines that do not express NRIR (14) vs lines expressing it (36) | 2.25× lower at baseline in the lines without NRIR | 0.007 | ⚠ within organs, on part of the lines; also absent: CMPK2, TSPAN7 |
| [[SAMD9]] | B | NRIR activity raises SAMD9's level | lines that do not express NRIR (14) vs lines expressing it (36) | 2.44× lower at baseline in the lines without NRIR | 0.013 | ⚠ within organs, on part of the lines; also absent: CMPK2, TSPAN7 |
| [[IFI44]] | B | NRIR activity raises IFI44's level | lines that do not express NRIR (14) vs lines expressing it (36) | 2.61× lower at baseline in the lines without NRIR | 0.013 | ⚠ within organs, on part of the lines; also absent: CMPK2, TSPAN7 |
| [[IFI16]] | B | NRIR activity raises IFI16's level | lines that do not express NRIR (14) vs lines expressing it (36) | 3.36× lower at baseline in the lines without NRIR | 0.016 | ⚠ within organs, on part of the lines; also absent: CMPK2, TSPAN7 |

## Where it sits

- **Module**: [[Module 032]] — interferon alpha response; 139 genes; every member is in the + arm (projection on the module's main direction 0.861). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (48.5, 54.6); signed map (65.6, 31.8). **Vector** length 89.2, 21.8% of its response variance represented; |z| ≥ 3 in 1,040 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *interferon alpha response* (hallmark, mean cos +0.71 to 56); *interferon gamma response* (hallmark, mean cos +0.72 to 60); *interferon* (control, mean cos +0.79 to 23).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.2 | +5.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.0 | +7.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.8 | +6.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.6 | +4.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.4 | +2.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.8 | +4.1 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.7 | +5.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.0 | -0.1 |
|  | [[Cepharanthine (drug)]] 5 µM |  | +1.8 | +2.5 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +1.7 | +0.7 |
| fall | [[Tofacitinib (drug)]] 5 µM |  | -5.1 | -9.6 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -4.4 | -5.8 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | -4.3 | -9.3 |
|  | [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | -3.8 | -6.0 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -3.4 | -7.9 |

## What is on record

|  |  |
|---|---|
| Name | negative regulator of interferon response |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 2p25.2 — chr2:6,819,463-6,840,464 (-) |
| Ensembl biotype | lncRNA |
| Also known as | lncRNA-CMPK2, lncCMPK2 |
| Gene groups (HGNC) | Long non-coding RNAs with non-systematic symbols |
| Matched by | ensembl_id |

**Summary**, from NCBI Gene [104326052](https://www.ncbi.nlm.nih.gov/gene/104326052):

> This gene is thought to produce a functional long non-coding RNA. This transcript may be a negative regulator of interferon response. [provided by RefSeq, Feb 2015]

**Accessions** — [HGNC:51269](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:51269) · Entrez [104326052](https://www.ncbi.nlm.nih.gov/gene/104326052) · Ensembl [ENSG00000225964](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000225964)

## Data

Gene col 13498: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13498); `tables/drug_effects.parquet` (43 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13498, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13498]; `tensor/DDL_lfc|DDL_z.npy` [13498]; `embed/gene_vectors.npy` [13498]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13498 or target_col == 13498). Every well: [[NRIR — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NRIR.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
