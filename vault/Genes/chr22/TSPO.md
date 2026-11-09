---
symbol: "TSPO"
type: "gene"
col: 1919
ensembl_id: "ENSG00000100300"
name: "translocator protein"
location: "22q13.2"
module: 3
arm: "+"
pooled_cpm: 33.53
n_lines_expressing: 48
n_dd_up: 5
n_dd_down: 9
n_dd_up_clean: 0
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/003"]
generated_by: "tahoemap"
---

# TSPO

*translocator protein* — 22q13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.53× (z +9.6, q 6e-19, up in 38 of 40 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 1 line (C32 8.14×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 1 line (HS-578T 3.81×; ⚠ toxic; transcription drop).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.321× (z -13.9, q 3e-41, down in 44 of 45 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NME2]] (+0.67, fdr 1e-05), [[GNB2]] (+0.60, fdr 1e-05), [[LAMTOR2]] (+0.60, fdr 1e-05); moves opposite to [[ZSCAN29]] (-0.57, fdr 2e-04), [[ZNF772]] (-0.56, fdr 4e-05), [[ZNF502]] (-0.56, fdr 6e-05).
> It sits in the **+** arm of [[Module 003]] (mRNA 3'-end processing).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[MSLN]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 5 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1919.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 1 line (C32 8.14×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 1 line (HS-578T 3.81×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.53×** | +9.6 | 6e-19 | 38/40 (HS-578T, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.71×** | +7.7 | 6e-12 | 30/32 (C32, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.05×** | +5.8 | 1e-06 | 31/35 (HS-578T, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift; position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~36% of this change | **1.88×** | +5.5 | 6e-06 | 34/43 (SW1417, Panc 03.27, …) | inconsistent across doses | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.57×** | +3.5 | 0.059 | 23/44 (NCI-H2030, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, none with an alert. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 1919.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.321×** | -13.9 | 3e-41 | 44/45 (RKO, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.326×** | -9.7 | 9e-20 | 42/45 (MIA PaCa-2, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **0.557×** | -5.0 | 8e-05 | 34/46 (A-172, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.543×** | -4.7 | 5e-04 | 32/45 (RKO, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **0.603×** | -4.4 | 0.002 | 32/46 (RKO, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.399×** | -4.2 | 0.003 | 30/44 (HCT15, NCI-H460, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.623×** | -4.1 | 0.004 | 28/46 (A-172, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.666×** | -3.5 | 0.034 | 25/46 (HEC-1-A, SW48, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.678×** | -3.2 | 0.100 | 24/45 (LS 180, HEC-1-A, …) | inconsistent across doses |  |
| [[GSK1059615 (drug)]] 5 µM |  | 0.507× | -3.1 | 0.12 | 27/44 (LS 180, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Sapanisertib (drug)]] 5 µM |  | 0.514× | -3.0 | 0.14 | 21/46 (AsPC-1, SNU-1, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.09 per unit of S-phase module lfc, +0.52 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1919. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HS-578T (line)]] | alt | 71.7 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 3.81× (z +8.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.335× (z -11.0) |
| [[A498 (line)]] | wt | 67.3 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.324× (z -12.0) |
| [[AsPC-1 (line)]] | alt | 41.5 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.185× (z -16.0) |
| [[HEC-1-A (line)]] | alt | 39.5 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.352× (z -10.3) |
| [[KATO III (line)]] | alt | 74.3 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.264× (z -13.6) |
| [[LS 180 (line)]] | wt | 58.4 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.248× (z -12.8) |
| [[MIA PaCa-2 (line)]] | alt | 30.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0590× (z -16.1) |
| [[NCI-H1573 (line)]] | alt | 19.5 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.153× (z -9.8) |
| [[RKO (line)]] | wt | 41.5 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.112× (z -18.1) |
| [[SW480 (line)]] | alt | 26.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.228× (z -14.1) |
| [[A-172 (line)]] | wt | 34.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.364× (z -9.9) |
| [[A549 (line)]] | wt | 18.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.266× (z -9.6) |
| [[BT-474 (line)]] | alt | 20.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.202× (z -11.3) |
| [[C32 (line)]] | wt | 26.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 8.14× (z +10.1) ⚠ toxic; transcription drop | — |
| [[CFPAC-1 (line)]] | alt | 56.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.396× (z -9.0) |
| [[CHP-212 (line)]] | wt | 29.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.144× (z -9.4) |
| [[COLO 205 (line)]] | alt | 27.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.138× (z -13.6) |
| [[H4 (line)]] | wt | 33.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.129× (z -13.9) |
| [[HOP62 (line)]] | alt | 28.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.277× (z -11.9) |
| [[Hs 766T (line)]] | wt | 77.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.269× (z -12.5) |
| [[HT-29 (line)]] | alt | 36.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.231× (z -12.7) |
| [[J82 (line)]] | alt | 26.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.299× (z -10.2) |
| [[LoVo (line)]] | wt | 30.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.214× (z -13.8) |
| [[NCI-H2030 (line)]] | alt | 41.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.136× (z -17.9) |
| [[NCI-H23 (line)]] | alt | 23.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.211× (z -11.8) |
| [[NCI-H2347 (line)]] | alt | 48.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.366× (z -10.5) |
| [[NCI-H460 (line)]] | wt | 21.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.334× (z -9.5) |
| [[PANC-1 (line)]] | alt | 29.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.371× (z -9.2) |
| [[SHP-77 (line)]] | alt | 13.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.249× (z -8.8) |
| [[SW1417 (line)]] | alt | 16.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.331× (z -8.5) |
| [[A-427 (line)]] | wt | 22.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 20.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 30.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 6.54 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 26.8 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 18.5 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 22.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 21.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 26.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 27.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 27.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 27.9 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 7.22 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 24.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 21.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 47.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1919), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*62 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NME2]] | +0.67 | +0.73 / +0.52 | both halves | 1e-05 |  |
| [[GNB2]] | +0.60 | +0.62 / +0.57 | both halves | 1e-05 |  |
| [[LAMTOR2]] | +0.60 | +0.49 / +0.57 | both halves | 1e-05 |  |
| [[APRT]] | +0.60 | +0.54 / +0.55 | both halves | 1e-05 |  |
| [[NHP2]] | +0.59 | +0.64 / +0.48 | both halves | 2e-05 |  |
| [[PRDX4]] | +0.58 | +0.63 / +0.50 | both halves | 1e-05 |  |
| [[TRAPPC1]] | +0.57 | +0.62 / +0.52 | both halves | 1e-05 |  |
| [[RAP1A]] | +0.57 | +0.57 / +0.29 | both halves | 3e-04 |  |
| [[HIGD2A]] | +0.57 | +0.61 / +0.57 | both halves | 8e-06 |  |
| [[PRELID1]] | +0.57 | +0.50 / +0.55 | both halves | 1e-05 |  |
| [[MIR4458HG]] | +0.55 | +0.46 / +0.59 | both halves | 3e-05 |  |
| [[TCTN3]] | +0.55 | +0.45 / +0.45 | both halves | 3e-05 |  |

