---
symbol: "OCRL"
type: "gene"
col: 4321
ensembl_id: "ENSG00000122126"
name: "OCRL inositol polyphosphate-5-phosphatase"
location: "Xq26.1"
module: 25
arm: "+"
pooled_cpm: 28.11
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 5
n_dd_up_clean: 1
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 0
direction_downstream: 2
tags: ["gene", "module/025"]
generated_by: "tahoemap"
---

# OCRL

*OCRL inositol polyphosphate-5-phosphatase* — Xq26.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.00× (z +8.6, q 7e-15, up in 28 of 35 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Homoharringtonine (drug)]] 5 µM: 1.27× (z +4.3, q 0.003, up in 23 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 1 line (SW480 2.12×).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (1 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.410× (z -16.4, q 0e+00, down in 42 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LIN7C]] (+0.77, fdr 7e-06), [[GMFB]] (+0.77, fdr 7e-06), [[PRELID3B]] (+0.74, fdr 7e-06); moves opposite to [[SMIM27]] (-0.66, fdr 1e-04), [[SNHG9]] (-0.66, fdr 1e-04), [[MIA]] (-0.66, fdr 3e-05).
> It sits in the **+** arm of [[Module 025]] (oxidative phosphorylation).
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 2 go from it, the strongest it → [[PRPS1]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 3 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4321.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 1 line (SW480 2.12×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.00×** | +8.6 | 7e-15 | 28/35 (LoVo, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.51×** | +5.3 | 4e-05 | 27/44 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.27×** | +4.3 | 0.003 | 23/47 (SW480, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.39×** | +4.2 | 0.004 | 23/47 (MIA PaCa-2, SNU-423, …) | inconsistent across doses |  |
| [[Folic acid (drug)]] 5 µM |  | 1.20× | +3.3 | 0.11 | 16/48 (MIA PaCa-2, SW 900, …) | top dose only | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 2 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4321.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.410×** | -16.4 | 0e+00 | 42/47 (SW480, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **0.713×** | -4.4 | 0.003 | 25/46 (LS 180, SNU-1, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.710×** | -4.3 | 0.003 | 27/46 (SW480, C32, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Sodium Salicylate (drug)]] 5 µM |  | **0.831×** | -3.4 | 0.081 | 20/48 (MIA PaCa-2, LOX-IMVI, …) | rises with dose |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.611×** | -3.4 | 0.088 | 16/46 (A498, LoVo, …) | rises with dose | noisy plate (z scaled) |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | 0.787× | -3.1 | 0.16 | 17/47 (HT-29, RKO, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | 0.786× | -3.0 | 0.19 | 17/44 (RKO, RPMI-7951, …) | top dose only | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.04 per unit of S-phase module lfc, -0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4321. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 31.5 | 1 | 2 | [[Homoharringtonine (drug)]] 5 µM 2.12× (z +9.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.267× (z -17.5) |
| [[NCI-H23 (line)]] | alt | 40.8 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.244× (z -15.1) |
| [[RKO (line)]] | wt | 35.3 | 0 | 2 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.160× (z -12.3) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.386× (z -9.4) |
| [[A549 (line)]] | wt | 35.0 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.411× (z -10.6) |
| [[C32 (line)]] | wt | 18.9 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.185× (z -8.7) |
| [[HEC-1-A (line)]] | alt | 27.5 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.461× (z -9.0) |
| [[HOP62 (line)]] | alt | 26.3 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.375× (z -10.3) |
| [[Hs 766T (line)]] | wt | 32.6 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.390× (z -9.0) |
| [[HS-578T (line)]] | alt | 16.0 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.333× (z -9.6) |
| [[HT-29 (line)]] | alt | 28.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.327× (z -12.5) |
| [[hTERT-HPNE (line)]] | wt | 19.6 | 0 | 1 | — | [[Thymol (drug)]] 0.5 µM 0.0886× (z -12.9) |
| [[J82 (line)]] | alt | 38.7 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.457× (z -9.3) |
| [[KATO III (line)]] | alt | 26.7 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.290× (z -13.0) |
| [[LoVo (line)]] | wt | 19.8 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.343× (z -11.8) |
| [[LOX-IMVI (line)]] | wt | 29.5 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.376× (z -10.6) |
| [[LS 180 (line)]] | wt | 22.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.356× (z -9.6) |
| [[MIA PaCa-2 (line)]] | alt | 40.9 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.299× (z -13.7) |
| [[NCI-H1573 (line)]] | alt | 18.7 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.251× (z -12.1) |
| [[NCI-H1792 (line)]] | alt | 17.8 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.333× (z -9.3) |
| [[NCI-H2030 (line)]] | alt | 28.6 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.340× (z -11.8) |
| [[NCI-H460 (line)]] | wt | 43.7 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.316× (z -14.4) |
| [[Panc 03.27 (line)]] | alt | 28.8 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.359× (z -10.3) |
| [[PANC-1 (line)]] | alt | 42.4 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.391× (z -12.6) |
| [[RPMI-7951 (line)]] | alt | 20.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.141× (z -15.0) |
| [[SK-MEL-2 (line)]] | alt | 32.6 | 0 | 1 (1 ⚠) | — | [[AZD2858 (drug)]] 0.5 µM 0.0904× (z -10.7) ⚠ toxic |
| [[SW1417 (line)]] | alt | 28.8 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.395× (z -9.1) |
| [[A-172 (line)]] | wt | 16.0 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 40.6 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 29.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 31.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 18.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 28.1 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 18.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 22.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 19.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 18.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 19.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 24.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 22.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 35.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 25.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 31.4 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 33.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 21.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 24.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4321), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*64 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LIN7C]] | +0.77 | +0.59 / +0.85 | both halves | 7e-06 |  |
| [[GMFB]] | +0.77 | +0.62 / +0.82 | both halves | 7e-06 |  |
| [[PRELID3B]] | +0.74 | +0.61 / +0.81 | both halves | 7e-06 |  |
| [[DLD]] | +0.73 | +0.59 / +0.78 | both halves | 7e-06 |  |
| [[NONO]] | +0.72 | +0.47 / +0.79 | both halves | 2e-05 |  |
| [[TEX261]] | +0.72 | +0.55 / +0.72 | both halves | 1e-05 |  |
| [[PTPN11]] | +0.70 | +0.63 / +0.72 | both halves | 7e-06 |  |
| [[PIGO]] | +0.70 | +0.53 / +0.73 | both halves | 1e-05 |  |
| [[SGPL1]] | +0.70 | +0.50 / +0.73 | both halves | 1e-05 |  |
| [[API5]] | +0.68 | +0.37 / +0.77 | both halves | 9e-05 |  |
| [[IPO8]] | +0.68 | +0.49 / +0.76 | both halves | 1e-05 |  |
| [[ZDHHC21]] | +0.68 | +0.43 / +0.73 | both halves | 3e-05 |  |

## Genes that move opposite

*36 of its nearest partners move opposite, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SMIM27]] | -0.66 | -0.35 / -0.70 | both halves | 1e-04 |  |
| [[SNHG9]] | -0.66 | -0.33 / -0.72 | both halves | 1e-04 |  |
| [[MIA]] | -0.66 | -0.46 / -0.68 | both halves | 3e-05 |  |
| [[NDUFA2]] | -0.65 | -0.44 / -0.72 | both halves | 3e-05 |  |
| [[LINC00685]] | -0.64 | -0.37 / -0.72 | both halves | 8e-05 |  |
| [[IMP3]] | -0.64 | -0.42 / -0.71 | both halves | 4e-05 |  |
| [[DCTN6-DT]] | -0.63 | -0.50 / -0.69 | both halves | 1e-05 |  |
| [[SNHG19]] | -0.63 | -0.48 / -0.64 | both halves | 2e-05 |  |
| [[CTBP1-AS]] ⚠ | -0.63 | -0.47 / -0.64 | both halves | 2e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[ZNHIT1]] | -0.63 | -0.51 / -0.68 | both halves | 1e-05 |  |
| [[SPACDR]] | -0.63 | -0.49 / -0.70 | both halves | 1e-05 |  |
| [[RSRP1]] | -0.62 | -0.45 / -0.66 | both halves | 3e-05 |  |
| [[QPCTL]] | -0.62 | -0.48 / -0.69 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 0, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PRPS1]] | C | OCRL's natural level strengthens PRPS1's drug response | OCRL's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.72, reverse +0.46; direction not clear | 0.006 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| cells under [[Bendamustine (drug)]] 0.5 µM | C | OCRL's natural level lowers the cells' numbers under Bendamustine 0.5 µM (makes them more sensitive) | OCRL's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.57 | 0.507 over the table, 0.098 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

