---
symbol: "CDKL2"
type: "gene"
col: 6233
ensembl_id: "ENSG00000138769"
name: "cyclin dependent kinase like 2"
location: "4q21.1"
module: 53
arm: "+"
pooled_cpm: 9.62
n_lines_expressing: 43
n_dd_up: 16
n_dd_down: 2
n_dd_up_clean: 14
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/053"]
generated_by: "tahoemap"
---

# CDKL2

*cyclin dependent kinase like 2* — 4q21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (2 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.76× (z +20.1, q 0e+00, up in 31 of 37 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Digitoxin (drug)]] 0.05 µM: 0.637× (z -4.8, q 7e-04, down in 20 of 39 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 6 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (PANC-1 0.224×, CFPAC-1 0.262×; ⚠ cell-cycle shift, explains ~0% of this change); [[Bortezomib (drug)]] 5 µM in 1 line (PANC-1 0.0581×; ⚠ toxic; cell-cycle shift, explains ~62% of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (NCI-H2030 0.152×; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 5 µM in 1 line (CFPAC-1 0.372×); [[Apalutamide (drug)]] 0.05 µM in 1 line (BT-474 0.0749×); [[Digitoxin (drug)]] 0.05 µM in 1 line (NCI-H1573 0.0487×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DHDH]] (+0.66, fdr 7e-06), [[RUNDC3A-AS1]] (+0.66, fdr 7e-06), [[RSPH9]] (+0.60, fdr 7e-06); moves opposite to [[AAGAB]] (-0.57, fdr 1e-05), [[MTOR]] (-0.52, fdr 2e-05), [[CNOT11]] (-0.51, fdr 2e-05).
> It is in [[Module 053]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TCEA3]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 2 with an alert ⚠. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6233.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.76×** | +20.1 | 0e+00 | 31/37 (A498, NCI-H460, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.47×** | +9.7 | 8e-20 | 27/40 (SW480, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **1.70×** | +8.1 | 1e-13 | 26/39 (SW1417, HT-29, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.10×** | +8.0 | 2e-13 | 26/38 (CFPAC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.08×** | +7.9 | 3e-13 | 26/39 (SW480, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.10×** | +7.7 | 2e-12 | 17/37 (NCI-H460, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.62×** | +7.3 | 2e-11 | 20/37 (SW480, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.56×** | +6.8 | 7e-10 | 19/40 (J82, A498, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~18% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.81×** | +6.4 | 1e-08 | 23/39 (SW480, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.76×** | +6.1 | 7e-08 | 9/28 (LoVo, Hs 766T, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[PF-06260933 (drug)]] 5 µM |  | **2.78×** | +5.8 | 4e-07 | 16/35 (NCI-H460, BT-474, …) | top dose only | noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM |  | **1.68×** | +5.6 | 1e-06 | 22/39 (SW480, SW1417, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.68×** | +5.4 | 3e-06 | 2/12 (A498, RPMI-7951) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 0.5 µM |  | **1.45×** | +4.0 | 0.002 | 13/38 (J82, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Filgotinib (drug)]] 5 µM |  | **1.35×** | +3.2 | 0.050 | 10/40 (A498, HepG2/C3A, …) | top dose only |  |
| [[Demeclocycline (drug)]] 0.05 µM |  | **1.39×** | +3.0 | 0.100 | 2/39 (PANC-1, NCI-H661) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 6233.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 6 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (PANC-1 0.224×, CFPAC-1 0.262×; ⚠ cell-cycle shift, explains ~0% of this change); [[Bortezomib (drug)]] 5 µM in 1 line (PANC-1 0.0581×; ⚠ toxic; cell-cycle shift, explains ~62% of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (NCI-H2030 0.152×; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 5 µM in 1 line (CFPAC-1 0.372×); [[Apalutamide (drug)]] 0.05 µM in 1 line (BT-474 0.0749×); [[Digitoxin (drug)]] 0.05 µM in 1 line (NCI-H1573 0.0487×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.05 µM |  | **0.637×** | -4.8 | 7e-04 | 20/39 (NCI-H1573, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~11% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.664×** | -4.4 | 0.003 | 21/39 (BT-474, NCI-H1792, …) | inconsistent across doses | cell-cycle shift (explains ~13% here) |
| [[Benztropine (mesylate) (drug)]] 0.5 µM |  | 0.745× | -3.2 | 0.30 | 3/39 (NCI-H661, C32, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.04 per unit of S-phase module lfc, -0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6233. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 16.6 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.224× (z -12.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW480 (line)]] | alt | 5.56 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.29× (z +9.2) | — |
| [[BT-474 (line)]] | alt | 10.5 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.18× (z +10.0) | [[Apalutamide (drug)]] 0.05 µM 0.0749× (z -9.4) |
| [[CFPAC-1 (line)]] | alt | 22.2 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.372× (z -9.6) |
| [[NCI-H1792 (line)]] | alt | 12.2 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.42× (z +8.5) | [[Digitoxin (drug)]] 5 µM 0.143× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~96% of this change |
| [[NCI-H460 (line)]] | wt | 3.54 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.36× (z +10.8) | — |
| [[A498 (line)]] | wt | 3.84 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.66× (z +11.7) | — |
| [[HepG2_C3A (line)]] | wt | 2.98 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 15.3× (z +8.5) | — |
| [[HOP62 (line)]] | alt | 6.36 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.03× (z +8.8) | — |
| [[HS-578T (line)]] | alt | 3.41 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 12.8× (z +8.9) | — |
| [[NCI-H1573 (line)]] | alt | 5.09 | 0 | 1 | — | [[Digitoxin (drug)]] 0.05 µM 0.0487× (z -9.4) |
| [[NCI-H2030 (line)]] | alt | 14.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.152× (z -10.4) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 43.7 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.366× (z -9.4) ⚠ toxic; cell-cycle shift, explains ~23% of this change |
| [[A-172 (line)]] | wt | 1.56 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 26.8 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 10.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 6.11 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.10 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 4.35 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.73 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 11.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.30 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 9.39 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.86 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 5.43 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 7.01 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 7.83 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 5.50 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 5.66 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.42 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.86 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 7.96 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 8.36 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 8.43 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.31 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.44 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 2.13 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 4.49 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.31 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 6.03 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.93 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6233), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DHDH]] | +0.66 | +0.66 / +0.58 | both halves | 7e-06 |  |
| [[RUNDC3A-AS1]] | +0.66 | +0.60 / +0.67 | both halves | 7e-06 |  |
| [[RSPH9]] | +0.60 | +0.61 / +0.61 | both halves | 7e-06 |  |
| [[WDR47]] | +0.60 | +0.64 / +0.53 | both halves | 1e-05 |  |
| [[CASKIN1]] | +0.59 | +0.53 / +0.52 | both halves | 1e-05 |  |
| [[LDHC]] | +0.58 | +0.63 / +0.56 | both halves | 1e-05 |  |
| [[APC2]] | +0.58 | +0.58 / +0.55 | both halves | 1e-05 |  |
| [[CCDC181]] | +0.58 | +0.57 / +0.62 | both halves | 9e-06 |  |
| [[MIR9-1HG]] | +0.58 | +0.55 / +0.59 | both halves | 1e-05 |  |
| [[GRAMD2A]] | +0.57 | +0.59 / +0.53 | both halves | 1e-05 |  |
| [[CAPN12]] | +0.57 | +0.43 / +0.47 | both halves | 3e-05 |  |
| [[ADORA1]] | +0.57 | +0.51 / +0.57 | both halves | 1e-05 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AAGAB]] | -0.57 | -0.55 / -0.52 | both halves | 1e-05 |  |
| [[MTOR]] | -0.52 | -0.52 / -0.47 | both halves | 2e-05 |  |
| [[CNOT11]] | -0.51 | -0.49 / -0.48 | both halves | 2e-05 |  |
| [[ANAPC7]] | -0.49 | -0.39 / -0.45 | both halves | 6e-05 |  |
| [[TERF2]] | -0.49 | -0.41 / -0.52 | both halves | 4e-05 |  |
| [[ATR]] | -0.49 | -0.44 / -0.44 | both halves | 3e-05 |  |
| [[PPIL1]] | -0.49 | -0.48 / -0.43 | both halves | 3e-05 |  |
| [[TMEM168]] | -0.48 | -0.48 / -0.43 | both halves | 4e-05 |  |
| [[LEMD2]] | -0.47 | -0.37 / -0.47 | both halves | 8e-05 |  |
| [[DNAJC11]] | -0.47 | -0.30 / -0.56 | both halves | 2e-04 |  |
| [[RFT1]] | -0.47 | -0.52 / -0.38 | both halves | 7e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TCEA3]] | B | TCEA3 activity raises CDKL2's level | lines that do not express TCEA3 (14) vs lines expressing it (36) | 1.59× lower at baseline in the lines without TCEA3 | 0.047 | ⚠ within organs, on part of the lines; also absent: ZNF43, ENSG00000267383, ZNF681; maybe low, not absent |
| [[PTPN6]] | B | PTPN6 activity raises CDKL2's level | lines that do not express PTPN6 (8) vs lines expressing it (42) | 1.66× lower at baseline in the lines without PTPN6 | 0.047 | ⚠ within organs, on part of the lines; also absent: LMTK3, ENSG00000257252; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 053]]; 88 genes; every member is in the + arm (projection on the module's main direction 0.562). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (41.2, -19.1); signed map (13.1, 16.4). **Vector** length 81.4, 16.0% of its response variance represented; |z| ≥ 3 in 1,104 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +6.1 | +8.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.3 | +8.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.3 | +20.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.8 | +5.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.4 | +6.1 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +2.3 | +2.6 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.2 | +5.8 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +2.0 | +1.5 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.9 | +3.2 |
| fall | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -3.2 | +1.5 |
|  | [[Digitoxin (drug)]] 0.05 µM |  | -3.1 | -4.8 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.1 | -2.5 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -3.0 | -4.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.7 | -2.4 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.4 | -1.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.2 | -1.7 |
|  | [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | -1.8 | -2.3 |
|  | [[Berbamine (drug)]] 0.05 µM |  | -1.8 | -2.7 |
|  | [[Pralsetinib (drug)]] 5 µM |  | -1.7 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | cyclin dependent kinase like 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q21.1 — chr4:75,576,496-75,630,716 (-) |
| Ensembl biotype | protein_coding |
| Also known as | P56, KKIAMRE |
| Gene groups (HGNC) | Cyclin dependent kinase like family |
| Matched by | ensembl_id |

UniProt [Q92772](https://www.uniprot.org/uniprotkb/Q92772) carries no function annotation.

**Summary**, from NCBI Gene [8999](https://www.ncbi.nlm.nih.gov/gene/8999):

> This gene product is a member of a large family of CDC2-related serine/threonine protein kinases. It accumulates primarily in the cytoplasm, with lower levels in the nucleus. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:1782](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1782) · Entrez [8999](https://www.ncbi.nlm.nih.gov/gene/8999) · UniProt [Q92772](https://www.uniprot.org/uniprotkb/Q92772) · Ensembl [ENSG00000138769](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000138769)

## Data

Gene col 6233: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6233); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6233, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6233]; `tensor/DDL_lfc|DDL_z.npy` [6233]; `embed/gene_vectors.npy` [6233]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6233 or target_col == 6233). Every well: [[CDKL2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CDKL2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