## Genes that move opposite

*38 of its nearest partners move opposite, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZSCAN29]] | -0.57 | -0.66 / -0.29 | both halves | 2e-04 |  |
| [[ZNF772]] | -0.56 | -0.53 / -0.41 | both halves | 4e-05 |  |
| [[ZNF502]] | -0.56 | -0.61 / -0.38 | both halves | 6e-05 |  |
| [[C22orf46]] | -0.55 | -0.53 / -0.39 | both halves | 5e-05 |  |
| [[CSTF2T]] | -0.55 | -0.56 / -0.46 | both halves | 3e-05 |  |
| [[USP16]] | -0.54 | -0.54 / -0.46 | both halves | 2e-05 |  |
| [[LARP7]] | -0.54 | -0.58 / -0.31 | both halves | 2e-04 |  |
| [[MIS12]] | -0.54 | -0.59 / -0.39 | both halves | 5e-05 |  |
| [[GRIPAP1]] | -0.54 | -0.62 / -0.39 | both halves | 5e-05 |  |
| [[DEDD]] | -0.53 | -0.53 / -0.39 | both halves | 6e-05 |  |
| [[ZNF780A]] | -0.53 | -0.62 / -0.45 | both halves | 3e-05 |  |
| [[ZNF554]] | -0.53 | -0.61 / -0.40 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MSLN]] | B | MSLN activity raises TSPO's level | lines that do not express MSLN (33) vs lines expressing it (17) | 1.45× lower at baseline in the lines without MSLN | 0.022 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: C4BPB, EPS8L3, EDAR |
| [[HDAC6]] | B | HDAC6 activity raises TSPO's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 003]] — mRNA 3'-end processing; 246 genes; this gene is in the **+** arm (projection on the module's main direction 0.385). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-50.7, -20.6); signed map (-36.4, 11.8). **Vector** length 56.7, 14.2% of its response variance represented; |z| ≥ 3 in 686 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +2.5 | -0.6 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +2.1 | +1.4 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +2.0 | +2.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | +1.8 | -2.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +1.7 | -0.9 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +1.2 | +1.5 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +1.1 | +1.8 |
|  | [[Budesonide (drug)]] 0.05 µM |  | +0.9 | +1.3 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +0.9 | +1.2 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | +0.8 | +0.6 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -4.3 | -9.7 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -3.5 | -13.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.9 | -2.2 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.7 | -1.4 |
|  | [[Harringtonine (drug)]] 5 µM |  | -2.4 | -4.7 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -1.8 | -0.2 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.7 | -0.4 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.3 | -0.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.2 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | translocator protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q13.2 — chr22:43,151,547-43,163,242 (+) |
| Ensembl biotype | protein_coding |
| Also known as | PBR, MBR, PKBS, mDRC, DBI, IBP, pk18, TSPO1; previously BZRP |
| Gene groups (HGNC) | Translocator protein family |
| Hallmark sets | PEROXISOME, APOPTOSIS |
| Reactome | 4 pathways, smallest: Pregnenolone biosynthesis; Metabolism of steroid hormones; Metabolism of steroids |
| Matched by | ensembl_id |

UniProt [B1AH88](https://www.uniprot.org/uniprotkb/B1AH88) carries no function annotation.

**Summary**, from NCBI Gene [706](https://www.ncbi.nlm.nih.gov/gene/706):

> Present mainly in the mitochondrial compartment of peripheral tissues, the protein encoded by this gene interacts with some benzodiazepines and has different affinities than its endogenous counterpart. The protein is a key factor in the flow of cholesterol into mitochondria to permit the initiation of steroid hormone synthesis. Alternatively spliced transcript variants have been reported; one of the variants lacks an internal exon and is considered non-coding, and the other variants encode the …

**Accessions** — [HGNC:1158](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1158) · Entrez [706](https://www.ncbi.nlm.nih.gov/gene/706) · UniProt [B1AH88](https://www.uniprot.org/uniprotkb/B1AH88) · Ensembl [ENSG00000100300](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000100300)

## Data

Gene col 1919: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1919); `tables/drug_effects.parquet` (16 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1919, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1919]; `tensor/DDL_lfc|DDL_z.npy` [1919]; `embed/gene_vectors.npy` [1919]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1919 or target_col == 1919). Every well: [[TSPO — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TSPO.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
