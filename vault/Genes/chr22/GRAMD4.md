---
symbol: "GRAMD4"
type: "gene"
col: 1109
ensembl_id: "ENSG00000075240"
name: "GRAM domain containing 4"
location: "22q13.31"
module: 77
arm: "+"
pooled_cpm: 20.26
n_lines_expressing: 50
n_dd_up: 0
n_dd_down: 27
n_dd_up_clean: 0
n_dd_down_clean: 20
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/077"]
generated_by: "tahoemap"
---

# GRAMD4

*GRAM domain containing 4* — 22q13.31

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> Pooled over the cell lines (median), lowered significantly by 27 drug-doses (7 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.395× (z -24.8, q 0e+00, down in 44 of 46 measured lines).
> Its strongest partners by |cos| (91 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 9 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SSBP4]] (+0.65, fdr 2e-05), [[TNK2]] (+0.64, fdr 3e-05), [[BRF1]] (+0.64, fdr 1e-05); moves opposite to [[PCNX4-DT]] (-0.66, fdr 1e-04), [[PKN2-AS1]] (-0.65, fdr 2e-04), [[EIF1B-AS1]] (-0.64, fdr 1e-04).
> It sits in the **+** arm of [[Module 077]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 0 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1109.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | 1.19× | +3.2 | 0.35 | 9/46 (NCI-H460, SHP-77, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 0.5 µM |  | 1.18× | +3.2 | 0.35 | 6/47 (AN3 CA, A-427, …) | inconsistent across doses |  |
| [[Pexidartinib (hydrochloride) (drug)]] 5 µM |  | 1.18× | +3.1 | 0.35 | 8/47 (KATO III, A549, …) | top dose only | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 33 in all, 12 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 27 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1109.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.395×** | -24.8 | 0e+00 | 44/46 (C32, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.406×** | -24.1 | 0e+00 | 42/48 (PANC-1, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.401×** | -16.6 | 0e+00 | 41/46 (C32, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift; position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.441×** | -15.5 | 0e+00 | 38/48 (LS 180, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.444×** | -14.8 | 0e+00 | 41/46 (C32, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.496×** | -13.2 | 5e-38 | 37/47 (SHP-77, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | **0.512×** | -12.6 | 1e-34 | 36/46 (NCI-H460, LoVo, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.547×** | -11.4 | 3e-28 | 34/47 (C32, SHP-77, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.553×** | -10.7 | 5e-25 | 27/45 (C32, SW480, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.588×** | -10.0 | 9e-22 | 30/47 (C32, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **0.389×** | -9.3 | 7e-19 | 33/48 (KATO III, HS-578T, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~15% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.642×** | -8.4 | 3e-15 | 26/46 (PANC-1, SHP-77, …) | all doses, stronger at high dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.642×** | -8.0 | 4e-14 | 26/47 (C32, Panc 03.27, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.765×** | -7.1 | 5e-11 | 25/48 (HS-578T, Hs 766T, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~32% of this change | **0.691×** | -6.7 | 9e-10 | 24/45 (HepG2/C3A, C32, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.719×** | -6.2 | 2e-08 | 21/47 (SNU-423, LoVo, …) | two highest doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.743×** | -5.6 | 8e-07 | 17/47 (MIA PaCa-2, C32, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.746×** | -5.5 | 1e-06 | 21/47 (SHP-77, LS 180, …) | two highest doses | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.08 per unit of S-phase module lfc, -0.31 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1109. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SHP-77 (line)]] | alt | 201 | 0 | 14 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.147× (z -17.4) |
| [[C32 (line)]] | wt | 77.9 | 0 | 10 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.144× (z -19.5) |
| [[SW480 (line)]] | alt | 13.2 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.306× (z -13.5) |
| [[A549 (line)]] | wt | 22.2 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.170× (z -16.9) |
| [[NCI-H2030 (line)]] | alt | 17.9 | 0 | 5 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.201× (z -10.8) |
| [[PANC-1 (line)]] | alt | 18.8 | 0 | 5 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.216× (z -17.8) |
| [[HepG2_C3A (line)]] | wt | 29.3 | 0 | 4 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.172× (z -13.1) |
| [[HS-578T (line)]] | alt | 19.5 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.184× (z -15.5) |
| [[LoVo (line)]] | wt | 19.9 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.278× (z -14.9) |
| [[NCI-H2347 (line)]] | alt | 16.3 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.250× (z -13.8) |
| [[HT-29 (line)]] | alt | 18.2 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.196× (z -16.1) |
| [[KATO III (line)]] | alt | 29.0 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.160× (z -14.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.229× (z -11.4) |
| [[MIA PaCa-2 (line)]] | alt | 19.5 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.141× (z -16.7) |
| [[Panc 03.27 (line)]] | alt | 13.7 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.159× (z -14.4) |
| [[RKO (line)]] | wt | 19.2 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.145× (z -12.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.287× (z -11.1) |
| [[SW 900 (line)]] | alt | 19.8 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.239× (z -12.0) |
| [[COLO 205 (line)]] | alt | 18.4 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.222× (z -11.1) |
| [[HEC-1-A (line)]] | alt | 17.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.290× (z -12.6) |
| [[LOX-IMVI (line)]] | wt | 7.00 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.213× (z -9.8) |
| [[NCI-H23 (line)]] | alt | 15.2 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.147× (z -16.6) |
| [[SNU-423 (line)]] | alt | 16.8 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.240× (z -12.4) |
| [[SW1417 (line)]] | alt | 14.2 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.282× (z -12.3) |
| [[BT-474 (line)]] | alt | 29.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.246× (z -13.2) |
| [[CFPAC-1 (line)]] | alt | 9.55 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.357× (z -8.5) |
| [[CHP-212 (line)]] | wt | 31.3 | 0 | 1 | — | [[Vandetanib (drug)]] 0.5 µM 0.0696× (z -9.6) |
| [[J82 (line)]] | alt | 7.06 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.135× (z -8.7) |
| [[LS 180 (line)]] | wt | 24.9 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.216× (z -12.1) |
| [[NCI-H1573 (line)]] | alt | 18.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.112× (z -14.9) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[NCI-H460 (line)]] | wt | 8.75 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0724× (z -17.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change |
| [[RPMI-7951 (line)]] | alt | 9.50 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.0718× (z -10.6) |
| [[SK-MEL-2 (line)]] | alt | 11.3 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.133× (z -8.9) |
| [[SW48 (line)]] | wt | 21.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.236× (z -9.6) |
| [[A-172 (line)]] | wt | 15.1 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 13.3 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 14.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 23.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 9.30 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 25.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 7.76 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 23.0 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 8.08 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 16.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.24 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 25.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 26.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 18.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 12.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1109), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*42 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SSBP4]] | +0.65 | +0.71 / +0.48 | both halves | 2e-05 |  |
| [[TNK2]] | +0.64 | +0.58 / +0.44 | both halves | 3e-05 |  |
| [[BRF1]] | +0.64 | +0.57 / +0.50 | both halves | 1e-05 |  |
| [[RSAD1]] | +0.64 | +0.59 / +0.40 | both halves | 5e-05 |  |
| [[MAST3]] | +0.63 | +0.54 / +0.46 | both halves | 3e-05 |  |
| [[TMEM120B]] | +0.63 | +0.62 / +0.41 | both halves | 4e-05 |  |
| [[HDAC11]] | +0.63 | +0.56 / +0.43 | both halves | 4e-05 |  |
| [[MINK1]] | +0.62 | +0.61 / +0.47 | both halves | 2e-05 |  |
| [[POLRMT]] | +0.62 | +0.61 / +0.35 | both halves | 1e-04 |  |
| [[ST6GALNAC6]] | +0.61 | +0.61 / +0.39 | both halves | 5e-05 |  |
| [[CACNA1H]] | +0.61 | +0.57 / +0.51 | both halves | 1e-05 |  |
| [[TSNARE1]] | +0.60 | +0.54 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

*58 of its nearest partners move opposite, 9 of them with an alert (⚠; 9 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PCNX4-DT]] | -0.66 | -0.67 / -0.35 | both halves | 1e-04 |  |
| [[PKN2-AS1]] | -0.65 | -0.66 / -0.30 | both halves | 2e-04 |  |
| [[EIF1B-AS1]] | -0.64 | -0.64 / -0.35 | both halves | 1e-04 |  |
| [[RNPC3-DT]] | -0.64 | -0.62 / -0.22 | both halves | 6e-04 |  |
| [[CCDC90B-AS1]] | -0.64 | -0.65 / -0.24 | both halves | 5e-04 |  |
| [[MMADHC-DT]] | -0.63 | -0.66 / -0.24 | both halves | 5e-04 |  |
| [[CACNA2D1]] | -0.62 | -0.52 / -0.37 | both halves | 8e-05 |  |
| [[TMEM202-AS1]] | -0.62 | -0.64 / -0.22 | both halves | 6e-04 |  |
| [[SUCLG2-DT]] | -0.62 | -0.60 / -0.32 | both halves | 2e-04 |  |
| [[DDX6]] | -0.62 | -0.55 / -0.32 | both halves | 2e-04 |  |
| [[C11orf58]] | -0.61 | -0.66 / -0.27 | both halves | 3e-04 |  |
| [[RIPK2-DT]] | -0.61 | -0.66 / -0.33 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises GRAMD4's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.6% of all compounds | 0.041 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 077]]; 59 genes; this gene is in the **+** arm (projection on the module's main direction 0.682). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.44).
- **Nodal map** (x, y) = (8.0, 11.9); signed map (-40.6, -5.4). **Vector** length 78.9, 15.6% of its response variance represented; |z| ≥ 3 in 1,137 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.1 | +2.8 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +3.5 | +0.8 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +3.2 | +0.5 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +3.2 | +0.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.9 | +2.6 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.0 | +2.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.9 | +1.8 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | +1.6 | +0.6 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +1.4 | +0.2 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -4.7 | -16.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -4.6 | -24.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -4.1 | -14.8 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -3.6 | -10.0 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -3.3 | -10.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.1 | -7.1 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.8 | -11.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.6 | -1.2 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.4 | -1.4 |
|  | [[Cobimetinib (drug)]] 0.5 µM |  | -2.3 | +0.6 |

## What is on record

|  |  |
|---|---|
| Name | GRAM domain containing 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q13.31 — chr22:46,576,012-46,679,790 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0767, DIP |
| Gene groups (HGNC) | GRAM domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6IC98](https://www.uniprot.org/uniprotkb/Q6IC98) (GRAM domain-containing protein 4):

> Plays a role as a mediator of E2F1-induced apoptosis in the absence of p53/TP53. Plays a role as a mediator of E2F1-induced apoptosis in the absence of p53/TP53. Inhibits TLR9 response to nucelic acids and regulates TLR9-mediated innate immune response (By similarity).

**Summary**, from NCBI Gene [23151](https://www.ncbi.nlm.nih.gov/gene/23151):

> GRAMD4 is a mitochondrial effector of E2F1 (MIM 189971)-induced apoptosis (Stanelle et al., 2005 [PubMed 15565177]).[supplied by OMIM, Jan 2011]

**Accessions** — [HGNC:29113](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29113) · Entrez [23151](https://www.ncbi.nlm.nih.gov/gene/23151) · UniProt [Q6IC98](https://www.uniprot.org/uniprotkb/Q6IC98) · Ensembl [ENSG00000075240](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000075240)

## Data

Gene col 1109: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1109); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1109, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1109]; `tensor/DDL_lfc|DDL_z.npy` [1109]; `embed/gene_vectors.npy` [1109]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1109 or target_col == 1109). Every well: [[GRAMD4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GRAMD4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
