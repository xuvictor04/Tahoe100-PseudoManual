---
symbol: "SENP8"
type: "gene"
col: 9258
ensembl_id: "ENSG00000166192"
name: "SUMO peptidase family member, NEDD8 specific"
location: "15q23"
module: 15
arm: "+"
pooled_cpm: 3.5
n_lines_expressing: 50
n_dd_up: 19
n_dd_down: 5
n_dd_up_clean: 13
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/015"]
generated_by: "tahoemap"
---

# SENP8

*SUMO peptidase family member, NEDD8 specific* — 15q23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (6 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 4.14× (z +22.2, q 0e+00, up in 37 of 38 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (3 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 0.657× (z -4.7, q 0.001, down in 13 of 46 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 1 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Clofarabine (drug)]] 5 µM in 1 line (NCI-H2030 0.0697×); [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM in 1 line (HOP62 0.0939×); [[Orlistat (drug)]] 5 µM in 1 line (C32 0.0547×).
> Its strongest partners by |cos| (85 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 15 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[C12orf60]] (+0.77, fdr 1e-04), [[SMIM19]] (+0.77, fdr 1e-05), [[DDX59]] (+0.77, fdr 1e-05); moves opposite to [[CAMK2G]] (-0.67, fdr 1e-04), [[EDA]] (-0.62, fdr 2e-04), [[PACC1]] (-0.61, fdr 9e-05).
> It sits in the **+** arm of [[Module 015]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 6 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9258.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **4.14×** | +22.2 | 0e+00 | 37/38 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.64×** | +10.3 | 3e-22 | 22/34 (HOP62, PANC-1, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.26×** | +8.6 | 1e-15 | 22/37 (SW480, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.69×** | +8.1 | 5e-14 | 17/38 (NCI-H1573, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.89×** | +6.7 | 2e-09 | 12/21 (KATO III, HT-29, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.53×** | +6.6 | 5e-09 | 13/46 (NCI-H1573, LoVo, …) | rises with dose | low cells (technical?) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.52×** | +6.5 | 5e-09 | 17/47 (SW1417, HEC-1-A, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.72×** | +6.0 | 2e-07 | 15/36 (LoVo, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.79×** | +5.9 | 2e-07 | 2/7 (SNU-423, A498) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.57×** | +4.9 | 5e-05 | 16/45 (SW1417, LOX-IMVI, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.53×** | +4.7 | 1e-04 | 9/43 (PANC-1, SW1417, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.55×** | +4.6 | 2e-04 | 1/6 (A498) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM |  | **1.48×** | +4.3 | 8e-04 | 9/42 (NCI-H460, HOP62, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.42×** | +3.8 | 0.006 | 7/42 (LoVo, A-427, …) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.25×** | +3.3 | 0.043 | 1/47 (A498) | inconsistent across doses |  |
| [[Triamcinolone (drug)]] 5 µM |  | **1.22×** | +3.1 | 0.072 | 4/46 (C-33 A, PANC-1, …) | rises with dose |  |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | **1.31×** | +3.0 | 0.090 | 0/42 | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 3 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9258.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 1 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Clofarabine (drug)]] 5 µM in 1 line (NCI-H2030 0.0697×); [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM in 1 line (HOP62 0.0939×); [[Orlistat (drug)]] 5 µM in 1 line (C32 0.0547×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.657×** | -4.7 | 0.001 | 13/46 (HS-578T, RPMI-7951, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.678×** | -4.3 | 0.004 | 11/47 (PANC-1, SNU-423, …) | all doses, stronger at high dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~24% of this change | **0.723×** | -3.5 | 0.089 | 9/24 (LOX-IMVI, PANC-1, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.739×** | -3.4 | 0.096 | 10/44 (AsPC-1, PANC-1, …) | two highest doses |  |
| [[Lactate (calcium) (drug)]] 5 µM |  | **0.743×** | -3.3 | 0.099 | 2/47 (PANC-1, CHP-212) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.09 per unit of S-phase module lfc, -0.36 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9258. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 3.73 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.89× (z +8.7) | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM 0.0939× (z -9.2) |
| [[PANC-1 (line)]] | alt | 4.94 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.16× (z +10.5) | [[Docetaxel (drug)]] 0.05 µM 0.199× (z -8.5) ⚠ transcription drop; cell-cycle shift, would explain all of this change |
| [[A498 (line)]] | wt | 2.03 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.58× (z +8.7) | — |
| [[C32 (line)]] | wt | 3.97 | 0 | 1 | — | [[Orlistat (drug)]] 5 µM 0.0547× (z -8.6) |
| [[HEC-1-A (line)]] | alt | 2.95 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.66× (z +8.5) | — |
| [[LS 180 (line)]] | wt | 3.54 | 0 | 1 | — | [[Bendamustine (drug)]] 0.05 µM 0.0660× (z -8.6) |
| [[NCI-H2030 (line)]] | alt | 4.48 | 0 | 1 | — | [[Clofarabine (drug)]] 5 µM 0.0697× (z -9.9) |
| [[NCI-H460 (line)]] | wt | 2.82 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.24× (z +10.1) | — |
| [[SW1417 (line)]] | alt | 4.34 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.25× (z +9.7) | — |
| [[SW480 (line)]] | alt | 4.11 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.93× (z +9.2) | — |
| [[A-172 (line)]] | wt | 3.31 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 2.57 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.91 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.20 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.78 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.55 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.68 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.64 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.84 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.48 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.75 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.58 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.09 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.80 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.55 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.45 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.45 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.23 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 6.96 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 3.01 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.09 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.49 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.43 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 6.20 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.67 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.46 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.34 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.99 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.28 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.71 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.31 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.69 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.84 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.91 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.90 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 4.44 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.92 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.04 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.29 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.84 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9258), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 15 of them with an alert (⚠; 15 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[C12orf60]] | +0.77 | +0.85 / +0.35 | both halves | 1e-04 |  |
| [[SMIM19]] | +0.77 | +0.75 / +0.57 | both halves | 1e-05 |  |
| [[DDX59]] | +0.77 | +0.61 / +0.56 | both halves | 1e-05 |  |
| [[PNISR-AS1]] | +0.74 | +0.67 / +0.48 | both halves | 2e-05 |  |
| [[MFF-DT]] | +0.72 | +0.73 / +0.36 | both halves | 1e-04 |  |
| [[PBLD]] | +0.72 | +0.70 / +0.33 | both halves | 1e-04 |  |
| [[UBE3B]] | +0.72 | +0.75 / +0.35 | both halves | 1e-04 |  |
| [[TSTD3]] | +0.70 | +0.69 / +0.36 | both halves | 1e-04 |  |
| [[SEPTIN7-DT]] | +0.70 | +0.72 / +0.42 | both halves | 4e-05 |  |
| [[PKN2-AS1]] | +0.70 | +0.75 / +0.24 | both halves | 4e-04 |  |
| [[DICER1-AS1]] | +0.69 | +0.68 / +0.50 | both halves | 1e-05 |  |
| [[SEC24B-AS1]] | +0.69 | +0.57 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CAMK2G]] | -0.67 | -0.60 / -0.33 | both halves | 1e-04 |  |
| [[EDA]] | -0.62 | -0.53 / -0.30 | both halves | 2e-04 |  |
| [[PACC1]] | -0.61 | -0.55 / -0.36 | both halves | 9e-05 |  |
| [[CADM4]] | -0.61 | -0.31 / -0.44 | both halves | 2e-04 |  |
| [[NAA40]] | -0.61 | -0.41 / -0.48 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers SENP8's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.4% of all compounds | 0.015 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 015]]; 210 genes; this gene is in the **+** arm (projection on the module's main direction 0.654). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (2.0, 14.2); signed map (22.8, -14.2). **Vector** length 54.8, 6.78% of its response variance represented; |z| ≥ 3 in 1,102 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.8 | +22.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +3.6 | +10.3 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +2.8 | +8.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +2.8 | +6.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.7 | +6.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.5 | +3.8 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.4 | +2.2 |
|  | [[Triamcinolone (drug)]] 5 µM |  | +1.4 | +3.1 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.0 | +2.6 |
| fall | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -3.9 | -1.7 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.7 | -2.5 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -3.0 | +1.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.7 | -0.1 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.4 | +0.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.7 | -1.4 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.2 | -1.9 |
|  | [[Belinostat (drug)]] 0.05 µM |  | -1.1 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | SUMO peptidase family member, NEDD8 specific |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q23 — chr15:72,114,258-72,143,692 (+) |
| Ensembl biotype | protein_coding |
| Also known as | NEDP1, DEN1, HsT17512; previously PRSC2 |
| Gene groups (HGNC) | SUMO specific peptidases |
| Reactome | 3 pathways, smallest: UCH proteinases; Neddylation; Deubiquitination |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96LD8](https://www.uniprot.org/uniprotkb/Q96LD8) (Sentrin-specific protease 8):

> Protease that catalyzes two essential functions in the NEDD8 pathway: processing of full-length NEDD8 to its mature form and deconjugation of NEDD8 from targeted proteins such as cullins or p53.

**Summary**, from NCBI Gene [123228](https://www.ncbi.nlm.nih.gov/gene/123228):

> This gene encodes a cysteine protease that is a member of the sentrin-specific protease family. The encoded protein is involved in processing and deconjugation of the ubiquitin-like protein termed, neural precursor cell expressed developmentally downregulated 8. Alternate splicing results in multiple transcript variants.[provided by RefSeq, Oct 2009]

**Accessions** — [HGNC:22992](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:22992) · Entrez [123228](https://www.ncbi.nlm.nih.gov/gene/123228) · UniProt [Q96LD8](https://www.uniprot.org/uniprotkb/Q96LD8) · Ensembl [ENSG00000166192](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000166192)

## Data

Gene col 9258: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9258); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9258, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9258]; `tensor/DDL_lfc|DDL_z.npy` [9258]; `embed/gene_vectors.npy` [9258]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9258 or target_col == 9258). Every well: [[SENP8 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SENP8.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
