---
symbol: "WAKMAR2"
type: "gene"
col: 14137
ensembl_id: "ENSG00000237499"
name: "wound and keratinocyte migration associated lncRNA 2"
location: "6q23.3"
module: 80
arm: "+"
pooled_cpm: 3.89
n_lines_expressing: 48
n_dd_up: 33
n_dd_down: 1
n_dd_up_clean: 24
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 1
direction_downstream: 1
tags: ["gene", "module/080"]
generated_by: "tahoemap"
---

# WAKMAR2

*wound and keratinocyte migration associated lncRNA 2* — 6q23.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 33 drug-doses (9 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 11.6× (z +37.2, q 0e+00, up in 33 of 34 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Adagrasib (drug)]] 0.05 µM: 0.887× (z -4.7, q 0.002, down in 16 of 44 measured lines) ⚠ position not correctable. The strongest without an alert is [[Tadalafil (drug)]] 5 µM: 0.691× (z -3.8, q 0.035, down in 6 of 37 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 7 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 1 line (NCI-H23 0.0892×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Niclosamide (olamine) (drug)]] 5 µM in 1 line (NCI-H23 0.0834×; ⚠ toxic; cell-cycle shift, explains ~29% of this change); [[Auranofin (drug)]] 5 µM in 1 line (NCI-H23 0.140×).
> Its strongest partners by |cos| (95 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF341-AS1]] (+0.80, fdr 7e-06), [[PIGV]] (+0.75, fdr 4e-05), [[EYS]] (+0.74, fdr 1e-05); moves opposite to [[FAM118A]] (-0.65, fdr 4e-04), [[INPP4A]] (-0.63, fdr 4e-05), [[ST6GALNAC4]] (-0.63, fdr 1e-04).
> It is in [[Module 080]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); 1 goes from it, the strongest it → [[DENND3-AS1]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 33 in all, 9 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 33 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14137.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **11.6×** | +37.2 | 0e+00 | 33/34 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **11.0×** | +36.4 | 0e+00 | 30/31 (NCI-H1573, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Harringtonine (drug)]] 5 µM |  | **7.86×** | +21.3 | 0e+00 | 34/36 (SNU-423, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **5.48×** | +18.2 | 0e+00 | 29/32 (NCI-H460, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **5.12×** | +16.8 | 0e+00 | 29/32 (NCI-H460, SNU-423, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **4.42×** | +15.3 | 0e+00 | 26/33 (HOP62, HS-578T, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.16×** | +15.3 | 0e+00 | 12/14 (PANC-1, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~13% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **2.54×** | +14.1 | 3e-43 | 26/43 (HOP62, NCI-H2347, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.31×** | +12.3 | 4e-33 | 3/7 (HOP62, SNU-423, …) | all doses, flat | cell-cycle shift (explains ~13% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.25×** | +11.7 | 1e-29 | 5/9 (J82, HOP62, …) | all doses, flat | cell-cycle shift (explains ~10% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **2.42×** | +9.5 | 2e-19 | 21/39 (C32, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.42×** | +9.1 | 5e-18 | 13/19 (HS-578T, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[TAK-901 (drug)]] 5 µM |  | **4.90×** | +8.9 | 2e-17 | 23/34 (NCI-H460, LoVo, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~5% here); composition shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM |  | **1.52×** | +6.4 | 8e-09 | 15/42 (NCI-H460, J82, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.50×** | +6.1 | 4e-08 | 16/42 (SW480, SW1417, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.70×** | +5.7 | 5e-07 | 13/40 (NCI-H2347, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.61×** | +5.1 | 1e-05 | 13/39 (A-172, HT-29, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.57×** | +4.8 | 5e-05 | 11/42 (NCI-H2347, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Triamcinolone (drug)]] 5 µM |  | **1.32×** | +4.2 | 7e-04 | 7/42 (HOP62, Hs 766T, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 14137.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 7 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 1 line (NCI-H23 0.0892×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Niclosamide (olamine) (drug)]] 5 µM in 1 line (NCI-H23 0.0834×; ⚠ toxic; cell-cycle shift, explains ~29% of this change); [[Auranofin (drug)]] 5 µM in 1 line (NCI-H23 0.140×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.887× | -4.7 | 0.002 | 16/44 (A549, HT-29, …) | inconsistent across doses |  |
| [[Tadalafil (drug)]] 5 µM |  | **0.691×** | -3.8 | 0.035 | 6/37 (RPMI-7951, A498, …) | top dose only |  |
| [[Rifaximin (drug)]] 5 µM |  | 0.721× | -3.4 | 0.13 | 10/38 (NCI-H2030, HT-29, …) | all doses, flat | position effect removed |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | 0.754× | -3.0 | 0.33 | 4/43 (NCI-H23, J82, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.18 per unit of S-phase module lfc, +0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14137. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H23 (line)]] | alt | 34.5 | 0 | 6 (5 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0892× (z -14.0) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.140× (z -11.4) |
| [[NCI-H460 (line)]] | wt | 12.2 | 4 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 7.39× (z +18.0) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.238× (z -9.1) ⚠ unreliable plate only |
| [[C32 (line)]] | wt | 11.6 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.1× (z +13.2) | — |
| [[HS-578T (line)]] | alt | 3.13 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 53.7× (z +15.5) | — |
| [[A-172 (line)]] | wt | 4.42 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 38.9× (z +15.8) | — |
| [[SNU-423 (line)]] | alt | 4.64 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 49.4× (z +15.5) | — |
| [[HOP62 (line)]] | alt | 2.65 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 35.3× (z +14.9) | — |
| [[LoVo (line)]] | wt | 1.61 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 34.3× (z +13.0) | — |
| [[NCI-H1573 (line)]] | alt | 5.39 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 19.9× (z +15.6) | — |
| [[PANC-1 (line)]] | alt | 1.36 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 31.5× (z +15.9) | — |
| [[HEC-1-A (line)]] | alt | 1.58 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 14.7× (z +9.9) | — |
| [[HepG2_C3A (line)]] | wt | 3.61 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 19.3× (z +9.8) | — |
| [[hTERT-HPNE (line)]] | wt | 3.26 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 22.8× (z +10.9) | — |
| [[J82 (line)]] | alt | 6.91 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 12.6× (z +14.6) | — |
| [[NCI-H2030 (line)]] | alt | 2.41 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 25.8× (z +15.0) | — |
| [[SW 900 (line)]] | alt | 2.46 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 29.8× (z +12.1) | — |
| [[A498 (line)]] | wt | 2.41 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 12.5× (z +11.5) | — |
| [[AsPC-1 (line)]] | alt | 2.79 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 11.5× (z +9.9) | — |
| [[BT-474 (line)]] | alt | 2.59 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 23.4× (z +9.2) | — |
| [[CFPAC-1 (line)]] | alt | 1.44 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 25.1× (z +10.8) | — |
| [[COLO 205 (line)]] | alt | 3.86 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 14.1× (z +9.1) | — |
| [[Hs 766T (line)]] | wt | 1.86 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 12.9× (z +8.7) | — |
| [[LS 180 (line)]] | wt | 3.11 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.31× (z +9.7) | — |
| [[NCI-H1792 (line)]] | alt | 3.29 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 32.9× (z +14.1) | — |
| [[NCI-H2347 (line)]] | alt | 6.32 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.00× (z +10.1) | — |
| [[Panc 03.27 (line)]] | alt | 1.81 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 38.5× (z +11.3) | — |
| [[RPMI-7951 (line)]] | alt | 3.24 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 17.2× (z +9.2) | — |
| [[SW48 (line)]] | wt | 2.33 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 100× (z +11.7) | — |
| [[SW480 (line)]] | alt | 3.09 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.40× (z +8.7) | — |
| [[A-427 (line)]] | wt | 1.08 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.09 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.89 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.889 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 1.45 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.98 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.45 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.20 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.25 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.89 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.05 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.73 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.71 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.13 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.14 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.21 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.43 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.972 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 3.79 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.74 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.87 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14137), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 5 of them with an alert (⚠; 5 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF341-AS1]] | +0.80 | +0.74 / +0.62 | both halves | 7e-06 |  |
| [[PIGV]] | +0.75 | +0.80 / +0.41 | both halves | 4e-05 |  |
| [[EYS]] | +0.74 | +0.76 / +0.51 | both halves | 1e-05 |  |
| [[CDK6-AS1]] | +0.73 | +0.63 / +0.50 | both halves | 1e-05 |  |
| [[NEK8]] | +0.73 | +0.74 / +0.39 | both halves | 5e-05 |  |
| [[ENO3]] | +0.72 | +0.74 / +0.49 | both halves | 1e-05 |  |
| [[SEPTIN7-DT]] | +0.72 | +0.72 / +0.37 | both halves | 9e-05 |  |
| [[TMEM202-AS1]] | +0.71 | +0.72 / +0.37 | both halves | 8e-05 |  |
| [[F8]] | +0.71 | +0.73 / +0.42 | both halves | 4e-05 |  |
| [[TIGD6]] | +0.71 | +0.73 / +0.42 | both halves | 4e-05 |  |
| [[MZF1-AS1]] | +0.70 | +0.76 / +0.28 | both halves | 3e-04 |  |
| [[RBMS3-AS3]] | +0.70 | +0.69 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FAM118A]] | -0.65 | -0.61 / -0.26 | both halves | 4e-04 |  |
| [[INPP4A]] | -0.63 | -0.49 / -0.41 | both halves | 4e-05 |  |
| [[ST6GALNAC4]] | -0.63 | -0.62 / -0.33 | both halves | 1e-04 |  |
| [[MAST3]] | -0.63 | -0.57 / -0.23 | both halves | 5e-04 |  |
| [[BRF1]] | -0.62 | -0.61 / -0.25 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers WAKMAR2's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 6.4% of all compounds | 0.053 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DENND3-AS1]] | C | WAKMAR2's natural level weakens DENND3-AS1's drug response | WAKMAR2's natural level across 44 lines (lineage-adjusted; a glimpse) | r -0.66, reverse +0.18; direction not clear | 0.074 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others; direction unclear |

## Where it sits

- **Module**: [[Module 080]]; 57 genes; every member is in the + arm (projection on the module's main direction 0.854). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.36; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (14.4, 11.3); signed map (28.2, 4.8). **Vector** length 82.4, 15.5% of its response variance represented; |z| ≥ 3 in 1,140 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +10.6 | +36.4 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +9.6 | +37.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +6.6 | +14.1 |
|  | [[Harringtonine (drug)]] 5 µM |  | +6.3 | +21.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.2 | +12.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.0 | +6.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.1 | +5.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.9 | +3.0 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.8 | +4.2 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -4.0 | -1.2 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.2 | -1.7 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | -3.1 | +0.2 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~95% of this change | -2.8 | +1.5 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -2.5 | -2.0 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.4 | -1.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.9 | -0.4 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.5 | -3.0 |
|  | [[Ipatasertib (drug)]] 5 µM |  | -1.5 | -2.1 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.4 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | wound and keratinocyte migration associated lncRNA 2 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 6q23.3 — chr6:137,823,673-137,868,233 (-) |
| Ensembl biotype | lncRNA |
| Also known as | lnc-TNFAIP3 |
| Gene groups (HGNC) | Long non-coding RNAs with non-systematic symbols |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:53754](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:53754) · Entrez [100130476](https://www.ncbi.nlm.nih.gov/gene/100130476) · Ensembl [ENSG00000237499](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000237499)

## Data

Gene col 14137: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14137); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14137, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14137]; `tensor/DDL_lfc|DDL_z.npy` [14137]; `embed/gene_vectors.npy` [14137]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14137 or target_col == 14137). Every well: [[WAKMAR2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/WAKMAR2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
