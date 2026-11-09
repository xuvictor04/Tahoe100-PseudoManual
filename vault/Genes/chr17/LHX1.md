---
symbol: "LHX1"
type: "gene"
col: 15794
ensembl_id: "ENSG00000273706"
name: "LIM homeobox 1"
location: "17q12"
module: 112
arm: "+"
pooled_cpm: 6.34
n_lines_expressing: 23
n_dd_up: 10
n_dd_down: 1
n_dd_up_clean: 4
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 2
direction_downstream: 6
tags: ["gene", "module/112"]
generated_by: "tahoemap"
---

# LHX1

*LIM homeobox 1* — 17q12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (6 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.62× (z +10.0, q 9e-21, up in 9 of 18 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Clobetasol propionate (drug)]] 5 µM: 0.573× (z -4.1, q 0.023, down in 11 of 21 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Adagrasib (drug)]] 0.05 µM in 2 lines (MIA PaCa-2 0.514×, HOP62 0.583×; ⚠ position not correctable); [[Panobinostat (drug)]] 0.5 µM in 1 line (SW480 0.1000×; ⚠ cell-cycle shift, would explain all of this change); [[Imiquimod (maleate) (drug)]] 5 µM in 1 line (A-172 0.0861×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC03042]] (+0.60, fdr 2e-05), [[LHX1-DT]] (+0.60, fdr 7e-06, ⚠ same locus), [[LIF-AS2]] (+0.58, fdr 1e-04), [[IL23A]] (+0.56, fdr 3e-05); moves opposite to [[ATL3]] (-0.55, fdr 8e-05), [[COPS8]] (-0.54, fdr 4e-05), [[PDLIM1]] (-0.52, fdr 2e-05).
> It is in [[Module 112]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[FMNL1-DT]] → it (grade B ⚠); 6 go from it, the strongest it → [[LBH]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 6 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15794.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.62×** | +10.0 | 9e-21 | 9/18 (HOP62, Hs 766T, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **2.47×** | +6.4 | 5e-08 | 2/8 (SNU-423, PANC-1) | all doses, stronger at high dose | composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.71×** | +5.6 | 4e-06 | 8/21 (PANC-1, SW480, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **2.00×** | +5.1 | 4e-05 | 4/16 (Hs 766T, HOP62, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~64% of this change | **1.63×** | +5.1 | 4e-05 | 9/18 (HOP62, SNU-423, …) | rises with dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | **1.98×** | +5.0 | 5e-05 | 0/11 | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.96×** | +4.7 | 2e-04 | 8/14 (Hs 766T, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **1.93×** | +4.5 | 6e-04 | 4/10 (Hs 766T, SNU-423, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.71×** | +3.9 | 0.005 | 8/19 (HOP62, PANC-1, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.45×** | +3.8 | 0.008 | 5/21 (NCI-H23, C32, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | 1.55× | +3.1 | 0.11 | 4/19 (Hs 766T, HOP62, …) | top dose only | cell-cycle shift (explains ~11% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 15794.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Adagrasib (drug)]] 0.05 µM in 2 lines (MIA PaCa-2 0.514×, HOP62 0.583×; ⚠ position not correctable); [[Panobinostat (drug)]] 0.5 µM in 1 line (SW480 0.1000×; ⚠ cell-cycle shift, would explain all of this change); [[Imiquimod (maleate) (drug)]] 5 µM in 1 line (A-172 0.0861×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Clobetasol propionate (drug)]] 5 µM |  | **0.573×** | -4.1 | 0.023 | 11/21 (HOP62, A498, …) | rises with dose |  |
| [[Budesonide (drug)]] 5 µM |  | 0.621× | -3.5 | 0.11 | 9/21 (HOP62, SNU-423, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.616× | -3.4 | 0.11 | 6/21 (SNU-423, SW480, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 5 µM |  | 0.617× | -3.1 | 0.30 | 8/21 (SW480, MIA PaCa-2, …) | inconsistent across doses | cell-cycle shift (explains ~20% here); noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.14 per unit of S-phase module lfc, +0.41 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15794. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 12.1 | 4 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 8.98× (z +14.6) ⚠ cell-cycle shift, explains ~64% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.64× (z +10.2) | [[Adagrasib (drug)]] 0.05 µM 0.583× (z -8.6) ⚠ position not correctable |
| [[A-172 (line)]] | wt | 7.12 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.65× (z +9.0) | [[Imiquimod (maleate) (drug)]] 5 µM 0.0861× (z -9.6) |
| [[MIA PaCa-2 (line)]] | alt | 62.0 | 0 | 2 (2 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.514× (z -11.7) ⚠ position not correctable |
| [[Hs 766T (line)]] | wt | 9.20 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.12× (z +9.1) | — |
| [[LOX-IMVI (line)]] | wt | 6.86 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0863× (z -9.0) ⚠ toxic; cell-cycle shift, explains ~49% of this change |
| [[SNU-423 (line)]] | alt | 20.0 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.98× (z +12.4) ⚠ cell-cycle shift, explains ~64% of this change | — |
| [[SW480 (line)]] | alt | 8.02 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.1000× (z -10.3) ⚠ cell-cycle shift, would explain all of this change |
| [[A-427 (line)]] | wt | 0.765 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 36.3 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.35 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 0.608 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 1.91 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 0.620 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.788 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 3.54 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.469 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 1.55 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 3.42 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.910 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.65 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.04 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 0.473 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.622 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.467 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.960 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.382 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.857 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.309 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.566 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 2.13 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 0.341 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 2.20 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.65 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.45 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 1.19 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 3.16 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.837 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 4.10 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 6.01 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.322 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.51 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.322 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.492 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.398 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 1.17 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 1.19 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 2.58 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.99 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.895 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15794), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC03042]] | +0.60 | +0.62 / +0.47 | both halves | 2e-05 |  |
| [[LHX1-DT]] | +0.60 | +0.63 / +0.62 | both halves | 7e-06 | ⚠ same locus (0.1 kb: neighbours can correlate without regulation) |
| [[LIF-AS2]] | +0.58 | +0.33 / +0.60 | both halves | 1e-04 |  |
| [[IL23A]] | +0.56 | +0.44 / +0.54 | both halves | 3e-05 |  |
| [[SYNJ2]] | +0.56 | +0.50 / +0.53 | both halves | 1e-05 |  |
| [[SPHK1]] | +0.55 | +0.47 / +0.62 | both halves | 2e-05 |  |
| [[LINC00973]] | +0.55 | +0.47 / +0.41 | both halves | 4e-05 |  |
| [[SOX9]] | +0.54 | +0.40 / +0.58 | both halves | 5e-05 |  |
| [[FAM43A]] | +0.53 | +0.37 / +0.53 | both halves | 8e-05 |  |
| [[LIF]] | +0.53 | +0.49 / +0.45 | both halves | 3e-05 |  |
| [[NPTX1]] | +0.53 | +0.38 / +0.55 | both halves | 6e-05 |  |
| [[PINLYP]] | +0.52 | +0.41 / +0.51 | both halves | 4e-05 |  |
| [[ISM1]] | +0.52 | +0.53 / +0.35 | both halves | 1e-04 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATL3]] | -0.55 | -0.37 / -0.55 | both halves | 8e-05 |  |
| [[COPS8]] | -0.54 | -0.42 / -0.51 | both halves | 4e-05 |  |
| [[PDLIM1]] | -0.52 | -0.52 / -0.48 | both halves | 2e-05 |  |
| [[DPY19L4]] | -0.48 | -0.38 / -0.44 | both halves | 7e-05 |  |
| [[CPD]] | -0.47 | -0.35 / -0.45 | both halves | 1e-04 |  |
| [[DROSHA]] | -0.45 | -0.29 / -0.47 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FMNL1-DT]] | B | FMNL1-DT activity raises LHX1's level | lines that do not express FMNL1-DT (23) vs lines expressing it (27) | 1.80× lower at baseline in the lines without FMNL1-DT | 0.039 | ⚠ within organs, on part of the lines; also absent: CACNG6, FMNL1, SLFN11; maybe low, not absent |
| [[LHX1-DT]] | C | LHX1-DT activity raises LHX1's level | lines that do not express LHX1-DT (28) vs lines expressing it (22) | 3.49× lower at baseline in the lines without LHX1-DT | 0.001 | ⚠ within organs, on part of the lines; also absent: LHX1, EYA4, CDH4; co-absent with the target |

### Downstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 4, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LBH]] | B | LHX1 activity raises LBH's level | lines that do not express LHX1 (27) vs lines expressing it (23) | 2.99× lower at baseline in the lines without LHX1 | 0.033 | ⚠ within organs, on part of the lines; also absent: LHX1-DT, ADAMTS16, ECSCR |
| [[FAM43A]] | B | LHX1 activity raises FAM43A's level | lines that do not express LHX1 (27) vs lines expressing it (23) | 1.82× lower at baseline in the lines without LHX1 | 0.072 | ⚠ within organs, on part of the lines; also absent: LHX1-DT, ADAMTS16, ECSCR |
| [[FOSL1]] | B | LHX1 activity raises FOSL1's level | lines that do not express LHX1 (27) vs lines expressing it (23) | 1.83× lower at baseline in the lines without LHX1 | 0.088 | ⚠ within organs, on part of the lines; also absent: LHX1-DT, ADAMTS16, ECSCR |
| [[SHB]] | B | LHX1 activity raises SHB's level | lines that do not express LHX1 (27) vs lines expressing it (23) | 1.56× lower at baseline in the lines without LHX1 | 0.089 | ⚠ within organs, on part of the lines; also absent: LHX1-DT, ADAMTS16, ECSCR |
| [[LHX1-DT]] | C | LHX1 activity raises LHX1-DT's level | lines that do not express LHX1 (27) vs lines expressing it (23) | 2.96× lower at baseline in the lines without LHX1 | 0.001 | ⚠ within organs, on part of the lines; also absent: LHX1-DT, ADAMTS16, ECSCR; co-absent with the target |
| [[TMEM163]] | C | LHX1 activity raises TMEM163's level | lines that do not express LHX1 (27) vs lines expressing it (23) | 1.93× lower at baseline in the lines without LHX1 | 0.066 | ⚠ within organs, on part of the lines; also absent: LHX1-DT, ADAMTS16, ECSCR; co-absent with the target |

## Where it sits

- **Module**: [[Module 112]] — TNF-alpha signaling via NF-kB; 43 genes; every member is in the + arm (projection on the module's main direction 0.647). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (44.5, -4.0); signed map (10.8, 37.9). **Vector** length 44.1, 9.47% of its response variance represented; |z| ≥ 3 in 485 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.1 | +10.0 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~64% of this change | +3.2 | +5.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.2 | +3.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +1.7 | +2.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | +1.6 | +6.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.6 | +2.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.3 | +1.2 |
|  | [[Entrectinib (drug)]] 5 µM |  | +1.2 | +1.6 |
|  | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | +1.1 | +1.1 |
| fall | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.1 | -2.5 |
|  | [[Budesonide (drug)]] 5 µM |  | -1.9 | -3.5 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.8 | -2.6 |
|  | [[Trametinib (drug)]] 5 µM |  | -1.8 | -3.1 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -1.7 | -4.1 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | -1.4 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | LIM homeobox 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q12 — chr17:36,936,785-36,944,612 (+) |
| Ensembl biotype | protein_coding |
| Also known as | LIM-1, LIM1 |
| Gene groups (HGNC) | LIM class homeoboxes |
| Reactome | 5 pathways, smallest: Formation of intermediate mesoderm; Nephron development; Formation of the nephric duct |
| Matched by | ensembl_id |

**Function**, from UniProt [P48742](https://www.uniprot.org/uniprotkb/P48742) (LIM/homeobox protein Lhx1):

> Potential transcription factor. May play a role in early mesoderm formation and later in lateral mesoderm differentiation and neurogenesis.

**Summary**, from NCBI Gene [3975](https://www.ncbi.nlm.nih.gov/gene/3975):

> This gene encodes a member of a large protein family which contains the LIM domain, a unique cysteine-rich zinc-binding domain. The encoded protein is a transcription factor important for the development of the renal and urogenital systems. This gene is a candidate for Mayer-Rokitansky-Kuster-Hauser syndrome, a disorder characterized by anomalies in the female genital tract. [provided by RefSeq, Dec 2010]

**Accessions** — [HGNC:6593](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6593) · Entrez [3975](https://www.ncbi.nlm.nih.gov/gene/3975) · UniProt [P48742](https://www.uniprot.org/uniprotkb/P48742) · Ensembl [ENSG00000273706](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000273706)

## Data

Gene col 15794: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15794); `tables/drug_effects.parquet` (15 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15794, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15794]; `tensor/DDL_lfc|DDL_z.npy` [15794]; `embed/gene_vectors.npy` [15794]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15794 or target_col == 15794). Every well: [[LHX1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LHX1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
