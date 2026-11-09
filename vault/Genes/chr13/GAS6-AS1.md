---
symbol: "GAS6-AS1"
type: "gene"
col: 13918
ensembl_id: "ENSG00000233695"
name: "GAS6 antisense RNA 1"
location: "13q34"
module: 62
arm: "+"
pooled_cpm: 5.91
n_lines_expressing: 34
n_dd_up: 23
n_dd_down: 1
n_dd_up_clean: 14
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 1
direction_downstream: 2
tags: ["gene", "module/062"]
generated_by: "tahoemap"
---

# GAS6-AS1

*GAS6 antisense RNA 1* — 13q34

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.75× (z +11.0, q 2e-25, up in 3 of 6 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.89× (z +10.2, q 5e-22, up in 11 of 24 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Adagrasib (drug)]] 0.05 µM: 0.902× (z -4.2, q 0.019, down in 9 of 32 measured lines) ⚠ position not correctable. The strongest without an alert is [[Ixazomib citrate (drug)]] 5 µM: 0.728× (z -3.6, q 0.080, down in 9 of 29 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (NCI-H1573 0.137×; ⚠ toxic; transcription drop); [[Digitoxin (drug)]] 5 µM in 1 line (SHP-77 0.239×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change); [[Digitoxin (drug)]] 0.5 µM in 1 line (LoVo 0.0692×; ⚠ cell-cycle shift, explains ~0% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (SHP-77 0.443×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PURPL]] (+0.67, fdr 3e-05), [[PTCHD4]] (+0.67, fdr 1e-05), [[PINCR]] (+0.63, fdr 3e-05); moves opposite to [[RAD54B]] (-0.46, fdr 1e-04), [[PHKA2]] (-0.44, fdr 2e-04), [[ORC3]] (-0.43, fdr 6e-05).
> It is in [[Module 062]], a single-armed module (p53 targets up).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); 2 go from it, the strongest it → [[FLG-AS1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 9 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13918.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.75×** | +11.0 | 2e-25 | 3/6 (A498, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.89×** | +10.2 | 5e-22 | 11/24 (AsPC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.05×** | +8.1 | 7e-14 | 3/14 (LS 180, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.61×** | +7.6 | 5e-12 | 12/30 (A498, A549, …) | rises with dose | position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.98×** | +7.1 | 1e-10 | 2/8 (A498, LOX-IMVI) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.47×** | +6.1 | 1e-07 | 11/30 (KATO III, LOX-IMVI, …) | rises with dose | position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.64×** | +5.6 | 2e-06 | 4/19 (A549, SNU-423, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.41×** | +5.4 | 4e-06 | 10/26 (COLO 205, SNU-423, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.61×** | +5.4 | 4e-06 | 9/28 (SNU-423, SK-MEL-2, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.63×** | +5.3 | 6e-06 | 5/18 (NCI-H460, LS 180, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.55×** | +4.9 | 5e-05 | 12/27 (A498, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.52×** | +4.7 | 1e-04 | 10/26 (LOX-IMVI, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.50×** | +4.6 | 2e-04 | 11/30 (NCI-H1573, AsPC-1, …) | rises with dose | position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.50×** | +4.4 | 4e-04 | 8/21 (A549, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.43×** | +3.9 | 0.004 | 8/26 (AsPC-1, A549, …) | inconsistent across doses | cell-cycle shift (explains ~19% here) |
| [[Epirubicin (hydrochloride) (drug)]] 0.05 µM |  | **1.45×** | +3.8 | 0.004 | 7/23 (LS 180, A-172, …) | inconsistent across doses | low cells (technical?) |
| [[Ponatinib (drug)]] 5 µM |  | **1.36×** | +3.4 | 0.019 | 9/30 (A549, A-172, …) | rises with dose |  |
| [[Bendamustine (drug)]] 5 µM |  | **1.36×** | +3.3 | 0.029 | 2/26 (SNU-423, A549) | top dose only |  |
| [[Selinexor (drug)]] 0.5 µM |  | **1.34×** | +3.3 | 0.032 | 7/27 (NCI-H460, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.34×** | +3.1 | 0.052 | 6/24 (KATO III, NCI-H23, …) | inconsistent across doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 13918.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (NCI-H1573 0.137×; ⚠ toxic; transcription drop); [[Digitoxin (drug)]] 5 µM in 1 line (SHP-77 0.239×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change); [[Digitoxin (drug)]] 0.5 µM in 1 line (LoVo 0.0692×; ⚠ cell-cycle shift, explains ~0% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (SHP-77 0.443×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.902× | -4.2 | 0.019 | 9/32 (NCI-H1573, NCI-H2030, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.728×** | -3.6 | 0.080 | 9/29 (C32, NCI-H23, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[(S)-Crizotinib (drug)]] 0.05 µM |  | 0.746× | -3.1 | 0.29 | 4/30 (SW 900, SW480, …) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | 0.765× | -3.1 | 0.29 | 7/31 (SHP-77, LOX-IMVI, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.24 per unit of S-phase module lfc, -0.24 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13918. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[COLO 205 (line)]] | alt | 14.5 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.97× (z +10.5) | — |
| [[SHP-77 (line)]] | alt | 87.4 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.239× (z -10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.443× (z -8.5) |
| [[LoVo (line)]] | wt | 3.00 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.0692× (z -9.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H1573 (line)]] | alt | 22.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.137× (z -11.9) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 15.4 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.298× (z -8.9) ⚠ cell-cycle shift, explains ~25% of this change |
| [[A-172 (line)]] | wt | 3.61 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 2.20 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 3.28 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.13 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.56 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 6.86 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 0.787 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.07 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 7.00 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.793 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 4.46 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.12 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.29 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.07 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.11 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 1.32 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 2.96 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.40 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.01 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.52 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.72 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 23.5 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 15.5 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.752 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.703 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 1.81 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.27 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 8.00 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.957 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 2.71 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.97 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.32 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 1.23 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 1.36 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.17 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.85 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 6.39 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 5.17 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.68 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.13 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 2.42 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.23 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.05 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 1.97 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13918), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PURPL]] | +0.67 | +0.44 / +0.70 | both halves | 3e-05 |  |
| [[PTCHD4]] | +0.67 | +0.54 / +0.67 | both halves | 1e-05 |  |
| [[PINCR]] | +0.63 | +0.43 / +0.67 | both halves | 3e-05 |  |
| [[BAX]] | +0.63 | +0.53 / +0.59 | both halves | 1e-05 |  |
| [[EDA2R]] | +0.61 | +0.42 / +0.61 | both halves | 4e-05 |  |
| [[ADAMTS7]] | +0.61 | +0.41 / +0.66 | both halves | 4e-05 |  |
| [[INSYN2A]] | +0.60 | +0.37 / +0.63 | both halves | 9e-05 |  |
| [[CDKN1A]] | +0.59 | +0.40 / +0.60 | both halves | 5e-05 |  |
| [[ACTA2]] | +0.59 | +0.49 / +0.58 | both halves | 1e-05 |  |
| [[GRIN2C]] | +0.58 | +0.45 / +0.59 | both halves | 3e-05 |  |
| [[SPATA18]] | +0.57 | +0.37 / +0.61 | both halves | 8e-05 |  |
| [[ZNF561-AS1]] | +0.57 | +0.49 / +0.55 | both halves | 1e-05 | same gene group |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RAD54B]] | -0.46 | -0.35 / -0.40 | both halves | 1e-04 |  |
| [[PHKA2]] | -0.44 | -0.41 / -0.32 | both halves | 2e-04 |  |
| [[ORC3]] | -0.43 | -0.38 / -0.39 | both halves | 6e-05 |  |
| [[MBD4]] | -0.42 | -0.33 / -0.39 | both halves | 1e-04 |  |
| [[BARD1]] | -0.42 | -0.33 / -0.44 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers GAS6-AS1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.8% of all compounds | 0.028 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FLG-AS1]] | B | GAS6-AS1 activity raises FLG-AS1's level | lines that do not express GAS6-AS1 (16) vs lines expressing it (34) | 2.50× lower at baseline in the lines without GAS6-AS1 | 0.049 | ⚠ within organs, on part of the lines; also absent: ECM1, LINC02055, LINC02220; maybe low, not absent |
| [[PINCR]] | B | GAS6-AS1 activity raises PINCR's level | lines that do not express GAS6-AS1 (16) vs lines expressing it (34) | 2.14× lower at baseline in the lines without GAS6-AS1 | 0.082 | ⚠ within organs, on part of the lines; also absent: ECM1, LINC02055, LINC02220; maybe low, not absent |

## Where it sits

- **Module**: [[Module 062]] — p53 targets up; 78 genes; every member is in the + arm (projection on the module's main direction 0.655). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.30; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-14.3, 37.3); signed map (43.5, -23.4). **Vector** length 50.4, 8.29% of its response variance represented; |z| ≥ 3 in 789 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.9 | +7.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.7 | +11.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.6 | +8.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | +4.2 | +4.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.9 | +6.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.8 | +7.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.5 | +5.4 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.8 | +2.3 |
|  | [[Amsacrine (drug)]] 5 µM |  | +1.7 | +2.8 |
| fall | [[Artesunate (drug)]] 0.5 µM |  | -1.7 | -0.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.5 | -1.0 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.2 | -2.1 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -1.2 | -1.7 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -1.2 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | GAS6 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 13q34 — chr13:113,815,630-113,845,744 (+) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:39826](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:39826) · Entrez [650669](https://www.ncbi.nlm.nih.gov/gene/650669) · Ensembl [ENSG00000233695](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000233695)

## Data

Gene col 13918: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13918); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13918, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13918]; `tensor/DDL_lfc|DDL_z.npy` [13918]; `embed/gene_vectors.npy` [13918]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13918 or target_col == 13918). Every well: [[GAS6-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GAS6-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