## Where it sits

- **Module**: [[Module 025]] — oxidative phosphorylation; 171 genes; this gene is in the **+** arm (projection on the module's main direction 0.792). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-31.0, -19.4); signed map (-15.5, -38.3). **Vector** length 101, 24.4% of its response variance represented; |z| ≥ 3 in 714 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +9.6 | +8.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +8.8 | +5.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +7.4 | +1.5 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +3.8 | +1.8 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +3.6 | +4.2 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.5 | -0.0 |
|  | [[Folic acid (drug)]] 5 µM |  | +2.0 | +3.3 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | +2.0 | +2.3 |
|  | [[Adenine (drug)]] 5 µM |  | +1.9 | +1.9 |
|  | [[venetoclax (drug)]] 5 µM |  | +1.9 | +1.2 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -7.8 | -16.4 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -4.5 | -4.3 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.8 | -2.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.7 | -1.8 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | -2.3 | -4.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -2.3 | -2.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.2 | -0.8 |
|  | [[Sivelestat (sodium tetrahydrate) (drug)]] 0.5 µM |  | -2.1 | -2.0 |
|  | [[Azithromycin (hydrate) (drug)]] 5 µM |  | -2.0 | -2.9 |

## What is on record

|  |  |
|---|---|
| Name | OCRL inositol polyphosphate-5-phosphatase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xq26.1 — chrX:129,539,849-129,592,561 (+) |
| Ensembl biotype | protein_coding |
| Also known as | OCRL1, Dent-2 |
| Gene groups (HGNC) | Phosphoinositide phosphatases |
| Hallmark sets | PROTEIN_SECRETION |
| Reactome | 18 pathways, smallest: Synthesis of IP2, IP, and Ins in the cytosol; Synthesis of PIPs at the Golgi membrane; Synthesis of IP3 and IP4 in the cytosol |
| Matched by | ensembl_id |

**Function**, from UniProt [Q01968](https://www.uniprot.org/uniprotkb/Q01968) (Inositol polyphosphate 5-phosphatase OCRL):

> Catalyzes the hydrolysis of the 5-position phosphate of phosphatidylinositol 4,5-bisphosphate (PtdIns(4,5)P2) and phosphatidylinositol-3,4,5-bisphosphate (PtdIns(3,4,5)P3), with the greatest catalytic activity towards PtdIns(4,5)P2. Also, is able to hydrolyze the 5-phosphate of inositol 1,4,5-trisphosphate and of inositol 1,3,4,5-tetrakisphosphate. Regulates traffic in the endosomal pathway by regulating the specific pool of phosphatidylinositol 4,5-bisphosphate that is associated with …

**Summary**, from NCBI Gene [4952](https://www.ncbi.nlm.nih.gov/gene/4952):

> This gene encodes an inositol polyphosphate 5-phosphatase. This protein is involved in regulating membrane trafficking and is located in numerous subcellular locations including the trans-Golgi network, clathrin-coated vesicles and, endosomes and the plasma membrane. This protein may also play a role in primary cilium formation. Mutations in this gene cause oculocerebrorenal syndrome of Lowe and also Dent disease. Alternate splicing results in multiple transcript variants. [provided by RefSeq, …

**Accessions** — [HGNC:8108](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8108) · Entrez [4952](https://www.ncbi.nlm.nih.gov/gene/4952) · UniProt [Q01968](https://www.uniprot.org/uniprotkb/Q01968) · Ensembl [ENSG00000122126](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000122126)

## Data

Gene col 4321: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4321); `tables/drug_effects.parquet` (12 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4321, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4321]; `tensor/DDL_lfc|DDL_z.npy` [4321]; `embed/gene_vectors.npy` [4321]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4321 or target_col == 4321). Every well: [[OCRL — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/OCRL.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
