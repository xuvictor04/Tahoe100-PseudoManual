---
symbol: "PSMC3IP"
type: "gene"
col: 5214
ensembl_id: "ENSG00000131470"
name: "PSMC3 interacting protein"
location: "17q21.2"
module: 6
arm: "+"
pooled_cpm: 13.75
n_lines_expressing: 50
n_dd_up: 34
n_dd_down: 0
n_dd_up_clean: 11
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 7
direction_downstream: 0
tags: ["gene", "module/006"]
generated_by: "tahoemap"
---

# PSMC3IP

*PSMC3 interacting protein* — 17q21.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 34 drug-doses (23 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 4.10× (z +13.5, q 1e-38, up in 34 of 38 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~70% of this change. The strongest without an alert is [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM: 1.57× (z +6.1, q 6e-08, up in 25 of 48 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Selinexor (drug)]] 5 µM in 1 line (A498 0.342×; ⚠ cell-cycle shift, would explain all of this change); [[Idarubicin (hydrochloride) (drug)]] 0.5 µM in 1 line (A498 0.265×; ⚠ cell-cycle shift, explains ~31% of this change); [[Proglumide (drug)]] 0.05 µM in 1 line (SW48 0.0715×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ORC6]] (+0.82, fdr 7e-06), [[CLSPN]] (+0.80, fdr 7e-06), [[CHAF1A]] (+0.80, fdr 7e-06).
> It sits in the **+** arm of [[Module 006]] (E2F targets).
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[TCF19]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 34 in all, 23 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 34 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 23 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5214.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~70% of this change | **4.10×** | +13.5 | 1e-38 | 34/38 (HOP62, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~66% of this change | **3.96×** | +12.6 | 4e-34 | 18/19 (HOP62, LOX-IMVI, …) | all doses, stronger at high dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **2.26×** | +11.0 | 8e-26 | 41/46 (A549, NCI-H2030, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~79% of this change | **2.96×** | +10.4 | 6e-23 | 44/47 (SW480, KATO III, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~71% of this change | **2.77×** | +9.7 | 2e-20 | 44/47 (SW480, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~65% of this change | **2.85×** | +9.3 | 2e-18 | 25/27 (HOP62, NCI-H2347, …) | all doses, stronger at high dose | composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~84% of this change | **2.49×** | +8.7 | 3e-16 | 39/47 (SW480, KATO III, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **2.51×** | +8.4 | 2e-15 | 36/45 (SW480, NCI-H23, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~39% of this change | **2.49×** | +8.4 | 4e-15 | 35/39 (SW480, KATO III, …) | all doses, stronger at high dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~64% of this change | **2.19×** | +7.2 | 4e-11 | 36/45 (HOP62, SW480, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **2.04×** | +6.5 | 3e-09 | 31/46 (NCI-H2030, J82, …) | all doses, stronger at high dose | composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.57×** | +6.1 | 6e-08 | 25/48 (J82, SW480, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~63% of this change | **1.56×** | +5.9 | 1e-07 | 23/45 (J82, Panc 03.27, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~90% of this change | **1.85×** | +5.9 | 2e-07 | 32/45 (HEC-1-A, A-427, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.85×** | +5.8 | 2e-07 | 28/46 (NCI-H2030, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.75×** | +5.3 | 4e-06 | 32/47 (NCI-H2030, HOP62, …) | two highest doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.66×** | +4.8 | 5e-05 | 27/47 (NCI-H2030, SW480, …) | two highest doses | cell-cycle shift (explains ~24% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.58×** | +4.3 | 4e-04 | 23/47 (LoVo, SW480, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | **1.46×** | +3.3 | 0.018 | 13/43 (J82, A-427, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.42×** | +3.1 | 0.044 | 15/42 (NCI-H460, A498, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.37×** | +3.0 | 0.047 | 13/47 (A549, SW480, …) | all doses, stronger at high dose |  |
| [[Celecoxib (drug)]] 0.5 µM |  | **1.56×** | +2.9 | 0.059 | 6/46 (HEC-1-A, A-427, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | **1.35×** | +2.8 | 0.083 | 11/44 (C-33 A, NCI-H460, …) | inconsistent across doses | position effect removed |
| [[Glycyrrhizic acid (drug)]] 0.05 µM |  | **1.37×** | +2.8 | 0.097 | 10/42 (A-172, PANC-1, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 2 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 5214.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Selinexor (drug)]] 5 µM in 1 line (A498 0.342×; ⚠ cell-cycle shift, would explain all of this change); [[Idarubicin (hydrochloride) (drug)]] 0.5 µM in 1 line (A498 0.265×; ⚠ cell-cycle shift, explains ~31% of this change); [[Proglumide (drug)]] 0.05 µM in 1 line (SW48 0.0715×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | 0.691× | -3.6 | 0.13 | 19/46 (A498, A-172, …) | all doses, flat |  |
| [[palbociclib (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~88% of this change | 0.592× | -3.5 | 0.13 | 17/48 (A498, LOX-IMVI, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | 0.706× | -3.2 | 0.24 | 14/45 (HEC-1-A, NCI-H23, …) | top dose only | position effect removed |
| [[Cepharanthine (drug)]] 5 µM |  | 0.798× | -3.1 | 0.29 | 11/48 (NCI-H1573, HS-578T, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +1.26 per unit of S-phase module lfc, +0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5214. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 16.6 | 5 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.43× (z +10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~70% of this change | — |
| [[A498 (line)]] | wt | 23.9 | 0 | 3 (3 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.342× (z -11.1) ⚠ cell-cycle shift, would explain all of this change |
| [[HOP62 (line)]] | alt | 17.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.70× (z +11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~70% of this change | — |
| [[LOX-IMVI (line)]] | wt | 10.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 8.14× (z +9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~66% of this change | — |
| [[NCI-H2030 (line)]] | alt | 24.2 | 2 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.90× (z +8.8) ⚠ cell-cycle shift, explains ~36% of this change | — |
| [[A549 (line)]] | wt | 10.7 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.89× (z +9.9) ⚠ cell-cycle shift, explains ~36% of this change | — |
| [[J82 (line)]] | alt | 33.6 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.18× (z +14.1) ⚠ cell-cycle shift, explains ~63% of this change | — |
| [[KATO III (line)]] | alt | 14.2 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 5.19× (z +8.5) ⚠ cell-cycle shift, explains ~79% of this change | — |
| [[LoVo (line)]] | wt | 6.51 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 10.7× (z +10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~70% of this change | — |
| [[LS 180 (line)]] | wt | 6.12 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 10.1× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~70% of this change | — |
| [[NCI-H2347 (line)]] | alt | 8.96 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.11× (z +8.5) ⚠ cell-cycle shift, explains ~36% of this change | — |
| [[NCI-H460 (line)]] | wt | 10.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.83× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~70% of this change | — |
| [[SW1417 (line)]] | alt | 13.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.39× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~66% of this change | — |
| [[SW48 (line)]] | wt | 12.9 | 0 | 1 | — | [[Proglumide (drug)]] 0.05 µM 0.0715× (z -9.1) |
| [[A-172 (line)]] | wt | 20.5 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 22.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 5.71 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 5.33 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 7.47 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 8.70 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 6.25 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 11.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 25.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 7.44 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 7.17 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 7.73 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 10.9 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 10.0 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 5.41 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 4.91 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.96 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 13.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 25.2 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 24.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 5.30 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.76 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5214), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ORC6]] | +0.82 | +0.81 / +0.82 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS |
| [[CLSPN]] | +0.80 | +0.77 / +0.79 | both halves | 7e-06 |  |
| [[CHAF1A]] | +0.80 | +0.74 / +0.81 | both halves | 7e-06 |  |
| [[PKMYT1]] | +0.79 | +0.73 / +0.80 | both halves | 7e-06 |  |
| [[MCM10]] | +0.77 | +0.76 / +0.75 | both halves | 7e-06 |  |
| [[E2F1]] | +0.77 | +0.72 / +0.77 | both halves | 7e-06 |  |
| [[ATAD5]] | +0.77 | +0.72 / +0.77 | both halves | 7e-06 |  |
| [[GINS1]] | +0.76 | +0.72 / +0.75 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS |
| [[ZGRF1]] | +0.76 | +0.70 / +0.76 | both halves | 7e-06 |  |
| [[GINS4]] | +0.75 | +0.69 / +0.80 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS |
| [[RAD51AP1]] | +0.75 | +0.72 / +0.74 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS |
| [[FANCI]] | +0.75 | +0.65 / +0.76 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 4, C 3.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TCF19]] | B | TCF19 activity raises PSMC3IP's level | lines that do not express TCF19 (5) vs lines expressing it (45) | 1.84× lower at baseline in the lines without TCF19 | 0.034 | ⚠ within organs, on part of the lines; also absent: CLSPN, AURKB, SMARCD3; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers PSMC3IP's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 6.2% of all compounds | 0.047 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[TP73]] | B | TP73 activity raises PSMC3IP's level | lines that do not express TP73 (14) vs lines expressing it (36) | 1.40× lower at baseline in the lines without TP73 | 0.093 | ⚠ within organs, on part of the lines; also absent: SPTB, PRR36, EMID1; maybe low, not absent |
| [[ZNF66]] | B | ZNF66 activity raises PSMC3IP's level | lines that do not express ZNF66 (12) vs lines expressing it (38) | 1.27× lower at baseline in the lines without ZNF66 | 0.094 | ⚠ within organs, on part of the lines; also absent: ZNF737, ZNF100, ZNF85 |
| [[E2F1]] | C | E2F1 activity raises PSMC3IP's level | lines that do not express E2F1 (3) vs lines expressing it (47) | 2.09× lower at baseline in the lines without E2F1 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: MCM10, AURKB, ENSG00000197332; maybe low, not absent; its own permutation p |
| [[CDC45]] | C | CDC45 activity raises PSMC3IP's level | lines that do not express CDC45 (3) vs lines expressing it (47) | 1.89× lower at baseline in the lines without CDC45 | 0.062 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: CLSPN, SLC44A2, AURKB; maybe low, not absent |
| [[CLSPN]] | C | CLSPN activity raises PSMC3IP's level | lines that do not express CLSPN (4) vs lines expressing it (46) | 1.75× lower at baseline in the lines without CLSPN | 0.064 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: TCF19, CDC45, RRM2; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 006]] — E2F targets; 236 genes; this gene is in the **+** arm (projection on the module's main direction 0.737). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (-36.8, -46.9); signed map (-40.6, -45.5). **Vector** length 78.5, 18.5% of its response variance represented; |z| ≥ 3 in 1,002 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *DNA strand elongation* (reactome, mean cos +0.62 to 28); *DNA Replication* (reactome, mean cos +0.62 to 40); *E2F G1/S* (control, mean cos +0.61 to 23).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | +3.6 | +8.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~71% of this change | +3.4 | +4.7 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~64% of this change | +3.4 | +7.2 |
|  | [[Cytarabine (drug)]] 5 µM | ⚠ cell-cycle shift | +3.0 | +1.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | +3.0 | +11.0 |
|  | [[Cytarabine (hydrochloride) (drug)]] 0.05 µM |  | +2.1 | +1.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | +2.0 | +3.3 |
|  | [[Irinotecan (hydrochloride) (drug)]] 5 µM |  | +2.0 | +1.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.9 | +6.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.9 | +5.3 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -4.5 | -2.0 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | -3.4 | -3.6 |
|  | [[palbociclib (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~88% of this change | -2.1 | -3.5 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -2.1 | +0.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.1 | -1.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.0 | -1.3 |
|  | [[palbociclib (drug)]] 5 µM |  | -2.0 | -1.8 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -1.7 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | PSMC3 interacting protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q21.2 — chr17:42,572,310-42,577,831 (-) |
| Ensembl biotype | protein_coding |
| Also known as | TBPIP, GT198, HUMGT198A, Hop2 |
| Hallmark sets | E2F_TARGETS |
| Reactome | 4 pathways, smallest: Meiotic recombination; Meiosis; Reproduction |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9P2W1](https://www.uniprot.org/uniprotkb/Q9P2W1) (Homologous-pairing protein 2 homolog):

> Plays an important role in meiotic recombination. Stimulates DMC1-mediated strand exchange required for pairing homologous chromosomes during meiosis. The complex PSMC3IP/MND1 binds DNA, stimulates the recombinase activity of DMC1 as well as DMC1 D-loop formation from double-strand DNA. This complex stabilizes presynaptic RAD51 and DMC1 filaments formed on single strand DNA to capture double-strand DNA. This complex stimulates both synaptic and presynaptic critical steps in RAD51 and …

**Summary**, from NCBI Gene [29893](https://www.ncbi.nlm.nih.gov/gene/29893):

> This gene encodes a protein that functions in meiotic recombination. It is a subunit of the PSMC3IP/MND1 complex, which interacts with PSMC3/TBP1 to stimulate DMC1- and RAD51-mediated strand exchange during meiosis. The protein encoded by this gene can also co-activate ligand-driven transcription mediated by estrogen, androgen, glucocorticoid, progesterone, and thyroid nuclear receptors. Mutations in this gene cause XX female gonadal dysgenesis. Alternative splicing of this gene results in …

**Accessions** — [HGNC:17928](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17928) · Entrez [29893](https://www.ncbi.nlm.nih.gov/gene/29893) · UniProt [Q9P2W1](https://www.uniprot.org/uniprotkb/Q9P2W1) · Ensembl [ENSG00000131470](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000131470)

## Data

Gene col 5214: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5214); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5214, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5214]; `tensor/DDL_lfc|DDL_z.npy` [5214]; `embed/gene_vectors.npy` [5214]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5214 or target_col == 5214). Every well: [[PSMC3IP — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PSMC3IP.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
