---
symbol: "MFF-DT"
type: "gene"
col: 14079
ensembl_id: "ENSG00000236432"
name: "MFF divergent transcript"
location: "2q36.3"
module: 23
arm: "+"
pooled_cpm: 6.54
n_lines_expressing: 50
n_dd_up: 17
n_dd_down: 13
n_dd_up_clean: 11
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 5
direction_downstream: 0
tags: ["gene", "module/023"]
generated_by: "tahoemap"
---

# MFF-DT

*MFF divergent transcript* — 2q36.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (6 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.86× (z +19.3, q 0e+00, up in 39 of 41 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (5 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.407× (z -11.7, q 1e-28, down in 38 of 47 measured lines).
> Its strongest partners by |cos| (94 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 6 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TMEM202-AS1]] (+0.84, fdr 3e-05), [[ATE1OSP]] (+0.83, fdr 1e-05), [[PBLD]] (+0.83, fdr 4e-05); moves opposite to [[STUB1]] (-0.72, fdr 7e-04), [[PAFAH1B3]] (-0.72, fdr 8e-05), [[FCHO1]] (-0.70, fdr 2e-04).
> It sits in the **+** arm of [[Module 023]].
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[KIF21B]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 6 with an alert ⚠. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14079.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.86×** | +19.3 | 0e+00 | 39/41 (HEC-1-A, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.62×** | +8.9 | 2e-16 | 23/47 (HEC-1-A, NCI-H2030, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.94×** | +7.7 | 3e-12 | 24/39 (A498, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.77×** | +6.8 | 1e-09 | 8/19 (NCI-H2030, MIA PaCa-2, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.41×** | +6.3 | 3e-08 | 17/43 (NCI-H2030, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.45×** | +4.8 | 1e-04 | 16/43 (NCI-H2030, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.43×** | +4.7 | 2e-04 | 17/44 (NCI-H23, A-427, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~74% of this change | **1.28×** | +4.5 | 5e-04 | 13/48 (AsPC-1, LS 180, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~87% of this change | **1.31×** | +3.5 | 0.031 | 6/44 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **1.33×** | +3.5 | 0.031 | 5/48 (LoVo, SW480, …) | all doses, flat | noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.34×** | +3.4 | 0.034 | 9/30 (NCI-H1573, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~16% of this change | **1.29×** | +3.3 | 0.039 | 5/46 (A549, A-427, …) | rises with dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.28×** | +3.2 | 0.059 | 7/44 (NCI-H23, KATO III, …) | rises with dose |  |
| [[Binimetinib (drug)]] 0.05 µM |  | 1.19× | +3.2 | 0.059 | 13/48 (C32, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **1.30×** | +3.1 | 0.064 | 4/47 (NCI-H23, LoVo, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.30×** | +3.1 | 0.078 | 3/44 (PANC-1, SW480, …) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.26×** | +3.0 | 0.078 | 6/44 (hTERT-HPNE, A549, …) | inconsistent across doses |  |
| [[Lactate (calcium) (drug)]] 0.5 µM |  | **1.26×** | +3.0 | 0.089 | 4/45 (SNU-423, A-172, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 5 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14079.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.407×** | -11.7 | 1e-28 | 38/47 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.437×** | -10.8 | 2e-24 | 36/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.471×** | -9.8 | 3e-20 | 36/45 (NCI-H460, PANC-1, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.586×** | -6.9 | 5e-10 | 24/48 (NCI-H460, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | **0.610×** | -6.4 | 2e-08 | 21/40 (LOX-IMVI, PANC-1, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.617×** | -6.3 | 3e-08 | 21/42 (NCI-H2030, LoVo, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.629×** | -6.0 | 1e-07 | 21/46 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~38% of this change | **0.639×** | -5.2 | 1e-05 | 18/36 (A549, HepG2/C3A, …) | top dose only |  |
| [[Brivudine (drug)]] 5 µM |  | **0.515×** | -4.5 | 4e-04 | 6/46 (SW48, SNU-423, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.726×** | -4.2 | 0.002 | 15/45 (CFPAC-1, NCI-H460, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **0.804×** | -4.0 | 0.003 | 12/47 (NCI-H460, NCI-H1573, …) | top dose only |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **0.746×** | -3.8 | 0.006 | 13/45 (LS 180, RPMI-7951, …) | inconsistent across doses |  |
| [[Clopidogrel (drug)]] 0.05 µM |  | **0.784×** | -3.2 | 0.068 | 5/46 (AsPC-1, RPMI-7951, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.31 per unit of S-phase module lfc, -0.26 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14079. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 16.6 | 0 | 4 (3 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.198× (z -12.1) |
| [[PANC-1 (line)]] | alt | 7.50 | 1 | 3 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.70× (z +8.7) | [[Dinaciclib (drug)]] 5 µM 0.128× (z -11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H2030 (line)]] | alt | 7.73 | 1 | 2 | [[Homoharringtonine (drug)]] 5 µM 5.79× (z +11.9) | [[Bosentan (hydrate) (drug)]] 5 µM 0.107× (z -9.6) |
| [[SK-MEL-2 (line)]] | alt | 9.79 | 0 | 2 (1 ⚠) | — | [[Bortezomib (drug)]] 0.05 µM 0.0924× (z -9.7) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.119× (z -9.1) |
| [[A-172 (line)]] | wt | 7.18 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.144× (z -8.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A549 (line)]] | wt | 6.89 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0988× (z -9.2) ⚠ toxic; cell-cycle shift, explains ~38% of this change |
| [[H4 (line)]] | wt | 10.3 | 0 | 1 | — | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM 0.0950× (z -8.5) |
| [[HEC-1-A (line)]] | alt | 6.66 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.46× (z +9.0) | — |
| [[HepG2_C3A (line)]] | wt | 15.3 | 0 | 1 | — | [[Monocrotaline (drug)]] 0.05 µM 0.113× (z -8.8) |
| [[LOX-IMVI (line)]] | wt | 6.41 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0840× (z -11.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change |
| [[NCI-H1573 (line)]] | alt | 12.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.190× (z -8.9) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 3.85 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.107× (z -10.9) |
| [[A-427 (line)]] | wt | 3.19 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 6.30 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.14 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.62 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.63 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 7.57 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 15.2 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.61 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 7.37 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.55 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 7.92 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 3.06 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.86 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 6.61 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 4.17 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.49 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 4.82 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 5.00 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 4.49 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.92 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 5.97 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 7.99 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.02 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.58 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.48 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.39 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.32 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 4.85 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 8.03 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.63 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 8.16 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 6.82 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 8.76 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.83 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 4.23 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.49 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14079), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 6 of them with an alert (⚠; 6 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM202-AS1]] | +0.84 | +0.79 / +0.43 | both halves | 3e-05 |  |
| [[ATE1OSP]] | +0.83 | +0.77 / +0.51 | both halves | 1e-05 |  |
| [[PBLD]] | +0.83 | +0.73 / +0.42 | both halves | 4e-05 |  |
| [[OXA1L-DT]] | +0.82 | +0.77 / +0.44 | both halves | 3e-05 | same gene group |
| [[SEPTIN7-DT]] | +0.81 | +0.79 / +0.37 | both halves | 8e-05 | same gene group |
| [[ERCC6L2-AS1]] | +0.81 | +0.75 / +0.34 | both halves | 1e-04 |  |
| [[THBS4]] | +0.80 | +0.76 / +0.51 | both halves | 1e-05 |  |
| [[MAILR]] | +0.80 | +0.75 / +0.39 | both halves | 6e-05 |  |
| [[CHD1-DT]] | +0.79 | +0.74 / +0.37 | both halves | 8e-05 | same gene group |
| [[PNISR-AS1]] | +0.79 | +0.62 / +0.57 | both halves | 1e-05 |  |
| [[PKN2-AS1]] | +0.79 | +0.70 / +0.37 | both halves | 8e-05 |  |
| [[MAD2L1-DT]] | +0.79 | +0.71 / +0.37 | both halves | 9e-05 | same gene group |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[STUB1]] | -0.72 | -0.42 / -0.21 | both halves | 7e-04 |  |
| [[PAFAH1B3]] | -0.72 | -0.49 / -0.37 | both halves | 8e-05 |  |
| [[FCHO1]] | -0.70 | -0.55 / -0.29 | both halves | 2e-04 |  |
| [[KCTD17]] | -0.70 | -0.48 / -0.38 | both halves | 7e-05 |  |
| [[GPRIN1]] | -0.70 | -0.46 / -0.43 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KIF21B]] | B | KIF21B activity lowers MFF-DT's level | lines that do not express KIF21B (11) vs lines expressing it (39) | 1.47× higher at baseline in the lines without KIF21B | 0.006 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[TSPAN33]] | B | TSPAN33 activity raises MFF-DT's level | lines that do not express TSPAN33 (12) vs lines expressing it (38) | 1.29× lower at baseline in the lines without TSPAN33 | 0.031 | ⚠ within organs, on part of the lines; also absent: SRCIN1, CRACD, GNAZ; maybe low, not absent |
| [[SUCLG2-DT]] | B | SUCLG2-DT activity raises MFF-DT's level | lines that do not express SUCLG2-DT (7) vs lines expressing it (43) | 1.58× lower at baseline in the lines without SUCLG2-DT | 0.069 | ⚠ within organs, on part of the lines; also absent: TMCC2, DRAM1, ELK3; maybe low, not absent |
| [[TMEM92]] | B | TMEM92 activity lowers MFF-DT's level | lines that do not express TMEM92 (22) vs lines expressing it (28) | 1.31× higher at baseline in the lines without TMEM92 | 0.075 | ⚠ within organs, on part of the lines; also absent: ARL14, LINC01589, TNFSF10 |
| [[TOP2A]] | B | TOP2A activity lowers MFF-DT's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Idarubicin, Mitoxantrone) | 60% of the class's compounds vs 3.4% of all compounds | 0.095 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 023]]; 179 genes; this gene is in the **+** arm (projection on the module's main direction 0.893). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.34).
- **Nodal map** (x, y) = (4.0, 15.7); signed map (24.9, -9.2). **Vector** length 76.2, 13.0% of its response variance represented; |z| ≥ 3 in 1,119 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +8.1 | +19.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.4 | +4.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.3 | +4.7 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +4.3 | +7.7 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.3 | +6.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.0 | +8.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.2 | +2.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.7 | +2.9 |
|  | [[Triamcinolone (drug)]] 5 µM |  | +1.4 | +1.5 |
| fall | [[Belinostat (drug)]] 5 µM |  | -6.2 | -11.7 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -5.3 | -6.9 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | -5.1 | -9.8 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | -5.1 | -10.8 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -4.8 | -6.3 |
|  | [[Brivudine (drug)]] 5 µM |  | -3.4 | -4.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.3 | -4.0 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.2 | -1.7 |
|  | [[Belinostat (drug)]] 0.05 µM |  | -1.2 | -1.5 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | -1.0 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | MFF divergent transcript |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 2q36.3 — chr2:227,221,052-227,325,711 (-) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Divergent transcripts |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:41067](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:41067) · Entrez [654841](https://www.ncbi.nlm.nih.gov/gene/654841) · Ensembl [ENSG00000236432](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000236432)

## Data

Gene col 14079: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14079); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14079, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14079]; `tensor/DDL_lfc|DDL_z.npy` [14079]; `embed/gene_vectors.npy` [14079]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14079 or target_col == 14079). Every well: [[MFF-DT — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MFF-DT.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
