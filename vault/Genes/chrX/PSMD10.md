---
symbol: "PSMD10"
type: "gene"
col: 2176
ensembl_id: "ENSG00000101843"
name: "proteasome 26S subunit, non-ATPase 10"
location: "Xq22.3"
module: 74
arm: "+"
pooled_cpm: 26.91
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 0
n_dd_up_clean: 1
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 2
tags: ["gene", "module/074"]
generated_by: "tahoemap"
---

# PSMD10

*proteasome 26S subunit, non-ATPase 10* — Xq22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.80× (z +11.3, q 4e-27, up in 39 of 43 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 1.38× (z +3.6, q 0.035, up in 21 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 9 lines (PANC-1 3.84×, MIA PaCa-2 5.53×, HOP62 4.10×, SW480 3.28×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change); [[Dinaciclib (drug)]] 5 µM in 6 lines (NCI-H460 4.34×, J82 4.72×, A549 5.17×, PANC-1 3.09×, …; ⚠ toxic; transcription drop).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[IK]] (+0.65, fdr 7e-06), [[TRIM23]] (+0.65, fdr 7e-06), [[MTIF3]] (+0.64, fdr 7e-06); moves opposite to [[UTP4]] (-0.54, fdr 3e-05), [[MRPS25]] (-0.53, fdr 4e-05), [[CPNE7]] (-0.53, fdr 2e-05).
> It is in [[Module 074]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 2 go from it, the strongest it → cells under [[Bendamustine (drug)]] 0.5 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 6 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2176.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 9 lines (PANC-1 3.84×, MIA PaCa-2 5.53×, HOP62 4.10×, SW480 3.28×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change); [[Dinaciclib (drug)]] 5 µM in 6 lines (NCI-H460 4.34×, J82 4.72×, A549 5.17×, PANC-1 3.09×, …; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **2.80×** | +11.3 | 4e-27 | 39/43 (PANC-1, MIA PaCa-2, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.75×** | +10.7 | 2e-24 | 31/33 (NCI-H460, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.55×** | +4.8 | 3e-04 | 26/48 (HOP62, NCI-H1573, …) | all doses, flat |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~68% of this change | **1.47×** | +4.2 | 0.003 | 27/45 (Panc 03.27, NCI-H2030, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | **1.46×** | +3.8 | 0.014 | 21/39 (SNU-423, NCI-H2347, …) | all doses, stronger at high dose | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.38×** | +3.6 | 0.035 | 21/48 (HEC-1-A, BT-474, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 1.32× | +3.1 | 0.14 | 21/48 (H4, RKO, …) | inconsistent across doses |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~69% of this change | 1.23× | +3.1 | 0.14 | 20/48 (NCI-H460, NCI-H1573, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 2 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 2176.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.731× | -3.2 | 0.55 | 20/48 (Hs 766T, NCI-H460, …) | inconsistent across doses | position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.918× | -3.1 | 0.55 | 1/48 (HepG2/C3A) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.02 per unit of S-phase module lfc, +0.55 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2176. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 42.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.07× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | — |
| [[A549 (line)]] | wt | 27.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.17× (z +10.1) ⚠ toxic; transcription drop | — |
| [[Hs 766T (line)]] | wt | 39.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.54× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 24.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.53× (z +10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | — |
| [[PANC-1 (line)]] | alt | 46.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.84× (z +11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | — |
| [[A-172 (line)]] | wt | 15.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.44× (z +9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | — |
| [[CFPAC-1 (line)]] | alt | 20.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.57× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | — |
| [[HOP62 (line)]] | alt | 28.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.10× (z +10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | — |
| [[J82 (line)]] | alt | 26.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.72× (z +10.5) ⚠ toxic; transcription drop | — |
| [[NCI-H2030 (line)]] | alt | 33.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.50× (z +9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | — |
| [[NCI-H23 (line)]] | alt | 34.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.80× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | — |
| [[NCI-H460 (line)]] | wt | 27.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.34× (z +11.2) ⚠ toxic; transcription drop | — |
| [[SNU-423 (line)]] | alt | 38.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.83× (z +9.1) ⚠ toxic; transcription drop | — |
| [[SW480 (line)]] | alt | 35.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.28× (z +10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | — |
| [[A-427 (line)]] | wt | 33.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 22.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 18.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 16.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 29.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 15.9 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 22.0 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 24.8 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 20.0 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 44.6 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 15.0 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 17.2 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 21.9 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 27.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 22.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 27.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 24.5 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 22.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 19.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 19.2 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 34.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 13.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 29.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 19.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 28.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 17.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2176), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IK]] | +0.65 | +0.59 / +0.66 | both halves | 7e-06 |  |
| [[TRIM23]] | +0.65 | +0.67 / +0.64 | both halves | 7e-06 |  |
| [[MTIF3]] | +0.64 | +0.64 / +0.59 | both halves | 7e-06 |  |
| [[ASB8]] | +0.60 | +0.61 / +0.55 | both halves | 1e-05 | same gene group |
| [[AKAP9]] | +0.59 | +0.49 / +0.65 | both halves | 1e-05 |  |
| [[TBC1D23]] | +0.57 | +0.48 / +0.52 | both halves | 2e-05 |  |
| [[CETN3]] | +0.57 | +0.49 / +0.59 | both halves | 1e-05 |  |
| [[CIR1]] | +0.56 | +0.55 / +0.58 | both halves | 1e-05 |  |
| [[NDUFA8]] | +0.56 | +0.59 / +0.48 | both halves | 2e-05 |  |
| [[GOLPH3L]] | +0.56 | +0.44 / +0.53 | both halves | 3e-05 |  |
| [[FRA10AC1]] | +0.56 | +0.55 / +0.50 | both halves | 1e-05 |  |
| [[ERCC5]] | +0.56 | +0.60 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UTP4]] | -0.54 | -0.44 / -0.55 | both halves | 3e-05 |  |
| [[MRPS25]] | -0.53 | -0.41 / -0.51 | both halves | 4e-05 |  |
| [[CPNE7]] | -0.53 | -0.46 / -0.58 | both halves | 2e-05 |  |
| [[SEH1L]] | -0.52 | -0.49 / -0.55 | both halves | 1e-05 |  |
| [[SMG1P3]] | -0.51 | -0.50 / -0.54 | both halves | 1e-05 |  |
| [[GATAD2A]] | -0.49 | -0.54 / -0.45 | both halves | 3e-05 |  |
| [[NBL1]] | -0.48 | -0.45 / -0.48 | both halves | 3e-05 |  |
| [[GLB1L2]] | -0.48 | -0.52 / -0.57 | both halves | 1e-05 |  |
| [[GART]] | -0.48 | -0.45 / -0.49 | both halves | 3e-05 |  |
| [[CLN6]] | -0.48 | -0.50 / -0.43 | both halves | 3e-05 |  |
| [[E2F3]] | -0.47 | -0.38 / -0.42 | both halves | 7e-05 |  |
| [[CTPS1]] | -0.46 | -0.34 / -0.47 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 0, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Bendamustine (drug)]] 0.5 µM | C | PSMD10's natural level lowers the cells' numbers under Bendamustine 0.5 µM (makes them more sensitive) | PSMD10's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.66 | 0.360 over the table, 0.040 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |
| cells under [[Citalopram (hydrobromide) (drug)]] 0.05 µM | C | PSMD10's natural level raises the cells' numbers under Citalopram (hydrobromide) 0.05 µM (protects the cells) | PSMD10's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.65 | 0.365 over the table, 0.073 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

## Where it sits

- **Module**: [[Module 074]]; 63 genes; every member is in the + arm (projection on the module's main direction 0.589). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-34.2, -28.2); signed map (-15.3, -5.6). **Vector** length 59.7, 12.0% of its response variance represented; |z| ≥ 3 in 516 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | +2.4 | +4.8 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | +2.2 | +2.6 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +2.2 | +2.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +1.8 | +1.4 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +1.7 | +2.8 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +1.7 | +1.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.6 | +3.1 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.3 | +0.3 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | +1.3 | +0.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.2 | -0.7 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.8 | -3.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.5 | +1.4 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -2.2 | +0.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | -2.2 | +3.8 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.9 | -2.1 |
|  | [[EX229 (drug)]] 5 µM |  | -1.8 | -1.3 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -1.8 | -0.4 |
|  | [[TAK-733 (drug)]] 5 µM |  | -1.5 | -0.2 |
|  | [[venetoclax (drug)]] 5 µM |  | -1.3 | +0.1 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | -1.3 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | proteasome 26S subunit, non-ATPase 10 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xq22.3 — chrX:108,084,207-108,091,549 (-) |
| Ensembl biotype | protein_coding |
| Also known as | p28 |
| Gene groups (HGNC) | Ankyrin repeat domain containing; Proteasome |
| Reactome | 1 pathways, smallest: Proteasome assembly |
| Matched by | ensembl_id |

**Function**, from UniProt [O75832](https://www.uniprot.org/uniprotkb/O75832) (26S proteasome non-ATPase regulatory subunit 10):

> Acts as a chaperone during the assembly of the 26S proteasome, specifically of the PA700/19S regulatory complex (RC). In the initial step of the base subcomplex assembly is part of an intermediate PSMD10:PSMC4:PSMC5:PAAF1 module which probably assembles with a PSMD5:PSMC2:PSMC1:PSMD2 module. Independently of the proteasome, regulates EGF-induced AKT activation through inhibition of the RHOA/ROCK/PTEN pathway, leading to prolonged AKT activation. Plays an important role in RAS-induced …

**Summary**, from NCBI Gene [5716](https://www.ncbi.nlm.nih.gov/gene/5716):

> This gene encodes a subunit of the PA700/19S complex, which is the regulatory component of the 26S proteasome. The 26S proteosome complex is required for ubiquitin-dependent protein degradation. This protein is a non-ATPase subunit that may be involved in protein-protein interactions. Aberrant expression of this gene may paly a role in tumorigenesis. Two transcripts encoding different isoforms have been described. Pseudogenes have been identified on chromosomes 3 and 20.[provided by RefSeq, Mar …

**Accessions** — [HGNC:9555](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9555) · Entrez [5716](https://www.ncbi.nlm.nih.gov/gene/5716) · UniProt [O75832](https://www.uniprot.org/uniprotkb/O75832) · Ensembl [ENSG00000101843](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000101843)

## Data

Gene col 2176: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2176); `tables/drug_effects.parquet` (10 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2176, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2176]; `tensor/DDL_lfc|DDL_z.npy` [2176]; `embed/gene_vectors.npy` [2176]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2176 or target_col == 2176). Every well: [[PSMD10 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PSMD10.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
