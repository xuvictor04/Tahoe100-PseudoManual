---
symbol: "PDIA3P1"
type: "gene"
col: 11139
ensembl_id: "ENSG00000180867"
name: "protein disulfide isomerase family A member 3 pseudogene 1"
location: "1q21.1"
module: 10
arm: "+"
pooled_cpm: 7.87
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 0
n_dd_up_clean: 7
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/010"]
generated_by: "tahoemap"
---

# PDIA3P1

*protein disulfide isomerase family A member 3 pseudogene 1* — 1q21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 3.77× (z +15.7, q 0e+00, up in 13 of 13 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.00× (z +12.0, q 4e-31, up in 38 of 43 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 3 lines (SNU-423 0.0813×, KATO III 0.138×, SK-MEL-2 0.157×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~10% of this change); [[Simotinib (drug)]] 5 µM in 1 line (RKO 0.0988×; ⚠ toxic); [[Doxycycline (monohydrate) (drug)]] 0.05 µM in 1 line (SNU-423 0.0800×); [[Thymol (drug)]] 0.5 µM in 1 line (PANC-1 0.264×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ERAP1]] (+0.76, fdr 7e-06), [[SUCLG2-DT]] (+0.73, fdr 1e-05), [[NXT2]] (+0.71, fdr 7e-06); moves opposite to [[WRAP73]] (-0.61, fdr 1e-04), [[PIGU]] (-0.61, fdr 3e-05), [[POLR2I]] (-0.60, fdr 6e-05).
> It sits in the **+** arm of [[Module 010]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 4 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11139.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.77×** | +15.7 | 0e+00 | 13/13 (PANC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.03×** | +13.6 | 8e-40 | 32/34 (SW480, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.00×** | +12.0 | 4e-31 | 38/43 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.36×** | +9.8 | 2e-20 | 19/24 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.52×** | +5.0 | 7e-05 | 16/44 (SW480, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.30×** | +4.6 | 5e-04 | 13/47 (Panc 03.27, J82, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.28×** | +4.4 | 0.001 | 17/48 (HOP62, SW1417, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.44×** | +4.3 | 0.001 | 11/42 (HOP62, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.39×** | +4.0 | 0.004 | 10/38 (HS-578T, CFPAC-1, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~2% here); position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **1.21×** | +3.3 | 0.059 | 6/48 (PANC-1, NCI-H1573, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.30×** | +3.2 | 0.061 | 9/46 (SNU-423, J82, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 11139.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 3 lines (SNU-423 0.0813×, KATO III 0.138×, SK-MEL-2 0.157×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~10% of this change); [[Simotinib (drug)]] 5 µM in 1 line (RKO 0.0988×; ⚠ toxic); [[Doxycycline (monohydrate) (drug)]] 0.05 µM in 1 line (SNU-423 0.0800×); [[Thymol (drug)]] 0.5 µM in 1 line (PANC-1 0.264×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.882× | -5.2 | 1e-04 | 17/48 (A-172, RKO, …) | inconsistent across doses |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | 0.680× | -3.4 | 0.22 | 8/41 (H4, A498, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM |  | 0.771× | -3.2 | 0.30 | 9/47 (SW48, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | 0.769× | -3.1 | 0.30 | 8/43 (H4, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.09 per unit of S-phase module lfc, +0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11139. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 6.90 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 6.20× (z +11.1) ⚠ toxic; transcription drop | [[Thymol (drug)]] 0.5 µM 0.264× (z -8.6) |
| [[SNU-423 (line)]] | alt | 6.31 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0813× (z -10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~10% of this change · without an alert: [[Doxycycline (monohydrate) (drug)]] 0.05 µM 0.0800× (z -9.4) |
| [[SW480 (line)]] | alt | 4.48 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.48× (z +9.6) | — |
| [[A498 (line)]] | wt | 6.55 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.75× (z +9.3) ⚠ toxic; transcription drop | — |
| [[HOP62 (line)]] | alt | 10.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.04× (z +9.3) ⚠ toxic; transcription drop | — |
| [[J82 (line)]] | alt | 12.2 | 0 | 1 (1 ⚠) | — | [[AZD2858 (drug)]] 0.5 µM 0.128× (z -8.9) ⚠ toxic |
| [[KATO III (line)]] | alt | 11.5 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.138× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~10% of this change |
| [[NCI-H460 (line)]] | wt | 7.14 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.11× (z +8.5) | — |
| [[RKO (line)]] | wt | 8.34 | 0 | 1 (1 ⚠) | — | [[Simotinib (drug)]] 5 µM 0.0988× (z -9.5) ⚠ toxic |
| [[SK-MEL-2 (line)]] | alt | 13.3 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.157× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~10% of this change |
| [[A-172 (line)]] | wt | 9.72 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 11.5 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 4.44 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 7.97 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.13 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 6.08 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 7.03 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 8.46 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 9.55 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.81 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 9.85 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 10.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 5.36 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 7.96 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.80 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 6.48 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 6.74 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 8.01 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 8.50 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 8.54 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 5.61 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 6.94 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 9.56 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 7.83 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 8.49 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.29 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 5.92 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.20 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.33 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 6.89 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.93 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 9.51 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.28 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.20 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 5.24 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 6.55 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11139), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ERAP1]] | +0.76 | +0.62 / +0.61 | both halves | 7e-06 |  |
| [[SUCLG2-DT]] | +0.73 | +0.65 / +0.49 | both halves | 1e-05 |  |
| [[NXT2]] | +0.71 | +0.62 / +0.59 | both halves | 7e-06 |  |
| [[EIF4G2]] | +0.68 | +0.60 / +0.45 | both halves | 3e-05 |  |
| [[RCN1]] | +0.68 | +0.52 / +0.44 | both halves | 3e-05 |  |
| [[PAPOLA]] | +0.68 | +0.46 / +0.60 | both halves | 3e-05 |  |
| [[STRADB]] | +0.67 | +0.56 / +0.58 | both halves | 1e-05 |  |
| [[DDX6]] | +0.66 | +0.64 / +0.42 | both halves | 4e-05 |  |
| [[HFE]] | +0.66 | +0.48 / +0.48 | both halves | 2e-05 |  |
| [[ZBED5-AS1]] | +0.66 | +0.56 / +0.48 | both halves | 2e-05 |  |
| [[RAP2C-AS1]] | +0.65 | +0.60 / +0.54 | both halves | 1e-05 |  |
| [[TAF9B]] | +0.64 | +0.54 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[WRAP73]] | -0.61 | -0.34 / -0.46 | both halves | 1e-04 |  |
| [[PIGU]] | -0.61 | -0.50 / -0.46 | both halves | 3e-05 |  |
| [[POLR2I]] | -0.60 | -0.44 / -0.38 | both halves | 6e-05 |  |
| [[VPS37C]] | -0.60 | -0.52 / -0.48 | both halves | 2e-05 |  |
| [[TARS2]] | -0.60 | -0.38 / -0.49 | both halves | 6e-05 |  |
| [[RPP21]] | -0.60 | -0.41 / -0.48 | both halves | 4e-05 |  |
| [[GTF2H2]] | -0.59 | -0.35 / -0.47 | both halves | 1e-04 |  |
| [[LCMT1]] | -0.59 | -0.53 / -0.29 | both halves | 2e-04 |  |
| [[PBX4]] | -0.58 | -0.49 / -0.37 | both halves | 7e-05 |  |
| [[FANCE]] | -0.58 | -0.30 / -0.46 | both halves | 2e-04 |  |
| [[RALGDS]] | -0.56 | -0.53 / -0.38 | both halves | 7e-05 |  |
| [[ETHE1]] | -0.56 | -0.49 / -0.22 | both halves | 6e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers PDIA3P1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 2.5% of all compounds | 0.008 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[SUSD5]] | B | SUSD5 activity raises PDIA3P1's level | lines that do not express SUSD5 (23) vs lines expressing it (27) | 1.22× lower at baseline in the lines without SUSD5 | 0.054 | ⚠ within organs, on part of the lines; also absent: EDIL3, BVES, MAP9 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 010]]; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.644). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-1.2, 12.3); signed map (18.5, -35.0). **Vector** length 64.4, 9.85% of its response variance represented; |z| ≥ 3 in 833 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.7 | +12.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +7.4 | +9.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +7.3 | +13.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +7.2 | +15.7 |
|  | [[Selinexor (drug)]] 5 µM |  | +4.1 | +4.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.8 | +4.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.8 | +2.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.5 | +3.3 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.2 | +2.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.1 | +3.2 |
| fall | [[Belinostat (drug)]] 5 µM |  | -2.6 | -3.2 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -2.1 | -2.5 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.0 | -2.3 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.8 | -2.5 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.3 | -3.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -1.3 | -3.4 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | -1.2 | -2.1 |
|  | [[Irinotecan (hydrochloride) (drug)]] 5 µM |  | -1.2 | -1.9 |
|  | [[TAK-733 (drug)]] 0.05 µM |  | -1.1 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | protein disulfide isomerase family A member 3 pseudogene 1 |
| Locus type | pseudogene |
| Location | 1q21.1 — chr1:147,178,113-147,179,622 (+) |
| Ensembl biotype | transcribed_processed_pseudogene |
| Also known as | GRP58P; previously PDIA3P |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:4607](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4607) · Entrez [171423](https://www.ncbi.nlm.nih.gov/gene/171423) · Ensembl [ENSG00000180867](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000180867)

## Data

Gene col 11139: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11139); `tables/drug_effects.parquet` (15 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11139, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11139]; `tensor/DDL_lfc|DDL_z.npy` [11139]; `embed/gene_vectors.npy` [11139]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11139 or target_col == 11139). Every well: [[PDIA3P1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PDIA3P1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
