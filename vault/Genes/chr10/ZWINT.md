---
symbol: "ZWINT"
type: "gene"
col: 4387
ensembl_id: "ENSG00000122952"
name: "ZW10 interacting kinetochore protein"
location: "10q21.1"
module: 6
arm: "+"
pooled_cpm: 12.85
n_lines_expressing: 49
n_dd_up: 20
n_dd_down: 13
n_dd_up_clean: 3
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 20
direction_downstream: 0
tags: ["gene", "module/006"]
generated_by: "tahoemap"
---

# ZWINT

*ZW10 interacting kinetochore protein* — 10q21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (17 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 4.05× (z +13.3, q 2e-37, up in 33 of 36 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~72% of this change. The strongest without an alert is [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM: 1.40× (z +4.5, q 3e-04, up in 22 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (8 with an alert ⚠); the strongest is [[palbociclib (drug)]] 0.5 µM: 0.430× (z -5.7, q 5e-06, down in 30 of 47 measured lines) ⚠ cell-cycle shift, explains ~58% of this change. The strongest without an alert is [[Neratinib (maleate) (drug)]] 5 µM: 0.746× (z -4.0, q 0.010, down in 20 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[E2F8]] (+0.85, fdr 7e-06), [[ESCO2]] (+0.84, fdr 7e-06), [[MCM2]] (+0.84, fdr 7e-06).
> It sits in the **+** arm of [[Module 006]] (E2F targets).
> Probable direction (from the cell lines, not proof of direct regulation): 20 arrows point to it, the strongest [[E2F8]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 17 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 17 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4387.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~72% of this change | **4.05×** | +13.3 | 2e-37 | 33/36 (A-427, PANC-1, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~66% of this change | **3.96×** | +12.6 | 8e-34 | 23/23 (A498, A-172, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~71% of this change | **2.61×** | +8.4 | 7e-15 | 22/25 (A498, NCI-H2347, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~66% of this change | **1.88×** | +5.7 | 1e-06 | 27/45 (LOX-IMVI, PANC-1, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **1.82×** | +5.7 | 1e-06 | 26/46 (J82, PANC-1, …) | all doses, stronger at high dose | position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~59% of this change | **1.77×** | +5.4 | 6e-06 | 24/37 (PANC-1, HT-29, …) | inconsistent across doses | low cells (technical?) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~79% of this change | **1.77×** | +5.2 | 2e-05 | 25/45 (LOX-IMVI, SK-MEL-2, …) | top dose only | position effect removed |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.70×** | +5.0 | 3e-05 | 26/46 (A549, NCI-H2030, …) | all doses, stronger at high dose | position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~85% of this change | **1.73×** | +5.0 | 4e-05 | 27/43 (SW480, LOX-IMVI, …) | top dose only | position effect removed |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~76% of this change | **1.44×** | +4.8 | 7e-05 | 23/47 (SW480, NCI-H460, …) | top dose only | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~57% of this change | **1.68×** | +4.7 | 1e-04 | 21/38 (PANC-1, J82, …) | all doses, stronger at high dose | position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~87% of this change | **1.67×** | +4.6 | 2e-04 | 19/38 (NCI-H23, Hs 766T, …) | top dose only | position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.40×** | +4.5 | 3e-04 | 22/47 (SW480, PANC-1, …) | rises with dose | position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~84% of this change | **1.37×** | +4.2 | 0.001 | 19/45 (NCI-H2347, PANC-1, …) | rises with dose | position effect removed |
| [[Trifluridine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~73% of this change | **1.52×** | +4.0 | 0.002 | 20/47 (LS 180, SW480, …) | two highest doses |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.49×** | +3.6 | 0.011 | 16/46 (J82, HOP62, …) | top dose only | position effect removed |
| [[Retinoic acid (drug)]] 0.05 µM |  | **1.37×** | +3.0 | 0.090 | 11/47 (A498, NCI-H460, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 8 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4387.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[palbociclib (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~58% of this change | **0.430×** | -5.7 | 5e-06 | 30/47 (SW480, KATO III, …) | two highest doses | noisy plate (z scaled); position effect removed |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~58% of this change | **0.577×** | -5.0 | 2e-04 | 23/45 (LS 180, HCT15, …) | inconsistent across doses | position effect removed |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | **0.646×** | -4.2 | 0.006 | 20/46 (LoVo, LS 180, …) | all doses, flat |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **0.746×** | -4.0 | 0.010 | 20/47 (LoVo, Hs 766T, …) | rises with dose | position effect removed |
| [[4EGI-1 (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~63% of this change | **0.580×** | -3.7 | 0.021 | 18/47 (Hs 766T, SNU-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~86% of this change | **0.761×** | -3.7 | 0.021 | 24/47 (SW480, J82, …) | rises with dose |  |
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.690×** | -3.6 | 0.031 | 11/47 (SW480, J82, …) | inconsistent across doses |  |
| [[Neratinib (maleate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~80% of this change | **0.697×** | -3.4 | 0.035 | 16/44 (Hs 766T, HCT15, …) | rises with dose | position effect removed |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~87% of this change | **0.697×** | -3.4 | 0.035 | 18/47 (MIA PaCa-2, COLO 205, …) | all doses, flat |  |
| [[Temsirolimus (drug)]] 0.5 µM |  | **0.702×** | -3.4 | 0.040 | 16/44 (NCI-H460, RKO, …) | two highest doses | position effect removed |
| [[BAY1125976 (drug)]] 5 µM |  | **0.526×** | -3.2 | 0.070 | 13/47 (LoVo, LS 180, …) | top dose only | plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Rapamycin (drug)]] 5 µM |  | **0.791×** | -3.2 | 0.071 | 16/47 (MIA PaCa-2, RPMI-7951, …) | all doses, flat |  |
| [[Rapamycin (drug)]] 0.5 µM |  | **0.723×** | -3.1 | 0.082 | 15/45 (CFPAC-1, COLO 205, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +1.15 per unit of S-phase module lfc, +0.32 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4387. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LS 180 (line)]] | wt | 15.2 | 0 | 4 (3 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.152× (z -11.2) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Amsacrine (drug)]] 5 µM 0.231× (z -8.7) |
| [[H4 (line)]] | wt | 12.6 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 0.05 µM 0.0443× (z -10.1) |
| [[A498 (line)]] | wt | 14.5 | 0 | 2 (2 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.131× (z -16.1) ⚠ cell-cycle shift, would explain all of this change |
| [[A-172 (line)]] | wt | 14.2 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.183× (z -10.1) ⚠ cell-cycle shift, would explain all of this change |
| [[A-427 (line)]] | wt | 22.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.57× (z +10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~72% of this change | — |
| [[AN3 CA (line)]] | alt | 24.7 | 0 | 1 | — | [[Valdecoxib (drug)]] 0.05 µM 0.0828× (z -8.9) |
| [[HCT15 (line)]] | alt | 24.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.229× (z -9.0) ⚠ cell-cycle shift, would explain all of this change |
| [[HEC-1-A (line)]] | alt | 23.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.23× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~72% of this change | — |
| [[J82 (line)]] | alt | 17.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.02× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~72% of this change | — |
| [[LoVo (line)]] | wt | 7.49 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 0.5 µM 0.0564× (z -12.7) ⚠ cell-cycle shift, would explain all of this change |
| [[LOX-IMVI (line)]] | wt | 9.59 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.163× (z -11.7) ⚠ cell-cycle shift, would explain all of this change |
| [[PANC-1 (line)]] | alt | 14.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.85× (z +9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~72% of this change | — |
| [[SHP-77 (line)]] | alt | 10.00 | 0 | 1 | — | [[Cepharanthine (drug)]] 0.5 µM 0.0867× (z -9.8) |
| [[SNU-423 (line)]] | alt | 13.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.60× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~72% of this change | — |
| [[SW480 (line)]] | alt | 27.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.51× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~72% of this change | — |
| [[A549 (line)]] | wt | 6.30 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.79 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 19.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.22 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 7.80 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 9.73 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.40 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 9.69 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 10.3 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 4.31 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.91 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 7.39 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 4.45 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 5.45 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.62 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 13.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.92 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 14.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 7.37 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 9.13 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 9.47 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 13.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4387), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[E2F8]] | +0.85 | +0.82 / +0.86 | both halves | 7e-06 | STRING 766 |
| [[ESCO2]] | +0.84 | +0.81 / +0.86 | both halves | 7e-06 | STRING 413 |
| [[MCM2]] | +0.84 | +0.83 / +0.84 | both halves | 7e-06 | pathway: Cell Cycle Checkpoints; STRING 446 |
| [[MYBL2]] | +0.83 | +0.80 / +0.84 | both halves | 7e-06 | STRING 541 |
| [[MCM4]] | +0.83 | +0.81 / +0.82 | both halves | 7e-06 | pathway: Cell Cycle Checkpoints; STRING 606 |
| [[SKA3]] | +0.83 | +0.80 / +0.86 | both halves | 7e-06 | STRING 726 |
| [[CENPH]] | +0.83 | +0.82 / +0.82 | both halves | 7e-06 | pathway: Amplification  of signal from unattached  kinetochores via a MAD2  inhibitory signal; STRING 613 |
| [[PKMYT1]] | +0.82 | +0.81 / +0.83 | both halves | 7e-06 | pathway: Cell Cycle Checkpoints |
| [[PLK4]] | +0.82 | +0.80 / +0.80 | both halves | 7e-06 | pathway: Mitotic Prometaphase; STRING 557 |
| [[CENPU]] | +0.82 | +0.84 / +0.83 | both halves | 7e-06 | pathway: Amplification  of signal from unattached  kinetochores via a MAD2  inhibitory signal; STRING 829 |
| [[TIMELESS]] | +0.81 | +0.76 / +0.81 | both halves | 7e-06 | STRING 400 |
| [[GINS1]] | +0.81 | +0.77 / +0.80 | both halves | 7e-06 | STRING 849 |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*20 arrows, 20 of them with an alert ⚠; grade A 0, B 10, C 10. Shown: the 12 strongest; 8 more arrows (8 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[E2F8]] | B | E2F8 activity raises ZWINT's level | lines that do not express E2F8 (5) vs lines expressing it (45) | 2.39× lower at baseline in the lines without E2F8 | 0.009 | ⚠ across organs; also absent: CYB561, NMRAL1, RRM2; maybe low, not absent |
| [[TCF19]] | B | TCF19 activity raises ZWINT's level | lines that do not express TCF19 (5) vs lines expressing it (45) | 2.33× lower at baseline in the lines without TCF19 | 0.011 | ⚠ within organs, on part of the lines; also absent: CLSPN, AURKB, SMARCD3; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers ZWINT's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.2% of all compounds | 0.024 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[FAM111B]] | B | FAM111B activity raises ZWINT's level | lines that do not express FAM111B (10) vs lines expressing it (40) | 1.60× lower at baseline in the lines without FAM111B | 0.031 | ⚠ within organs, on part of the lines; also absent: E2F8, SLC37A2; maybe low, not absent |
| [[POGLUT3]] | B | POGLUT3 activity raises ZWINT's level | lines that do not express POGLUT3 (5) vs lines expressing it (45) | 1.50× lower at baseline in the lines without POGLUT3 | 0.047 | ⚠ within organs, on part of the lines; also absent: DENND2B, MEX3A, CAMKK1 |
| [[ZNF724]] | B | ZNF724 activity raises ZWINT's level | lines that do not express ZNF724 (8) vs lines expressing it (42) | 1.42× lower at baseline in the lines without ZNF724 | 0.048 | ⚠ within organs, on part of the lines; also absent: ENSG00000283201, ENSG00000269237, ZNF577 |
| [[MYBL1]] | B | MYBL1 activity raises ZWINT's level | lines that do not express MYBL1 (8) vs lines expressing it (42) | 1.64× lower at baseline in the lines without MYBL1 | 0.054 | ⚠ within organs, on part of the lines; also absent: NCS1, KCNC4, JAZF1; maybe low, not absent |
| [[ZNF66]] | B | ZNF66 activity raises ZWINT's level | lines that do not express ZNF66 (12) vs lines expressing it (38) | 1.23× lower at baseline in the lines without ZNF66 | 0.084 | ⚠ within organs, on part of the lines; also absent: ZNF737, ZNF100, ZNF85 |
| [[CDC25A]] | B | CDC25A activity raises ZWINT's level | lines that do not express CDC25A (5) vs lines expressing it (45) | 1.88× lower at baseline in the lines without CDC25A | 0.095 | ⚠ within organs, on part of the lines; also absent: ZNF367, E2F1, ALDH1B1; maybe low, not absent |
| [[E2F2]] | B | E2F2 activity raises ZWINT's level | lines that do not express E2F2 (13) vs lines expressing it (37) | 1.81× lower at baseline in the lines without E2F2 | 0.096 | ⚠ within organs, on part of the lines; also absent: ENSG00000260498, ABHD11, BRSK2; maybe low, not absent |
| [[MCM10]] | C | MCM10 activity raises ZWINT's level | lines that do not express MCM10 (4) vs lines expressing it (46) | 2.47× lower at baseline in the lines without MCM10 | 0.021 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: E2F1, AURKB, ENSG00000197332; maybe low, not absent |
| [[AURKB]] | C | AURKB activity raises ZWINT's level | lines that do not express AURKB (4) vs lines expressing it (46) | 2.60× lower at baseline in the lines without AURKB | 0.022 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: TCF19, SMARCD3, CDC45; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 006]] — E2F targets; 236 genes; this gene is in the **+** arm (projection on the module's main direction 0.835). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (-37.3, -44.9); signed map (-38.9, -47.1). **Vector** length 108, 28.9% of its response variance represented; |z| ≥ 3 in 1,035 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *E2F targets* (hallmark, mean cos +0.64 to 65); *DNA strand elongation* (reactome, mean cos +0.66 to 28); *DNA Replication* (reactome, mean cos +0.65 to 40).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~66% of this change | +5.6 | +12.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~72% of this change | +5.5 | +13.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~48% of this change | +5.2 | +5.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~71% of this change | +4.2 | +8.4 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~66% of this change | +4.0 | +5.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.1 | +4.5 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +2.4 | +3.0 |
|  | [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | +2.3 | +1.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | +2.2 | +2.5 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | +2.2 | +1.4 |
| fall | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | -5.4 | -4.2 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~58% of this change | -3.9 | -5.0 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -3.6 | -4.0 |
|  | [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~87% of this change | -3.3 | -3.4 |
|  | [[palbociclib (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~58% of this change | -3.3 | -5.7 |
|  | [[Rapamycin (drug)]] 5 µM |  | -2.8 | -3.2 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.7 | -2.2 |
|  | [[Temsirolimus (drug)]] 5 µM |  | -2.7 | -2.6 |
|  | [[palbociclib (drug)]] 5 µM |  | -2.2 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | ZW10 interacting kinetochore protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q21.1 — chr10:56,357,227-56,361,273 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KNTC2AP, SIP30, Zwint1 |
| Gene groups (HGNC) | KNL1 complex |
| Hallmark sets | DNA_REPAIR |
| Reactome | 17 pathways, smallest: Amplification  of signal from unattached  kinetochores via a MAD2  inhibitory signal; Amplification of signal from the kinetochores; EML4 and NUDC in mitotic spindle formation |
| Matched by | ensembl_id |

**Function**, from UniProt [O95229](https://www.uniprot.org/uniprotkb/O95229) (Outer kinetochore KNL1 complex subunit ZWINT):

> Acts as a component of the outer kinetochore KNL1 complex that serves as a docking point for spindle assembly checkpoint components and mediates microtubule-kinetochore interactions. Kinetochores, consisting of a centromere-associated inner segment and a microtubule-contacting outer segment, play a crucial role in chromosome segregation by mediating the physical connection between centromeric DNA and spindle microtubules. The outer kinetochore is made up of the ten-subunit KMN network, …

**Summary**, from NCBI Gene [11130](https://www.ncbi.nlm.nih.gov/gene/11130):

> This gene encodes a protein that is clearly involved in kinetochore function although an exact role is not known. It interacts with ZW10, another kinetochore protein, possibly regulating the association between ZW10 and kinetochores. The encoded protein localizes to prophase kinetochores before ZW10 does and it remains detectable on the kinetochore until late anaphase. It has a uniform distribution in the cytoplasm of interphase cells. Alternatively spliced transcript variants encoding …

**Accessions** — [HGNC:13195](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13195) · Entrez [11130](https://www.ncbi.nlm.nih.gov/gene/11130) · UniProt [O95229](https://www.uniprot.org/uniprotkb/O95229) · Ensembl [ENSG00000122952](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000122952)

## Data

Gene col 4387: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4387); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4387, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4387]; `tensor/DDL_lfc|DDL_z.npy` [4387]; `embed/gene_vectors.npy` [4387]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4387 or target_col == 4387). Every well: [[ZWINT — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZWINT.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
