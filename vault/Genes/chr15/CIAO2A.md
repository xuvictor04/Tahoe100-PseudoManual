---
symbol: "CIAO2A"
type: "gene"
col: 9359
ensembl_id: "ENSG00000166797"
name: "cytosolic iron-sulfur assembly component 2A"
location: "15q22.31"
module: 29
arm: "+"
pooled_cpm: 23.85
n_lines_expressing: 50
n_dd_up: 16
n_dd_down: 5
n_dd_up_clean: 8
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/029"]
generated_by: "tahoemap"
---

# CIAO2A

*cytosolic iron-sulfur assembly component 2A* — 15q22.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.67× (z +14.3, q 8e-44, up in 37 of 42 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.82× (z +12.7, q 3e-34, up in 42 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.652× (z -9.0, q 1e-16, down in 37 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TMEM68]] (+0.66, fdr 1e-05), [[TIAL1]] (+0.66, fdr 1e-05), [[DRAM2]] (+0.64, fdr 7e-06); moves opposite to [[IER2]] (-0.66, fdr 1e-05), [[MIDN]] (-0.64, fdr 1e-05), [[EGR1]] (-0.59, fdr 1e-05).
> It sits in the **+** arm of [[Module 029]] (Neutrophil degranulation).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[EGR3]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 8 with an alert ⚠. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9359.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.67×** | +14.3 | 8e-44 | 37/42 (PANC-1, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.82×** | +12.7 | 3e-34 | 42/48 (A549, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.25×** | +11.2 | 6e-27 | 29/34 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.54×** | +9.1 | 9e-18 | 39/48 (J82, NCI-H2347, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.73×** | +7.6 | 4e-12 | 33/45 (NCI-H2030, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.64×** | +6.8 | 9e-10 | 33/48 (NCI-H23, NCI-H460, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.61×** | +6.6 | 5e-09 | 27/38 (KATO III, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.59×** | +6.4 | 1e-08 | 29/47 (SK-MEL-2, A-427, …) | top dose only | cell-cycle shift (explains ~17% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.48×** | +5.8 | 3e-07 | 29/45 (RPMI-7951, HOP62, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~12% here); position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.40×** | +4.7 | 2e-04 | 22/47 (LoVo, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~21% here) |
| [[Selinexor (drug)]] 0.5 µM |  | **1.27×** | +3.6 | 0.015 | 20/48 (CHP-212, COLO 205, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **1.25×** | +3.2 | 0.055 | 15/47 (NCI-H460, SW1417, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | **1.24×** | +3.2 | 0.055 | 15/47 (PANC-1, RPMI-7951, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.23×** | +3.1 | 0.080 | 9/48 (A549, SW480, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.23×** | +3.1 | 0.086 | 12/48 (SNU-423, HOP62, …) | inconsistent across doses |  |
| [[Sulfatinib (drug)]] 5 µM |  | **1.24×** | +3.0 | 0.086 | 11/47 (A498, A549, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 1 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 9359.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.652×** | -9.0 | 1e-16 | 37/47 (NCI-H23, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.670×** | -6.0 | 7e-07 | 31/47 (A498, SNU-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.749×** | -4.3 | 0.003 | 20/48 (SHP-77, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.633×** | -3.6 | 0.050 | 15/48 (SW480, NCI-H2030, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled); position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **0.781×** | -3.4 | 0.069 | 13/47 (COLO 205, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~17% of this change | 0.792× | -3.2 | 0.12 | 12/47 (SNU-1, RPMI-7951, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.21 per unit of S-phase module lfc, +0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9359. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 22.7 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 4.10× (z +11.4) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.507× (z -8.5) |
| [[A549 (line)]] | wt | 28.8 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.11× (z +12.1) | — |
| [[KATO III (line)]] | alt | 40.7 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.96× (z +10.0) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.511× (z -8.9) |
| [[NCI-H1792 (line)]] | alt | 21.8 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.29× (z +10.2) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.91× (z +9.4) | — |
| [[NCI-H23 (line)]] | alt | 20.0 | 1 | 1 | [[Epirubicin (hydrochloride) (drug)]] 5 µM 4.14× (z +8.5) | [[Homoharringtonine (drug)]] 5 µM 0.209× (z -14.2) |
| [[PANC-1 (line)]] | alt | 27.4 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.57× (z +11.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.516× (z -8.9) |
| [[SK-MEL-2 (line)]] | alt | 25.7 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.61× (z +8.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.244× (z -14.0) |
| [[SW480 (line)]] | alt | 23.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.87× (z +12.7) ⚠ toxic; transcription drop | — |
| [[A498 (line)]] | wt | 33.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.09× (z +8.7) | — |
| [[C32 (line)]] | wt | 23.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.97× (z +8.6) ⚠ toxic; transcription drop | — |
| [[COLO 205 (line)]] | alt | 29.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.314× (z -9.1) |
| [[HepG2_C3A (line)]] | wt | 20.7 | 0 | 1 | — | [[Naproxen (drug)]] 0.05 µM 0.167× (z -8.5) |
| [[MIA PaCa-2 (line)]] | alt | 20.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.86× (z +8.6) ⚠ toxic; transcription drop | — |
| [[NCI-H2030 (line)]] | alt | 34.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.02× (z +8.6) | — |
| [[SNU-1 (line)]] | wt | 17.1 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.107× (z -9.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 21.9 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 17.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 25.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 21.2 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 21.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 28.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 24.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 24.4 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 26.9 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 16.1 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 26.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 17.9 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 19.8 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 26.5 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 19.6 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 28.1 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 20.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 25.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 22.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 22.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 26.5 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 23.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 29.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 38.3 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 20.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 36.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 26.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 24.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9359), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*72 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM68]] | +0.66 | +0.51 / +0.66 | both halves | 1e-05 |  |
| [[TIAL1]] | +0.66 | +0.52 / +0.62 | both halves | 1e-05 |  |
| [[DRAM2]] | +0.64 | +0.60 / +0.60 | both halves | 7e-06 |  |
| [[BMPR1A]] | +0.63 | +0.56 / +0.54 | both halves | 1e-05 |  |
| [[TMEM94]] | +0.63 | +0.51 / +0.59 | both halves | 1e-05 |  |
| [[NNT]] | +0.62 | +0.56 / +0.53 | both halves | 1e-05 |  |
| [[PCMTD1]] | +0.62 | +0.57 / +0.51 | both halves | 1e-05 |  |
| [[TMED8]] | +0.62 | +0.57 / +0.59 | both halves | 8e-06 |  |
| [[STRADB]] | +0.60 | +0.55 / +0.49 | both halves | 1e-05 |  |
| [[DERA]] | +0.59 | +0.53 / +0.49 | both halves | 1e-05 |  |
| [[SDHAF4]] | +0.59 | +0.43 / +0.54 | both halves | 3e-05 |  |
| [[SLC18B1]] | +0.58 | +0.61 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*28 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IER2]] | -0.66 | -0.68 / -0.54 | both halves | 1e-05 |  |
| [[MIDN]] | -0.64 | -0.63 / -0.55 | both halves | 1e-05 |  |
| [[EGR1]] | -0.59 | -0.61 / -0.50 | both halves | 1e-05 |  |
| [[PPP1R10]] | -0.59 | -0.65 / -0.63 | both halves | 7e-06 |  |
| [[TNFRSF12A]] | -0.58 | -0.59 / -0.57 | both halves | 9e-06 |  |
| [[ZNF274]] | -0.58 | -0.63 / -0.57 | both halves | 1e-05 |  |
| [[KLF2]] | -0.57 | -0.50 / -0.41 | both halves | 4e-05 |  |
| [[CCDC57]] | -0.57 | -0.54 / -0.46 | both halves | 2e-05 |  |
| [[SETX]] | -0.57 | -0.51 / -0.59 | both halves | 1e-05 |  |
| [[CSRNP1]] | -0.57 | -0.57 / -0.49 | both halves | 1e-05 |  |
| [[PMEPA1]] | -0.56 | -0.47 / -0.58 | both halves | 2e-05 |  |
| [[CHRNA10]] | -0.56 | -0.55 / -0.46 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EGR3]] | B | EGR3 activity lowers CIAO2A's level | lines that do not express EGR3 (9) vs lines expressing it (41) | 1.38× higher at baseline in the lines without EGR3 | 0.024 | ⚠ within organs, on part of the lines; also absent: ENSG00000261026 |
| [[TOP2A]] | B | TOP2A activity lowers CIAO2A's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 3.1% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 029]] — Neutrophil degranulation; 148 genes; this gene is in the **+** arm (projection on the module's main direction 0.588). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (-13.2, 15.8); signed map (-30.0, -19.2). **Vector** length 87.9, 20.0% of its response variance represented; |z| ≥ 3 in 780 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +7.9 | +9.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.8 | +12.7 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +6.1 | +6.4 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +5.5 | +6.8 |
|  | [[Selinexor (drug)]] 0.5 µM |  | +4.5 | +3.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.9 | +3.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.9 | +2.5 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +2.4 | +2.1 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +2.0 | +0.7 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.8 | +0.5 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -5.6 | -9.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -5.0 | -6.0 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.8 | -2.0 |
|  | [[Panobinostat (drug)]] 5 µM |  | -3.7 | -4.3 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.9 | -0.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.6 | -1.5 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.6 | -1.8 |
|  | [[Filgotinib (drug)]] 5 µM |  | -1.6 | -1.0 |
|  | [[Sivelestat (sodium tetrahydrate) (drug)]] 5 µM |  | -1.5 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | cytosolic iron-sulfur assembly component 2A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q22.31 — chr15:64,072,565-64,094,262 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ22875, CIA2A; previously FAM96A |
| Gene groups (HGNC) | Cytosolic iron-sulfur assembly components |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H5X1](https://www.uniprot.org/uniprotkb/Q9H5X1) (Cytosolic iron-sulfur assembly component 2A):

> Component of the cytosolic iron-sulfur protein assembly (CIA) complex, a multiprotein complex that mediates the incorporation of iron-sulfur cluster into extramitochondrial Fe/S proteins. As a CIA complex component and in collaboration with CIAO1 specifically matures ACO1 and stabilizes IREB2, connecting cytosolic iron-sulfur protein maturation with cellular iron regulation. May play a role in chromosome segregation through establishment of sister chromatid cohesion. May induce apoptosis in …

**Summary**, from NCBI Gene [84191](https://www.ncbi.nlm.nih.gov/gene/84191):

> Predicted to enable metal ion binding activity. Involved in iron-sulfur cluster assembly and protein maturation. Located in cytosol and nucleoplasm. Part of cytosolic [4Fe-4S] assembly targeting complex. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:26235](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26235) · Entrez [84191](https://www.ncbi.nlm.nih.gov/gene/84191) · UniProt [Q9H5X1](https://www.uniprot.org/uniprotkb/Q9H5X1) · Ensembl [ENSG00000166797](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000166797)

## Data

Gene col 9359: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9359); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9359, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9359]; `tensor/DDL_lfc|DDL_z.npy` [9359]; `embed/gene_vectors.npy` [9359]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9359 or target_col == 9359). Every well: [[CIAO2A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CIAO2A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
