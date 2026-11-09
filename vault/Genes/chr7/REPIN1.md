---
symbol: "REPIN1"
type: "gene"
col: 13163
ensembl_id: "ENSG00000214022"
name: "replication initiator 1"
location: "7q36.1"
module: 16
arm: "+"
pooled_cpm: 13.13
n_lines_expressing: 49
n_dd_up: 20
n_dd_down: 4
n_dd_up_clean: 13
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/016"]
generated_by: "tahoemap"
---

# REPIN1

*replication initiator 1* — 7q36.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (7 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.17× (z +19.1, q 0e+00, up in 40 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (2 with an alert ⚠); the strongest is [[Verteporfin (drug)]] 5 µM: 0.699× (z -4.0, q 0.026, down in 22 of 45 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Niclosamide (olamine) (drug)]] 5 µM in 1 line (BT-474 0.146×; ⚠ toxic); [[Doxycycline (monohydrate) (drug)]] 5 µM in 1 line (HOP62 0.0755×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (MIA PaCa-2 0.351×; ⚠ cell-cycle shift, explains ~33% of this change); [[Cysteamine (hydrochloride) (drug)]] 0.5 µM in 1 line (CHP-212 0.0782×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PBX2]] (+0.74, fdr 7e-06), [[CLK4]] (+0.72, fdr 7e-06), [[ZNF480]] (+0.71, fdr 7e-06); moves opposite to [[RECQL]] (-0.71, fdr 7e-06), [[MFN1]] (-0.70, fdr 7e-06), [[PIGF]] (-0.68, fdr 1e-05).
> It sits in the **+** arm of [[Module 016]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[DDR1]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 7 with an alert ⚠. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13163.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **3.17×** | +19.1 | 0e+00 | 40/44 (A498, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **3.43×** | +13.9 | 3e-41 | 39/45 (A498, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.50×** | +10.3 | 1e-22 | 16/22 (LS 180, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.33×** | +9.9 | 6e-21 | 36/43 (A498, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.28×** | +9.6 | 8e-20 | 29/36 (KATO III, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **2.17×** | +9.1 | 1e-17 | 35/46 (A498, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~30% of this change | **1.76×** | +6.6 | 3e-09 | 28/40 (PANC-1, A549, …) | inconsistent across doses | low cells (technical?) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.59×** | +5.4 | 5e-06 | 26/46 (A498, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.75×** | +5.3 | 6e-06 | 14/28 (SW1417, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM |  | **1.32×** | +4.6 | 2e-04 | 21/47 (MIA PaCa-2, NCI-H2030, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here); position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.49×** | +4.5 | 4e-04 | 18/41 (MIA PaCa-2, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.46×** | +4.2 | 0.001 | 13/40 (CFPAC-1, KATO III, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.79×** | +3.6 | 0.015 | 11/42 (SHP-77, PANC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.24×** | +3.6 | 0.015 | 12/47 (MIA PaCa-2, SW480, …) | top dose only |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.37×** | +3.5 | 0.016 | 19/45 (HEC-1-A, SW480, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.34×** | +3.3 | 0.039 | 11/46 (HEC-1-A, BT-474, …) | rises with dose | position effect removed |
| [[Thymol (drug)]] 0.5 µM |  | **1.31×** | +3.1 | 0.056 | 11/44 (NCI-H460, SNU-1, …) | two highest doses |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.37×** | +3.0 | 0.073 | 8/44 (NCI-H460, HS-578T, …) | all doses, stronger at high dose | low cells (technical?); noisy plate (z scaled); position effect removed |
| [[venetoclax (drug)]] 5 µM |  | **1.81×** | +3.0 | 0.073 | 7/40 (HEC-1-A, A498, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **1.31×** | +3.0 | 0.085 | 9/45 (MIA PaCa-2, HEC-1-A, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 2 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13163.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Niclosamide (olamine) (drug)]] 5 µM in 1 line (BT-474 0.146×; ⚠ toxic); [[Doxycycline (monohydrate) (drug)]] 5 µM in 1 line (HOP62 0.0755×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (MIA PaCa-2 0.351×; ⚠ cell-cycle shift, explains ~33% of this change); [[Cysteamine (hydrochloride) (drug)]] 0.5 µM in 1 line (CHP-212 0.0782×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Verteporfin (drug)]] 5 µM |  | **0.699×** | -4.0 | 0.026 | 22/45 (SW 900, A498, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.791×** | -3.9 | 0.026 | 17/44 (MIA PaCa-2, C32, …) | top dose only | position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.729×** | -3.7 | 0.036 | 18/46 (A498, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.746×** | -3.5 | 0.076 | 15/46 (SW480, SW48, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.28 per unit of S-phase module lfc, +0.46 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13163. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 18.7 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.13× (z +17.5) | — |
| [[MIA PaCa-2 (line)]] | alt | 15.2 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.04× (z +13.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.351× (z -8.8) ⚠ cell-cycle shift, explains ~33% of this change |
| [[A-172 (line)]] | wt | 10.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.95× (z +12.8) | — |
| [[BT-474 (line)]] | alt | 23.1 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.79× (z +10.1) | [[Niclosamide (olamine) (drug)]] 5 µM 0.146× (z -9.9) ⚠ toxic |
| [[HEC-1-A (line)]] | alt | 16.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.56× (z +11.5) | — |
| [[HOP62 (line)]] | alt | 4.06 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 15.3× (z +13.8) | [[Doxycycline (monohydrate) (drug)]] 5 µM 0.0755× (z -8.8) |
| [[KATO III (line)]] | alt | 16.7 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.17× (z +10.0) | — |
| [[LoVo (line)]] | wt | 13.8 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.12× (z +9.7) | — |
| [[NCI-H460 (line)]] | wt | 10.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.30× (z +11.0) | — |
| [[SNU-423 (line)]] | alt | 7.94 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.98× (z +11.6) | — |
| [[A549 (line)]] | wt | 7.14 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.23× (z +10.5) | — |
| [[C32 (line)]] | wt | 21.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.02× (z +9.1) | — |
| [[CHP-212 (line)]] | wt | 20.8 | 0 | 1 | — | [[Cysteamine (hydrochloride) (drug)]] 0.5 µM 0.0782× (z -8.5) |
| [[HS-578T (line)]] | alt | 7.49 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.91× (z +13.8) | — |
| [[HT-29 (line)]] | alt | 23.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.68× (z +9.3) | — |
| [[hTERT-HPNE (line)]] | wt | 6.30 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.14× (z +9.4) | — |
| [[J82 (line)]] | alt | 11.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.38× (z +11.6) | — |
| [[NCI-H2347 (line)]] | alt | 5.87 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.02× (z +8.8) | — |
| [[PANC-1 (line)]] | alt | 14.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.76× (z +10.3) | — |
| [[A-427 (line)]] | wt | 10.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 24.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.72 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 6.30 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 7.36 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 9.09 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 9.74 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 5.78 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 24.4 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.88 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 6.59 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 8.87 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 9.24 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 18.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 9.26 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 13.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 8.80 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 41.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 21.9 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 19.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13163), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PBX2]] | +0.74 | +0.67 / +0.65 | both halves | 7e-06 |  |
| [[CLK4]] | +0.72 | +0.64 / +0.67 | both halves | 7e-06 |  |
| [[ZNF480]] | +0.71 | +0.76 / +0.61 | both halves | 7e-06 | same gene group |
| [[ZNF620]] | +0.71 | +0.78 / +0.60 | both halves | 7e-06 | same gene group |
| [[PLD6]] | +0.71 | +0.70 / +0.71 | both halves | 7e-06 |  |
| [[AJUBA]] | +0.70 | +0.74 / +0.62 | both halves | 7e-06 |  |
| [[HNRNPH2]] | +0.70 | +0.77 / +0.60 | both halves | 7e-06 |  |
| [[TEF]] | +0.69 | +0.68 / +0.65 | both halves | 7e-06 |  |
| [[TRIP6]] | +0.69 | +0.72 / +0.59 | both halves | 7e-06 |  |
| [[RTL6]] | +0.69 | +0.72 / +0.62 | both halves | 7e-06 |  |
| [[ZNF764]] | +0.68 | +0.74 / +0.60 | both halves | 7e-06 | same gene group |
| [[METTL18]] | +0.68 | +0.71 / +0.61 | both halves | 7e-06 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RECQL]] | -0.71 | -0.67 / -0.69 | both halves | 7e-06 |  |
| [[MFN1]] | -0.70 | -0.73 / -0.61 | both halves | 7e-06 |  |
| [[PIGF]] | -0.68 | -0.64 / -0.54 | both halves | 1e-05 |  |
| [[SENP5]] | -0.66 | -0.64 / -0.66 | both halves | 7e-06 |  |
| [[SNHG30]] | -0.64 | -0.66 / -0.55 | both halves | 1e-05 |  |
| [[GOLT1B]] | -0.63 | -0.67 / -0.63 | both halves | 7e-06 |  |
| [[TOR1B]] | -0.61 | -0.54 / -0.56 | both halves | 1e-05 |  |
| [[P3H1]] | -0.61 | -0.61 / -0.58 | both halves | 7e-06 |  |
| [[GRB2]] | -0.61 | -0.62 / -0.51 | both halves | 1e-05 |  |
| [[BCAP31]] | -0.61 | -0.67 / -0.53 | both halves | 1e-05 |  |
| [[NME2]] | -0.60 | -0.71 / -0.44 | both halves | 3e-05 |  |
| [[TPTEP2-CSNK1E]] | -0.60 | -0.58 / -0.57 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 0, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DDR1]] | C | DDR1 activity strengthens REPIN1's drug response | lines that do not express DDR1 (3) vs lines expressing it (44) | the lines without DDR1 respond 0.30× as strongly (z diff +2.13); strongest at Homoharringtonine 0.5 µM: 0.81x vs 2.52x (z diff +5.0) | 0.081 | ⚠ few lines (3 vs 47); across organs; co-occurs with SMAD3; also absent: FTH1, LINC00847, IER3; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[MRPS33]] | C | MRPS33's natural level strengthens REPIN1's drug response | MRPS33's natural level across 47 lines (lineage-adjusted; a glimpse) | r +0.63, reverse +0.23; direction not clear | 0.084 | ⚠ tissue can mimic it; precision caveat; direction unclear |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 016]]; 206 genes; this gene is in the **+** arm (projection on the module's main direction 0.687). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-29.2, 10.8); signed map (13.6, -19.0). **Vector** length 92.3, 21.8% of its response variance represented; |z| ≥ 3 in 739 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +10.2 | +19.1 |
|  | [[Harringtonine (drug)]] 5 µM |  | +9.2 | +13.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +7.4 | +9.9 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +5.3 | +9.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.8 | +5.4 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.3 | +3.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +2.8 | +3.3 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.7 | +2.6 |
|  | [[Cobimetinib (drug)]] 0.5 µM |  | +2.4 | +2.6 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | -3.1 | -3.9 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | -2.7 | -3.5 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.7 | -2.5 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.4 | -1.6 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -2.2 | -2.4 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.6 | -1.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.6 | +0.8 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.5 | -0.5 |
|  | [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | -1.3 | -1.8 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.3 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | replication initiator 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q36.1 — chr7:150,368,189-150,374,044 (+) |
| Ensembl biotype | protein_coding |
| Also known as | RIP60, AP4, H_DJ0584D14.12, Zfp464; previously ZNF464 |
| Gene groups (HGNC) | Zinc fingers C2H2-type |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BWE0](https://www.uniprot.org/uniprotkb/Q9BWE0) (DNA-binding protein REPIN1):

> Sequence-specific double-stranded DNA-binding protein. Binds ATT-rich and T-rich DNA sequences and facilitates DNA bending. May regulate the expression of genes involved in cellular fatty acid import, including SCARB1/CD36, and genes involved in lipid droplet formation (By similarity). May regulate the expression of LCN2, and thereby influence iron metabolism and apoptosis-related pathways (By similarity). May regulate the expression of genes involved in glucose transport (By similarity).

**Summary**, from NCBI Gene [29803](https://www.ncbi.nlm.nih.gov/gene/29803):

> Enables sequence-specific DNA binding activity. Predicted to be involved in regulation of fatty acid transport and regulation of transcription by RNA polymerase II. Predicted to act upstream of or within positive regulation of D-glucose import across plasma membrane. Located in nucleoplasm. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:17922](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17922) · Entrez [29803](https://www.ncbi.nlm.nih.gov/gene/29803) · UniProt [Q9BWE0](https://www.uniprot.org/uniprotkb/Q9BWE0) · Ensembl [ENSG00000214022](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000214022)

## Data

Gene col 13163: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13163); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13163, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13163]; `tensor/DDL_lfc|DDL_z.npy` [13163]; `embed/gene_vectors.npy` [13163]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13163 or target_col == 13163). Every well: [[REPIN1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/REPIN1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
