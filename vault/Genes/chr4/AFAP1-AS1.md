---
symbol: "AFAP1-AS1"
type: "gene"
col: 15730
ensembl_id: "ENSG00000272620"
name: "AFAP1 antisense RNA 1"
location: "4p16.1"
module: 42
arm: "+"
pooled_cpm: 20.74
n_lines_expressing: 17
n_dd_up: 18
n_dd_down: 0
n_dd_up_clean: 11
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 4
tags: ["gene", "module/042"]
generated_by: "tahoemap"
---

# AFAP1-AS1

*AFAP1 antisense RNA 1* — 4p16.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.29× (z +11.6, q 2e-28, up in 1 of 10 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.58× (z +9.5, q 1e-18, up in 10 of 15 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (SK-MEL-2 0.288×; ⚠ cell-cycle shift, explains ~0% of this change).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LRRC59]] (+0.59, fdr 1e-05), [[TMEM214]] (+0.54, fdr 2e-05), [[CANX]] (+0.51, fdr 4e-05); moves opposite to [[GATAD2B]] (-0.51, fdr 5e-05), [[SMURF1]] (-0.46, fdr 6e-05), [[CYBA]] (-0.46, fdr 1e-04).
> It is in [[Module 042]], a single-armed module (UPR ER).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TSTD1]] → it (grade B ⚠); 4 go from it, the strongest it → [[CCT7]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 9 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15730.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.29×** | +11.6 | 2e-28 | 1/10 (Panc 03.27) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.58×** | +9.5 | 1e-18 | 10/15 (HOP62, PANC-1, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.70×** | +7.7 | 2e-12 | 1/14 (Hs 766T) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift; position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.58×** | +6.4 | 2e-08 | 7/15 (HOP62, SW 900, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.50×** | +5.9 | 4e-07 | 10/15 (COLO 205, A498, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.42×** | +4.9 | 1e-04 | 9/15 (SK-MEL-2, HOP62, …) | top dose only | cell-cycle shift (explains ~5% here); position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.40×** | +4.8 | 1e-04 | 2/15 (PANC-1, CFPAC-1) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here); position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.41×** | +4.8 | 1e-04 | 7/15 (A498, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~12% here); position effect removed |
| [[venetoclax (drug)]] 5 µM |  | **1.78×** | +4.4 | 8e-04 | 6/14 (PANC-1, AsPC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **1.30×** | +3.8 | 0.008 | 9/15 (AsPC-1, NCI-H1573, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | 1.20× | +3.7 | 0.010 | 1/15 (Hs 766T) | rises with dose | position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~17% of this change | **1.31×** | +3.7 | 0.011 | 1/13 (PANC-1) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.19× | +3.6 | 0.016 | 7/15 (CFPAC-1, Panc 03.27, …) | rises with dose | composition shift |
| [[Verteporfin (drug)]] 0.05 µM |  | **1.29×** | +3.4 | 0.027 | 0/15 | inconsistent across doses | position effect removed |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~1% of this change | 1.18× | +3.4 | 0.029 | 10/15 (CFPAC-1, Panc 03.27, …) | rises with dose | low cells (technical?) |
| [[Terfenadine (drug)]] 0.5 µM |  | **1.26×** | +3.3 | 0.031 | 8/15 (COLO 205, HT-29, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 0.5 µM |  | **1.25×** | +3.3 | 0.034 | 4/15 (SK-MEL-2, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.25×** | +3.2 | 0.043 | 0/15 | inconsistent across doses | position effect removed |
| [[Verteporfin (drug)]] 5 µM |  | **1.25×** | +3.1 | 0.067 | 0/15 | inconsistent across doses | position effect removed |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.48×** | +3.0 | 0.077 | 10/15 (CFPAC-1, Panc 03.27, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 15730.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (SK-MEL-2 0.288×; ⚠ cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.861× | -7.9 | 2e-12 | 5/15 (Panc 03.27, CFPAC-1, …) | inconsistent across doses |  |
| [[Gallic acid (hydrate) (drug)]] 0.05 µM |  | 0.805× | -3.2 | 0.43 | 5/15 (Panc 03.27, CFPAC-1, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.12 per unit of S-phase module lfc, -0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15730. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[CFPAC-1 (line)]] | alt | 54.7 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.56× (z +9.2) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[HOP62 (line)]] | alt | 40.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.80× (z +10.4) | — |
| [[HT-29 (line)]] | alt | 34.8 | 1 (1 ⚠) | 0 | [[c-Kit-IN-1 (drug)]] 0.05 µM 4.26× (z +9.0) ⚠ unreliable plate only | — |
| [[PANC-1 (line)]] | alt | 20.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.90× (z +9.8) | — |
| [[SK-MEL-2 (line)]] | alt | 37.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.288× (z -10.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 3.58 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 1.77 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 118 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.56 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 3.89 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 33.0 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.12 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 2.42 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 3.14 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 2.84 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 89.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.18 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 178 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.17 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 2.28 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 8.92 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.01 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.62 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 3.90 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 98.9 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 2.38 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 2.73 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 2.30 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.68 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 25.3 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.86 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 1.95 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.95 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 3.98 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 2.59 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.84 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 37.7 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.28 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 4.25 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 2.04 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 17.5 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.33 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 4.40 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 2.79 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 78.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.00 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 2.59 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 2.00 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15730), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*67 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LRRC59]] | +0.59 | +0.59 / +0.53 | both halves | 1e-05 |  |
| [[TMEM214]] | +0.54 | +0.48 / +0.53 | both halves | 2e-05 |  |
| [[CANX]] | +0.51 | +0.50 / +0.42 | both halves | 4e-05 |  |
| [[ZNF460]] | +0.51 | +0.46 / +0.48 | both halves | 3e-05 |  |
| [[USO1]] | +0.51 | +0.46 / +0.45 | both halves | 3e-05 |  |
| [[FKBP4]] | +0.50 | +0.49 / +0.43 | both halves | 3e-05 |  |
| [[CCT7]] | +0.49 | +0.54 / +0.35 | both halves | 1e-04 |  |
| [[GMPPB]] | +0.49 | +0.43 / +0.39 | both halves | 5e-05 |  |
| [[ZNF587]] | +0.48 | +0.34 / +0.45 | both halves | 1e-04 |  |
| [[HSPA13]] | +0.47 | +0.40 / +0.41 | both halves | 5e-05 |  |
| [[TMED2]] | +0.47 | +0.42 / +0.49 | both halves | 4e-05 |  |
| [[CKAP4]] | +0.46 | +0.54 / +0.30 | both halves | 2e-04 |  |

## Genes that move opposite

*33 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GATAD2B]] | -0.51 | -0.40 / -0.49 | both halves | 5e-05 |  |
| [[SMURF1]] | -0.46 | -0.42 / -0.39 | both halves | 6e-05 |  |
| [[CYBA]] | -0.46 | -0.39 / -0.35 | both halves | 1e-04 |  |
| [[TSTD1]] | -0.45 | -0.44 / -0.34 | both halves | 1e-04 |  |
| [[SIGIRR]] | -0.45 | -0.42 / -0.29 | both halves | 2e-04 |  |
| [[MAP3K3]] | -0.44 | -0.40 / -0.38 | both halves | 6e-05 |  |
| [[MARCHF2]] | -0.43 | -0.45 / -0.31 | both halves | 2e-04 |  |
| [[CROCCP2-1]] | -0.43 | -0.42 / -0.36 | both halves | 9e-05 |  |
| [[ARL17B]] | -0.42 | -0.55 / -0.35 | both halves | 1e-04 |  |
| [[ZFAND6]] | -0.42 | -0.34 / -0.40 | both halves | 1e-04 |  |
| [[GABARAPL2]] | -0.42 | -0.47 / -0.30 | both halves | 2e-04 |  |
| [[LLGL2]] | -0.42 | -0.36 / -0.25 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TSTD1]] | B | TSTD1 activity raises AFAP1-AS1's level | lines that do not express TSTD1 (19) vs lines expressing it (31) | 2.18× lower at baseline in the lines without TSTD1 | 0.078 | ⚠ within organs, on part of the lines; co-absent genes; also absent: CHMP4C, STYK1, SAMD12 |

### Downstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CCT7]] | B | AFAP1-AS1 activity lowers CCT7's level | lines that do not express AFAP1-AS1 (33) vs lines expressing it (17) | 1.26× higher at baseline in the lines without AFAP1-AS1 | 0.060 | ⚠ within organs, on part of the lines; also absent: AGR2, GABRP, LINC01610 |
| [[MAPK8IP3]] | B | AFAP1-AS1 activity raises MAPK8IP3's level | lines that do not express AFAP1-AS1 (33) vs lines expressing it (17) | 1.17× lower at baseline in the lines without AFAP1-AS1 | 0.069 | ⚠ within organs, on part of the lines; also absent: AGR2, GABRP, LINC01610 |
| [[IPO4]] | B | AFAP1-AS1 activity lowers IPO4's level | lines that do not express AFAP1-AS1 (33) vs lines expressing it (17) | 1.33× higher at baseline in the lines without AFAP1-AS1 | 0.096 | ⚠ within organs, on part of the lines; also absent: AGR2, GABRP, LINC01610 |
| [[SLC16A1]] | B | AFAP1-AS1 activity lowers SLC16A1's level | lines that do not express AFAP1-AS1 (33) vs lines expressing it (17) | 1.37× higher at baseline in the lines without AFAP1-AS1 | 0.099 | ⚠ within organs, on part of the lines; also absent: AGR2, GABRP, LINC01610 |

## Where it sits

- **Module**: [[Module 042]] — UPR ER; 103 genes; every member is in the + arm (projection on the module's main direction 0.365). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-21.5, -17.9); signed map (-56.9, 8.8). **Vector** length 41.0, 12.5% of its response variance represented; |z| ≥ 3 in 237 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.3 | +9.5 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +3.0 | +3.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.4 | +11.6 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | +2.3 | +4.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.1 | +7.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.8 | +5.9 |
|  | [[TAK-733 (drug)]] 5 µM |  | +1.7 | +2.0 |
|  | [[venetoclax (drug)]] 5 µM |  | +1.7 | +4.4 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +1.6 | +3.0 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +1.6 | +2.1 |
| fall | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.0 | +0.2 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.0 | -0.7 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -1.0 | +0.2 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -0.9 | -0.8 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift | -0.9 | -1.5 |
|  | [[Rapamycin (drug)]] 5 µM |  | -0.7 | -1.6 |
|  | [[Pentamidine (isethionate) (drug)]] 5 µM |  | -0.7 | +0.2 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -0.7 | -1.6 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -0.6 | -1.4 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -0.6 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | AFAP1 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 4p16.1 — chr4:7,754,077-7,778,928 (+) |
| Ensembl biotype | lncRNA |
| Also known as | ATMLP, MGC10981; previously AFAP1AS, AFAP1-AS |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

**Summary**, from NCBI Gene [84740](https://www.ncbi.nlm.nih.gov/gene/84740):

> This gene produces a long non-coding RNA that is overexpressed in tumor cells and may promote cancer cell metastasis. [provided by RefSeq, Dec 2017]

**Accessions** — [HGNC:28141](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28141) · Entrez [84740](https://www.ncbi.nlm.nih.gov/gene/84740) · Ensembl [ENSG00000272620](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000272620)

## Data

Gene col 15730: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15730); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15730, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15730]; `tensor/DDL_lfc|DDL_z.npy` [15730]; `embed/gene_vectors.npy` [15730]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15730 or target_col == 15730). Every well: [[AFAP1-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/AFAP1-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
