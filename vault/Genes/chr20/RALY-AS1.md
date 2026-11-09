---
symbol: "RALY-AS1"
type: "gene"
col: 16098
ensembl_id: "ENSG00000285230"
name: "RALY antisense RNA 1"
location: "20q11.22"
module: 26
arm: "+"
pooled_cpm: 2.33
n_lines_expressing: 50
n_dd_up: 24
n_dd_down: 3
n_dd_up_clean: 17
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/026"]
generated_by: "tahoemap"
---

# RALY-AS1

*RALY antisense RNA 1* — 20q11.22

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (7 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 10.0× (z +33.0, q 0e+00, up in 32 of 32 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (1 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.667× (z -4.1, q 0.021, down in 10 of 21 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 0.5 µM: 0.683× (z -3.9, q 0.028, down in 12 of 37 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Valdecoxib (drug)]] 0.5 µM in 1 line (A-427 0.0843×); [[Brimonidine (drug)]] 0.5 µM in 1 line (A-427 0.101×); [[Simotinib (drug)]] 5 µM in 1 line (SW1417 0.102×; ⚠ toxic); [[Vandetanib (drug)]] 0.5 µM in 1 line (SK-MEL-2 0.0799×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DUSP28]] (+0.71, fdr 7e-06), [[SIAH2-AS1]] (+0.70, fdr 7e-06), [[DPY19L3-DT]] (+0.68, fdr 7e-06); moves opposite to [[CAPN7]] (-0.58, fdr 2e-04), [[GPATCH11]] (-0.57, fdr 8e-05), [[RHOT1]] (-0.56, fdr 3e-05).
> It sits in the **+** arm of [[Module 026]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 7 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 16098.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **10.0×** | +33.0 | 0e+00 | 32/32 (SW480, SW1417, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **3.65×** | +12.6 | 5e-34 | 20/26 (MIA PaCa-2, SW480, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **2.37×** | +12.3 | 1e-32 | 18/44 (SW1417, A498, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM |  | **2.16×** | +11.0 | 6e-26 | 19/44 (SW480, PANC-1, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~16% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.72×** | +10.1 | 5e-22 | 33/46 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.72×** | +9.7 | 2e-20 | 18/30 (SW480, KATO III, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Auranofin (drug)]] 5 µM |  | **2.54×** | +9.4 | 4e-19 | 24/39 (HT-29, HEC-1-A, …) | top dose only | position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.56×** | +9.1 | 5e-18 | 1/3 (PANC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.88×** | +9.0 | 1e-17 | 17/34 (A498, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.22×** | +8.1 | 4e-14 | 22/42 (SW480, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.13×** | +7.1 | 9e-11 | 2/4 (SW1417, PANC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.92×** | +6.6 | 2e-09 | 5/13 (Hs 766T, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **1.72×** | +5.5 | 2e-06 | 12/44 (SW480, A-427, …) | rises with dose | cell-cycle shift (explains ~25% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.59×** | +4.7 | 1e-04 | 11/40 (MIA PaCa-2, A-427, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~51% of this change | **1.45×** | +3.6 | 0.012 | 5/14 (SW1417, J82, …) | rises with dose |  |
| [[Lidocaine (hydrochloride) (drug)]] 0.5 µM |  | **1.42×** | +3.5 | 0.016 | 1/29 (NCI-H1792) | inconsistent across doses |  |
| [[Triamcinolone (drug)]] 5 µM |  | **1.26×** | +3.3 | 0.028 | 3/42 (A498, MIA PaCa-2, …) | top dose only |  |
| [[Thymol (drug)]] 0.5 µM |  | **1.39×** | +3.3 | 0.028 | 2/23 (KATO III, MIA PaCa-2) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.39×** | +3.3 | 0.028 | 3/44 (SW480, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); position effect removed |
| [[Lidocaine (hydrochloride) (drug)]] 0.05 µM |  | **1.38×** | +3.2 | 0.032 | 1/16 (J82) | inconsistent across doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 2 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 16098.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Valdecoxib (drug)]] 0.5 µM in 1 line (A-427 0.0843×); [[Brimonidine (drug)]] 0.5 µM in 1 line (A-427 0.101×); [[Simotinib (drug)]] 5 µM in 1 line (SW1417 0.102×; ⚠ toxic); [[Vandetanib (drug)]] 0.5 µM in 1 line (SK-MEL-2 0.0799×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.667×** | -4.1 | 0.021 | 10/21 (HEC-1-A, J82, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.683×** | -3.9 | 0.028 | 12/37 (NCI-H1792, NCI-H2030, …) | two highest doses | cell-cycle shift (explains ~9% here) |
| [[Ranolazine (drug)]] 0.5 µM |  | **0.706×** | -3.5 | 0.073 | 6/42 (HepG2/C3A, MIA PaCa-2, …) | inconsistent across doses | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~22% of this change | 0.732× | -3.2 | 0.18 | 6/47 (A-427, C-33 A, …) | two highest doses | composition shift |
| [[Verapamil (drug)]] 0.05 µM |  | 0.716× | -3.2 | 0.18 | 8/39 (NCI-H1573, LOX-IMVI, …) | inconsistent across doses |  |
| [[Radotinib (drug)]] 5 µM |  | 0.812× | -3.0 | 0.23 | 9/41 (SHP-77, SW480, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.41 per unit of S-phase module lfc, -0.44 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 16098. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 5.72 | 0 | 2 | — | [[Valdecoxib (drug)]] 0.5 µM 0.0843× (z -10.0) |
| [[SW1417 (line)]] | alt | 6.57 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.14× (z +12.6) | [[Simotinib (drug)]] 5 µM 0.102× (z -9.0) ⚠ toxic |
| [[A-172 (line)]] | wt | 1.26 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 15.9× (z +8.9) | — |
| [[A498 (line)]] | wt | 2.02 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.98× (z +10.2) | — |
| [[CFPAC-1 (line)]] | alt | 1.59 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 20.4× (z +10.4) | — |
| [[HEC-1-A (line)]] | alt | 1.46 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 12.0× (z +9.4) | — |
| [[HOP62 (line)]] | alt | 1.07 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 12.8× (z +8.5) | — |
| [[HS-578T (line)]] | alt | 1.76 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 14.7× (z +9.1) | — |
| [[HT-29 (line)]] | alt | 2.35 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 11.9× (z +9.7) | — |
| [[J82 (line)]] | alt | 2.83 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.62× (z +8.8) | — |
| [[KATO III (line)]] | alt | 3.86 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.7× (z +11.5) | — |
| [[LoVo (line)]] | wt | 1.98 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 11.9× (z +10.7) | — |
| [[MIA PaCa-2 (line)]] | alt | 2.45 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 12.8× (z +9.9) | — |
| [[NCI-H2030 (line)]] | alt | 2.48 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.48× (z +8.5) | — |
| [[NCI-H460 (line)]] | wt | 1.49 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 11.6× (z +10.6) | — |
| [[PANC-1 (line)]] | alt | 2.59 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.24× (z +11.2) | — |
| [[SK-MEL-2 (line)]] | alt | 6.04 | 0 | 1 | — | [[Vandetanib (drug)]] 0.5 µM 0.0799× (z -8.8) |
| [[SNU-423 (line)]] | alt | 1.64 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 13.5× (z +9.0) | — |
| [[SW480 (line)]] | alt | 2.90 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.01× (z +12.7) | — |
| [[A549 (line)]] | wt | 1.83 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.81 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.89 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.01 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.29 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.60 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.56 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.05 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.90 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.35 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.74 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.52 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.01 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.58 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.69 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.04 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.26 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 1.78 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.27 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.35 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.44 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.45 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.96 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.25 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.51 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.70 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.84 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.38 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.82 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.60 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.18 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 16098), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DUSP28]] | +0.71 | +0.63 / +0.63 | both halves | 7e-06 |  |
| [[SIAH2-AS1]] | +0.70 | +0.64 / +0.64 | both halves | 7e-06 | same gene group |
| [[DPY19L3-DT]] | +0.68 | +0.59 / +0.59 | both halves | 7e-06 |  |
| [[HCG20]] | +0.68 | +0.50 / +0.56 | both halves | 1e-05 |  |
| [[SAXO1]] | +0.65 | +0.56 / +0.54 | both halves | 1e-05 |  |
| [[LINC00393]] | +0.65 | +0.52 / +0.58 | both halves | 1e-05 |  |
| [[MALINC1]] | +0.64 | +0.58 / +0.65 | both halves | 7e-06 |  |
| [[CCT6B]] | +0.64 | +0.58 / +0.49 | both halves | 1e-05 |  |
| [[LRP2BP]] | +0.64 | +0.47 / +0.51 | both halves | 2e-05 |  |
| [[PAXBP1-AS1]] | +0.64 | +0.53 / +0.59 | both halves | 1e-05 | same gene group |
| [[CCNT2-AS1]] | +0.63 | +0.58 / +0.52 | both halves | 1e-05 | same gene group |
| [[CPEB2-DT]] | +0.63 | +0.59 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CAPN7]] | -0.58 | -0.55 / -0.32 | both halves | 2e-04 |  |
| [[GPATCH11]] | -0.57 | -0.39 / -0.37 | both halves | 8e-05 |  |
| [[RHOT1]] | -0.56 | -0.54 / -0.46 | both halves | 3e-05 |  |
| [[COMMD2]] | -0.56 | -0.41 / -0.37 | both halves | 8e-05 |  |
| [[TTBK2]] | -0.54 | -0.27 / -0.38 | both halves | 3e-04 |  |
| [[VPS8]] | -0.54 | -0.46 / -0.30 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers RALY-AS1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.8% of all compounds | 0.028 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 026]]; 163 genes; this gene is in the **+** arm (projection on the module's main direction 0.483). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.40).
- **Nodal map** (x, y) = (12.1, 19.5); signed map (25.6, -2.2). **Vector** length 46.7, 5.53% of its response variance represented; |z| ≥ 3 in 1,062 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.9 | +33.0 |
|  | [[Selinexor (drug)]] 5 µM |  | +4.3 | +11.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.1 | +7.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.0 | +9.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.9 | +9.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.1 | +12.3 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.2 | +1.9 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +1.0 | +2.2 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.0 | +0.4 |
| fall | [[Brivudine (drug)]] 5 µM |  | -1.9 | -0.4 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.7 | -3.0 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -1.7 | +3.3 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.6 | -2.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~22% of this change | -1.5 | -3.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | -1.4 | -0.3 |
|  | [[Ipatasertib (drug)]] 5 µM |  | -1.2 | -1.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.1 | -0.3 |

## What is on record

|  |  |
|---|---|
| Name | RALY antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 20q11.22 — chr20:33,980,679-33,994,357 (-) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:50743](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:50743) · Entrez [101926888](https://www.ncbi.nlm.nih.gov/gene/101926888) · Ensembl [ENSG00000285230](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000285230)

## Data

Gene col 16098: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 16098); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 16098, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 16098]; `tensor/DDL_lfc|DDL_z.npy` [16098]; `embed/gene_vectors.npy` [16098]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 16098 or target_col == 16098). Every well: [[RALY-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RALY-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
