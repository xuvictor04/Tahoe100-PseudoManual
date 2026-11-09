---
symbol: "KICS2"
type: "gene"
col: 10472
ensembl_id: "ENSG00000174206"
name: "KICSTOR subunit 2"
location: "12q14.2"
module: 135
arm: "+"
pooled_cpm: 5.6
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 5
n_dd_up_clean: 8
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 1
direction_downstream: 1
tags: ["gene", "module/135"]
generated_by: "tahoemap"
---

# KICS2

*KICSTOR subunit 2* — 12q14.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 2.70× (z +10.8, q 3e-24, up in 33 of 39 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (4 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.612× (z -5.3, q 5e-05, down in 16 of 36 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change. The strongest without an alert is [[Ixazomib citrate (drug)]] 5 µM: 0.736× (z -3.3, q 0.096, down in 14 of 45 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 4 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Ouabain (Octahydrate) (drug)]] 0.5 µM in 2 lines (SW480 0.209×, PANC-1 0.239×; ⚠ cell-cycle shift, explains ~42% of this change); [[Belinostat (drug)]] 5 µM in 1 line (RKO 0.0443×; ⚠ cell-cycle shift, explains ~26% of this change); [[Digitoxin (drug)]] 5 µM in 1 line (PANC-1 0.181×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change); [[Asciminib (drug)]] 0.05 µM in 1 line (C32 0.0526×); [[Cobimetinib (drug)]] 0.5 µM in 1 line (RKO 0.0653×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TRMT5]] (+0.81, fdr 7e-06), [[ZNF507]] (+0.77, fdr 7e-06), [[ZXDB]] (+0.75, fdr 1e-05); moves opposite to [[CBFA2T2]] (-0.75, fdr 7e-06), [[GNB2]] (-0.72, fdr 1e-05), [[SAP130]] (-0.71, fdr 7e-06).
> It sits in the **+** arm of [[Module 135]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[FTCDNL1]] → it (grade B ⚠); 1 goes from it, the strongest it → [[CASTOR2]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 7 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10472.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.70×** | +10.8 | 3e-24 | 33/39 (NCI-H1573, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.87×** | +9.6 | 3e-19 | 29/40 (A-172, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.75×** | +8.6 | 2e-15 | 25/45 (A-427, A549, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Harringtonine (drug)]] 5 µM |  | **2.23×** | +8.3 | 1e-14 | 31/42 (NCI-H1573, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **2.06×** | +7.9 | 5e-13 | 35/45 (NCI-H1573, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.61×** | +7.3 | 3e-11 | 26/47 (NCI-H460, SNU-423, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.58×** | +7.0 | 2e-10 | 24/40 (HOP62, PANC-1, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.71×** | +5.8 | 5e-07 | 22/43 (NCI-H460, LoVo, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.61×** | +4.8 | 1e-04 | 5/14 (NCI-H460, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.46×** | +3.9 | 0.005 | 5/25 (NCI-H1573, A-172, …) | inconsistent across doses | cell-cycle shift (explains ~22% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.09× | +3.5 | 0.022 | 4/48 (NCI-H2030, J82, …) | inconsistent across doses |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.38×** | +3.5 | 0.022 | 9/46 (NCI-H1573, A-172, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.35×** | +3.2 | 0.055 | 6/44 (A-172, HOP62, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~75% of this change | **1.34×** | +3.2 | 0.055 | 8/43 (NCI-H460, A-427, …) | all doses, stronger at high dose |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.34×** | +3.1 | 0.066 | 6/44 (NCI-H1573, CFPAC-1, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 4 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10472.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 4 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Ouabain (Octahydrate) (drug)]] 0.5 µM in 2 lines (SW480 0.209×, PANC-1 0.239×; ⚠ cell-cycle shift, explains ~42% of this change); [[Belinostat (drug)]] 5 µM in 1 line (RKO 0.0443×; ⚠ cell-cycle shift, explains ~26% of this change); [[Digitoxin (drug)]] 5 µM in 1 line (PANC-1 0.181×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change); [[Asciminib (drug)]] 0.05 µM in 1 line (C32 0.0526×); [[Cobimetinib (drug)]] 0.5 µM in 1 line (RKO 0.0653×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **0.612×** | -5.3 | 5e-05 | 16/36 (PANC-1, HOP62, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~60% of this change | **0.714×** | -3.7 | 0.066 | 14/47 (PANC-1, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.725×** | -3.5 | 0.087 | 11/45 (PANC-1, C-33 A, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.736×** | -3.3 | 0.096 | 14/45 (PANC-1, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.736×** | -3.3 | 0.096 | 13/45 (SW480, PANC-1, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.05 per unit of S-phase module lfc, -0.44 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10472. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 8.69 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.181× (z -10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change |
| [[RKO (line)]] | wt | 5.27 | 0 | 2 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0443× (z -10.4) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Cobimetinib (drug)]] 0.5 µM 0.0653× (z -9.1) |
| [[C32 (line)]] | wt | 4.84 | 0 | 1 | — | [[Asciminib (drug)]] 0.05 µM 0.0526× (z -9.3) |
| [[NCI-H23 (line)]] | alt | 12.9 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.172× (z -9.5) ⚠ toxic; cell-cycle shift, explains ~78% of this change |
| [[SW480 (line)]] | alt | 8.36 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.209× (z -9.0) ⚠ cell-cycle shift, explains ~42% of this change |
| [[A-172 (line)]] | wt | 4.12 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 13.4 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 6.63 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 5.64 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.43 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.51 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 8.02 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.99 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.64 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 6.37 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.46 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 5.56 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.12 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 5.50 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.40 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 3.14 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.87 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.73 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.84 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.08 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.45 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 7.59 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 7.00 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.60 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.95 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 5.29 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 7.38 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 4.55 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 4.94 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.57 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.04 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 9.42 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.87 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.86 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.66 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.78 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 9.43 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.69 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.45 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 4.14 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.88 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.31 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.51 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 4.60 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 5.77 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10472), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*77 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TRMT5]] | +0.81 | +0.84 / +0.66 | both halves | 7e-06 |  |
| [[ZNF507]] | +0.77 | +0.81 / +0.61 | both halves | 7e-06 |  |
| [[ZXDB]] | +0.75 | +0.69 / +0.55 | both halves | 1e-05 |  |
| [[MTPAP]] | +0.73 | +0.71 / +0.68 | both halves | 7e-06 |  |
| [[UTP15]] | +0.72 | +0.73 / +0.62 | both halves | 7e-06 |  |
| [[ZXDA]] | +0.72 | +0.69 / +0.43 | both halves | 3e-05 |  |
| [[DPH5-DT]] | +0.72 | +0.79 / +0.47 | both halves | 2e-05 |  |
| [[MTHFSD]] | +0.72 | +0.75 / +0.47 | both halves | 2e-05 |  |
| [[BCDIN3D]] | +0.71 | +0.75 / +0.51 | both halves | 1e-05 |  |
| [[NEK9]] | +0.71 | +0.78 / +0.54 | both halves | 1e-05 |  |
| [[TRMT13]] | +0.70 | +0.77 / +0.54 | both halves | 1e-05 |  |
| [[GPATCH4]] | +0.69 | +0.75 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*23 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CBFA2T2]] | -0.75 | -0.77 / -0.58 | both halves | 7e-06 |  |
| [[GNB2]] | -0.72 | -0.70 / -0.54 | both halves | 1e-05 |  |
| [[SAP130]] | -0.71 | -0.75 / -0.58 | both halves | 7e-06 |  |
| [[GNAI2]] | -0.71 | -0.66 / -0.53 | both halves | 1e-05 |  |
| [[CARHSP1]] | -0.69 | -0.71 / -0.46 | both halves | 3e-05 |  |
| [[TRIM62]] | -0.68 | -0.64 / -0.52 | both halves | 1e-05 |  |
| [[COX6A1]] | -0.68 | -0.61 / -0.44 | both halves | 3e-05 |  |
| [[CABLES2]] | -0.67 | -0.57 / -0.43 | both halves | 3e-05 |  |
| [[GMCL1]] | -0.67 | -0.67 / -0.49 | both halves | 1e-05 |  |
| [[ADIPOR1]] | -0.67 | -0.63 / -0.56 | both halves | 1e-05 |  |
| [[SDHAP2]] | -0.66 | -0.73 / -0.45 | both halves | 3e-05 |  |
| [[MOSPD3]] | -0.65 | -0.71 / -0.46 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FTCDNL1]] | B | FTCDNL1 activity raises KICS2's level | lines that do not express FTCDNL1 (11) vs lines expressing it (39) | 1.45× lower at baseline in the lines without FTCDNL1 | 0.052 | ⚠ within organs, on part of the lines; also absent: RHBDL3, SCN8A, DLX1; maybe low, not absent |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CASTOR2]] | C | KICS2's natural level strengthens CASTOR2's drug response | KICS2's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.62, reverse -0.20; direction not clear | 0.081 | ⚠ tissue can mimic it; precision caveat; direction unclear |

## Where it sits

- **Module**: [[Module 135]]; 35 genes; this gene is in the **+** arm (projection on the module's main direction 0.649). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.39).
- **Nodal map** (x, y) = (-18.3, 6.2); signed map (9.9, -30.2). **Vector** length 72.6, 12.0% of its response variance represented; |z| ≥ 3 in 1,051 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +6.7 | +10.8 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +5.7 | +7.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.8 | +5.8 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | +4.5 | +8.6 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.3 | +9.6 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.8 | +3.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.6 | +7.3 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.3 | +1.9 |
|  | [[TAK-733 (drug)]] 5 µM |  | +1.9 | +2.8 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | -4.1 | -1.6 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.5 | -1.0 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -3.5 | +1.1 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.6 | +0.9 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.2 | +0.2 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.7 | -0.3 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -1.6 | -1.7 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.5 | -0.4 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.5 | -1.8 |
|  | [[HI-TOPK-032 (drug)]] 0.5 µM |  | -1.2 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | KICSTOR subunit 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q14.2 — chr12:64,186,316-64,222,296 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ32549; previously C12orf66 |
| Gene groups (HGNC) | KICSTOR complex |
| Reactome | 4 pathways, smallest: Amino acids regulate mTORC1; Cellular response to starvation; Cellular responses to stress |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96MD2](https://www.uniprot.org/uniprotkb/Q96MD2) (KICSTOR subunit 2):

> As part of the KICSTOR complex functions in the amino acid-sensing branch of the TORC1 signaling pathway. Recruits, in an amino acid-independent manner, the GATOR1 complex to the lysosomal membranes and allows its interaction with GATOR2 and the RAG GTPases. Functions upstream of the RAG GTPases and is required to negatively regulate mTORC1 signaling in absence of amino acids. In absence of the KICSTOR complex mTORC1 is constitutively localized to the lysosome and activated. The KICSTOR complex …

**Summary**, from NCBI Gene [144577](https://www.ncbi.nlm.nih.gov/gene/144577):

> Involved in several processes, including cellular response to amino acid starvation; cellular response to glucose starvation; and negative regulation of TORC1 signaling. Part of KICSTOR complex. Implicated in autosomal recessive intellectual developmental disorder 83. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:26517](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26517) · Entrez [144577](https://www.ncbi.nlm.nih.gov/gene/144577) · UniProt [Q96MD2](https://www.uniprot.org/uniprotkb/Q96MD2) · Ensembl [ENSG00000174206](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000174206)

## Data

Gene col 10472: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10472); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10472, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10472]; `tensor/DDL_lfc|DDL_z.npy` [10472]; `embed/gene_vectors.npy` [10472]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10472 or target_col == 10472). Every well: [[KICS2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KICS2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
