---
symbol: "POLD1"
type: "gene"
col: 717
ensembl_id: "ENSG00000062822"
name: "DNA polymerase delta 1, catalytic subunit"
location: "19q13.33"
module: 6
arm: "+"
pooled_cpm: 13.29
n_lines_expressing: 50
n_dd_up: 17
n_dd_down: 5
n_dd_up_clean: 2
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/006"]
generated_by: "tahoemap"
---

# POLD1

*DNA polymerase delta 1, catalytic subunit* — 19q13.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (15 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.16× (z +11.4, q 3e-27, up in 30 of 37 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 1.79× (z +8.5, q 2e-15, up in 30 of 46 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 2 lines (LoVo 4.94×, SW480 2.84×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (NCI-H460 2.83×; ⚠ cell-cycle shift, explains ~0% of this change).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (2 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 0.717× (z -6.9, q 2e-09, down in 22 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[POLE]] (+0.81, fdr 7e-06), [[MYBL2]] (+0.80, fdr 7e-06), [[TONSL]] (+0.80, fdr 7e-06).
> It sits in the **+** arm of [[Module 006]] (E2F targets).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TCF19]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 15 with an alert ⚠; shown: the 15 strongest. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 15 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 717.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 2 lines (LoVo 4.94×, SW480 2.84×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (NCI-H460 2.83×; ⚠ cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change | **2.16×** | +11.4 | 3e-27 | 30/37 (LoVo, SW480, …) | all doses, flat | composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | **1.97×** | +10.0 | 4e-21 | 27/47 (SW480, A549, …) | rises with dose | position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.79×** | +8.5 | 2e-15 | 30/46 (LoVo, HT-29, …) | top dose only | position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~64% of this change | **1.77×** | +8.1 | 9e-14 | 13/23 (NCI-H2030, A-172, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | **1.79×** | +7.9 | 3e-13 | 21/31 (CFPAC-1, HOP62, …) | all doses, flat | composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~63% of this change | **1.69×** | +7.7 | 1e-12 | 29/47 (LoVo, SW480, …) | rises with dose | position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~69% of this change | **1.62×** | +7.1 | 7e-11 | 22/47 (SW480, HT-29, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.49×** | +5.9 | 3e-07 | 20/47 (SW480, SHP-77, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~35% of this change | **1.50×** | +5.7 | 6e-07 | 22/43 (A-427, LoVo, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.39×** | +4.9 | 6e-05 | 16/47 (SW480, SHP-77, …) | all doses, flat |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.34×** | +4.3 | 8e-04 | 15/46 (SW480, J82, …) | all doses, stronger at high dose | position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **1.62×** | +3.7 | 0.011 | 14/46 (NCI-H460, NCI-H2347, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~17% here); composition shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.24×** | +3.2 | 0.056 | 11/47 (NCI-H460, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Cytarabine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~67% of this change | **1.25×** | +3.2 | 0.059 | 10/45 (A-427, SNU-423, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~83% of this change | **1.24×** | +3.2 | 0.059 | 10/46 (SW480, A549, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 3 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 717.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM |  | **0.717×** | -6.9 | 2e-09 | 22/48 (J82, A498, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~11% here) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.740×** | -4.4 | 0.002 | 20/46 (SW480, KATO III, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.743×** | -4.4 | 0.002 | 19/46 (Hs 766T, A-427, …) | rises with dose |  |
| [[Entrectinib (drug)]] 5 µM |  | **0.749×** | -4.3 | 0.003 | 15/47 (LoVo, NCI-H460, …) | top dose only |  |
| [[Cobimetinib (drug)]] 5 µM |  | **0.754×** | -4.0 | 0.007 | 14/46 (C32, NCI-H460, …) | top dose only | position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.932× | -3.7 | 0.017 | 9/48 (PANC-1, CFPAC-1, …) | inconsistent across doses |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 0.842× | -3.6 | 0.027 | 12/48 (SK-MEL-2, MIA PaCa-2, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.856× | -3.3 | 0.082 | 14/48 (LS 180, COLO 205, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | 0.810× | -3.1 | 0.12 | 16/47 (A498, RKO, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Rapamycin (drug)]] 5 µM |  | 0.866× | -3.0 | 0.14 | 6/48 (MIA PaCa-2, RKO, …) | rises with dose | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.63 per unit of S-phase module lfc, -0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 717. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[H4 (line)]] | wt | 26.2 | 0 | 2 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.118× (z -10.0) ⚠ transcription drop; cell-cycle shift, explains ~24% of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.243× (z -9.4) |
| [[J82 (line)]] | alt | 18.9 | 0 | 1 | — | [[Selinexor (drug)]] 5 µM 0.408× (z -9.3) |
| [[LoVo (line)]] | wt | 8.18 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.94× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 15.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.340× (z -8.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H460 (line)]] | wt | 8.49 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.83× (z +9.5) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[SHP-77 (line)]] | alt | 24.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.114× (z -14.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change |
| [[SW480 (line)]] | alt | 18.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.84× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change | — |
| [[A-172 (line)]] | wt | 15.7 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 19.9 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 16.2 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 11.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 5.34 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 34.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 8.39 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 6.84 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 12.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 8.51 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 24.3 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 41.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 7.26 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 8.65 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 7.15 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 13.1 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 11.1 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 6.40 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 5.32 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 7.98 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 9.97 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 7.93 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 17.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 14.5 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 6.76 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 8.35 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 10.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 10.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 717), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[POLE]] | +0.81 | +0.78 / +0.79 | both halves | 7e-06 | same gene group; pathway: HALLMARK_E2F_TARGETS; STRING 999 |
| [[MYBL2]] | +0.80 | +0.77 / +0.77 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS |
| [[TONSL]] | +0.80 | +0.79 / +0.74 | both halves | 7e-06 |  |
| [[RECQL4]] | +0.79 | +0.78 / +0.74 | both halves | 7e-06 | STRING 843 |
| [[UHRF1]] | +0.77 | +0.77 / +0.75 | both halves | 7e-06 |  |
| [[CDC45]] | +0.77 | +0.77 / +0.75 | both halves | 7e-06 | pathway: DNA Replication; STRING 886 |
| [[WDR76]] | +0.77 | +0.73 / +0.76 | both halves | 7e-06 |  |
| [[MCM5]] | +0.76 | +0.74 / +0.76 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 969 |
| [[FANCA]] | +0.76 | +0.76 / +0.73 | both halves | 7e-06 | STRING 564 |
| [[NCAPG2]] | +0.75 | +0.76 / +0.71 | both halves | 7e-06 |  |
| [[MCM3]] | +0.75 | +0.75 / +0.70 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 985 |
| [[MCM8]] | +0.74 | +0.70 / +0.73 | both halves | 7e-06 | pathway: DNA Replication; STRING 628 |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 1, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TCF19]] | B | TCF19 activity raises POLD1's level | lines that do not express TCF19 (5) vs lines expressing it (45) | 1.65× lower at baseline in the lines without TCF19 | 0.053 | ⚠ within organs, on part of the lines; also absent: CLSPN, AURKB, SMARCD3; maybe low, not absent |
| [[E2F1]], [[MCM3]] | C | E2F1, MCM3 activity raises POLD1's level | lines that do not express E2F1, MCM3 (3) vs lines expressing them (47) | 1.92× lower at baseline in the lines without E2F1, MCM3 | 0.066 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: MCM10, AURKB, ENSG00000197332; maybe low, not absent; co-absent genes |
| [[MCM10]] | C | MCM10 activity raises POLD1's level | lines that do not express MCM10 (4) vs lines expressing it (46) | 1.70× lower at baseline in the lines without MCM10 | 0.077 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: E2F1, AURKB, ENSG00000197332; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 006]] — E2F targets; 236 genes; this gene is in the **+** arm (projection on the module's main direction 0.753). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (-34.9, -43.1); signed map (-36.2, -45.7). **Vector** length 94.7, 19.9% of its response variance represented; |z| ≥ 3 in 946 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *E2F G1/S* (control, mean cos +0.62 to 23); *Cell Cycle Checkpoints* (reactome, mean cos +0.60 to 45); *Activation of the pre-replicative complex* (reactome, mean cos +0.64 to 22).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~64% of this change | +7.6 | +8.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | +6.9 | +7.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change | +6.9 | +11.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.4 | +8.5 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | +4.3 | +10.0 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.8 | +1.2 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +1.7 | +2.4 |
|  | [[Demeclocycline (drug)]] 5 µM |  | +1.6 | +1.1 |
|  | [[Arbutin (drug)]] 0.05 µM |  | +1.5 | +1.1 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | -4.4 | -4.4 |
|  | [[Selinexor (drug)]] 5 µM |  | -3.8 | -6.9 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -3.4 | -2.7 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.4 | -2.4 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | -3.0 | -4.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.4 | -1.2 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -2.4 | -3.6 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -2.2 | -1.9 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.2 | -3.0 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.9 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | DNA polymerase delta 1, catalytic subunit |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.33 — chr19:50,384,204-50,418,018 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CDC2; previously POLD |
| Gene groups (HGNC) | DNA polymerases |
| Hallmark sets | DNA_REPAIR, E2F_TARGETS |
| Reactome | 42 pathways, smallest: Cytosolic iron-sulfur cluster assembly; Leading Strand Synthesis; Mismatch repair (MMR) directed by MSH2:MSH3 (MutSbeta) |
| Matched by | ensembl_id |

**Function**, from UniProt [P28340](https://www.uniprot.org/uniprotkb/P28340) (DNA polymerase delta catalytic subunit):

> As the catalytic component of the trimeric (Pol-delta3 complex) and tetrameric DNA polymerase delta complexes (Pol-delta4 complex), plays a crucial role in high fidelity genome replication, including in lagging strand synthesis, and repair. Exhibits both DNA polymerase and 3'- to 5'-exonuclease activities. Requires the presence of accessory proteins POLD2, POLD3 and POLD4 for full activity. Depending upon the absence (Pol-delta3) or the presence of POLD4 (Pol-delta4), displays differences in …

**Summary**, from NCBI Gene [5424](https://www.ncbi.nlm.nih.gov/gene/5424):

> This gene encodes the 125-kDa catalytic subunit of DNA polymerase delta. DNA polymerase delta possesses both polymerase and 3' to 5' exonuclease activity and plays a critical role in DNA replication and repair. Alternatively spliced transcript variants have been observed for this gene, and a pseudogene of this gene is located on the long arm of chromosome 6. [provided by RefSeq, Mar 2012]

**Accessions** — [HGNC:9175](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9175) · Entrez [5424](https://www.ncbi.nlm.nih.gov/gene/5424) · UniProt [P28340](https://www.uniprot.org/uniprotkb/P28340) · Ensembl [ENSG00000062822](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000062822)

## Data

Gene col 717: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 717); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 717, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 717]; `tensor/DDL_lfc|DDL_z.npy` [717]; `embed/gene_vectors.npy` [717]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 717 or target_col == 717). Every well: [[POLD1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/POLD1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
