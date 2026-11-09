---
symbol: "LSM11"
type: "gene"
col: 7924
ensembl_id: "ENSG00000155858"
name: "LSM11, U7 small nuclear RNA associated"
location: "5q33.3"
module: 51
arm: "-"
pooled_cpm: 13.62
n_lines_expressing: 50
n_dd_up: 1
n_dd_down: 18
n_dd_up_clean: 0
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/051"]
generated_by: "tahoemap"
---

# LSM11

*LSM11, U7 small nuclear RNA associated* — 5q33.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 5 µM: 1.33× (z +5.4, q 5e-05, up in 16 of 41 measured lines) ⚠ toxic.
> Pooled over the cell lines (median), lowered significantly by 18 drug-doses (6 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 0.456× (z -14.6, q 3e-45, down in 35 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SMYD4]] (+0.60, fdr 1e-05), [[SCAI]] (+0.57, fdr 3e-05), [[SPATA33]] (+0.57, fdr 3e-05); moves opposite to [[DAB1]] (-0.60, fdr 1e-05), [[ALCAM]] (-0.57, fdr 4e-05), [[TRIP12]] (-0.56, fdr 4e-05).
> It sits in the **-** arm of [[Module 051]] (Chromatin modifying enzymes).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[FGD1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 2 with an alert ⚠. 1 of them raises it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7924.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.33×** | +5.4 | 5e-05 | 16/41 (SW480, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~0% of this change | 1.20× | +3.5 | 0.091 | 13/42 (RPMI-7951, NCI-H2030, …) | inconsistent across doses | low cells (technical?) |
| [[Lidocaine (hydrochloride) (drug)]] 0.05 µM |  | 1.20× | +3.5 | 0.091 | 12/43 (Panc 03.27, KATO III, …) | inconsistent across doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 11 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 18 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7924.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **0.456×** | -14.6 | 3e-45 | 35/48 (HOP62, A-172, …) | rises with dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.642×** | -12.1 | 4e-31 | 29/47 (HEC-1-A, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~6% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.417×** | -8.8 | 2e-16 | 28/48 (Panc 03.27, HS-578T, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~3% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.689×** | -6.9 | 5e-10 | 25/44 (RPMI-7951, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.696×** | -6.7 | 2e-09 | 24/45 (A-172, HS-578T, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.708×** | -6.6 | 3e-09 | 23/39 (NCI-H2030, AsPC-1, …) | two highest doses | cell-cycle shift (explains ~19% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.735×** | -5.7 | 8e-07 | 13/26 (SW480, A-172, …) | two highest doses | cell-cycle shift (explains ~18% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **0.568×** | -5.7 | 8e-07 | 17/43 (HOP62, LoVo, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM |  | **0.746×** | -5.6 | 9e-07 | 20/48 (HEC-1-A, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.812×** | -5.6 | 9e-07 | 19/48 (HEC-1-A, hTERT-HPNE, …) | rises with dose | position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.825×** | -5.2 | 8e-06 | 12/48 (NCI-H2347, A-172, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.774×** | -4.9 | 4e-05 | 13/47 (BT-474, NCI-H460, …) | two highest doses |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.787×** | -4.6 | 2e-04 | 12/47 (HOP62, C32, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~15% of this change | **0.792×** | -4.5 | 3e-04 | 13/48 (NCI-H1573, PANC-1, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~12% of this change | **0.794×** | -4.4 | 4e-04 | 11/47 (HT-29, LOX-IMVI, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.815×** | -3.9 | 0.003 | 10/47 (NCI-H661, SW1417, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 5 µM |  | 0.847× | -3.1 | 0.053 | 9/47 (HOP62, NCI-H2030, …) | rises with dose |  |
| [[Belumosudil (drug)]] 5 µM |  | 0.856× | -2.9 | 0.096 | 9/46 (AN3 CA, NCI-H1792, …) | top dose only |  |
| [[Trametinib (drug)]] 0.5 µM |  | 0.882× | -2.8 | 0.098 | 9/47 (HOP62, LoVo, …) | inconsistent across doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.06 per unit of S-phase module lfc, -0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7924. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 21.6 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.143× (z -13.6) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.247× (z -9.8) |
| [[A498 (line)]] | wt | 10.7 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.186× (z -12.1) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.356× (z -10.9) |
| [[AsPC-1 (line)]] | alt | 9.40 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.235× (z -11.0) |
| [[HEC-1-A (line)]] | alt | 26.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.434× (z -11.7) |
| [[NCI-H2347 (line)]] | alt | 15.7 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.314× (z -8.6) |
| [[NCI-H460 (line)]] | wt | 13.4 | 0 | 2 (1 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.345× (z -9.0) ⚠ cell-cycle shift, explains ~16% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.340× (z -8.8) |
| [[SNU-423 (line)]] | alt | 20.8 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.181× (z -11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change |
| [[CFPAC-1 (line)]] | alt | 12.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.337× (z -9.7) |
| [[HOP62 (line)]] | alt | 16.6 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.225× (z -10.5) |
| [[HS-578T (line)]] | alt | 15.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0689× (z -15.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change |
| [[J82 (line)]] | alt | 13.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0856× (z -14.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change |
| [[LOX-IMVI (line)]] | wt | 13.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.244× (z -8.6) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 11.5 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.179× (z -8.8) |
| [[NCI-H2030 (line)]] | alt | 11.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.239× (z -9.1) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 18.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.350× (z -9.7) |
| [[PANC-1 (line)]] | alt | 8.83 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.261× (z -9.1) |
| [[RPMI-7951 (line)]] | alt | 15.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.136× (z -9.7) |
| [[SHP-77 (line)]] | alt | 11.5 | 0 | 1 | — | [[Medroxyprogesterone acetate (drug)]] 0.5 µM 0.103× (z -10.9) |
| [[SK-MEL-2 (line)]] | alt | 25.9 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0859× (z -15.4) ⚠ cell-cycle shift, explains ~11% of this change |
| [[SW480 (line)]] | alt | 13.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.162× (z -15.3) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 13.3 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 12.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 27.8 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 5.65 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 11.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 17.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 8.54 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 9.34 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 13.2 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 15.0 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 12.8 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 8.35 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 18.6 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 13.1 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 8.62 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 9.74 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 8.00 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.81 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 14.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 12.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 6.11 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 16.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7924), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*61 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SMYD4]] | +0.60 | +0.52 / +0.57 | both halves | 1e-05 |  |
| [[SCAI]] | +0.57 | +0.55 / +0.45 | both halves | 3e-05 |  |
| [[SPATA33]] | +0.57 | +0.44 / +0.56 | both halves | 3e-05 |  |
| [[ZNF215]] | +0.55 | +0.48 / +0.53 | both halves | 2e-05 |  |
| [[NOD1]] | +0.55 | +0.43 / +0.58 | both halves | 3e-05 |  |
| [[MPG]] | +0.55 | +0.54 / +0.48 | both halves | 2e-05 |  |
| [[MCUB]] | +0.55 | +0.64 / +0.39 | both halves | 5e-05 |  |
| [[TMED8]] | +0.54 | +0.46 / +0.62 | both halves | 3e-05 |  |
| [[ANKS6]] | +0.53 | +0.48 / +0.44 | both halves | 3e-05 |  |
| [[PPIH]] | +0.52 | +0.51 / +0.45 | both halves | 3e-05 |  |
| [[ZNF749]] | +0.52 | +0.42 / +0.62 | both halves | 4e-05 |  |
| [[FAM24B]] | +0.52 | +0.40 / +0.45 | both halves | 5e-05 |  |

## Genes that move opposite

*39 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DAB1]] | -0.60 | -0.50 / -0.49 | both halves | 1e-05 |  |
| [[ALCAM]] | -0.57 | -0.41 / -0.61 | both halves | 4e-05 |  |
| [[TRIP12]] | -0.56 | -0.48 / -0.41 | both halves | 4e-05 |  |
| [[KLHL5]] | -0.56 | -0.49 / -0.54 | both halves | 1e-05 |  |
| [[CFAP418-AS1]] | -0.55 | -0.65 / -0.39 | both halves | 6e-05 |  |
| [[ATRX]] | -0.54 | -0.47 / -0.51 | both halves | 2e-05 |  |
| [[ITGAV]] | -0.54 | -0.31 / -0.58 | both halves | 2e-04 |  |
| [[PLA2G6]] | -0.53 | -0.50 / -0.42 | both halves | 4e-05 |  |
| [[RIPK2-DT]] | -0.53 | -0.57 / -0.41 | both halves | 4e-05 |  |
| [[CUTALP]] | -0.52 | -0.54 / -0.47 | both halves | 2e-05 |  |
| [[RAP2C-AS1]] | -0.52 | -0.54 / -0.44 | both halves | 3e-05 |  |
| [[OMA1]] | -0.52 | -0.52 / -0.42 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FGD1]] | B | FGD1 activity raises LSM11's level | lines that do not express FGD1 (9) vs lines expressing it (41) | 1.28× lower at baseline in the lines without FGD1 | 0.090 | ⚠ within organs, on part of the lines; also absent: CERCAM, CMTM3, CSRP2 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 051]] — Chromatin modifying enzymes; 89 genes; this gene is in the **-** arm (projection on the module's main direction -0.381). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (3.4, 26.9); signed map (-39.6, -0.0). **Vector** length 68.4, 10.5% of its response variance represented; |z| ≥ 3 in 883 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +4.0 | +5.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.9 | +1.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.9 | +1.9 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +2.7 | +2.5 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.6 | +2.1 |
|  | [[EX229 (drug)]] 5 µM |  | +2.2 | +1.3 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +1.9 | +1.8 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | +1.6 | +2.3 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +1.6 | +1.6 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -4.5 | -14.6 |
|  | [[TAK-901 (drug)]] 5 µM |  | -3.7 | -8.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -3.3 | -6.6 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -2.9 | -12.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.7 | -5.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.4 | -5.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.3 | -5.6 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.0 | -2.9 |
|  | [[Binimetinib (drug)]] 5 µM |  | -1.9 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | LSM11, U7 small nuclear RNA associated |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q33.3 — chr5:157,743,712-157,760,709 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ38273 |
| Gene groups (HGNC) | LSm proteins |
| Reactome | 5 pathways, smallest: SLBP independent Processing of Histone Pre-mRNAs; SLBP Dependent Processing of Replication-Dependent Histone Pre-mRNAs; Processing of Capped Intronless Pre-mRNA |
| Matched by | ensembl_id |

**Function**, from UniProt [P83369](https://www.uniprot.org/uniprotkb/P83369) (U7 snRNA-associated Sm-like protein LSm11):

> Component of the U7 snRNP complex that is involved in the histone 3'-end pre-mRNA processing. Increases U7 snRNA levels but not histone 3'-end pre-mRNA processing activity, when overexpressed. Required for cell cycle progression from G1 to S phases (By similarity). Binds specifically to the Sm-binding site of U7 snRNA.

**Summary**, from NCBI Gene [134353](https://www.ncbi.nlm.nih.gov/gene/134353):

> Enables U7 snRNA binding activity. Involved in mRNA 3'-end processing by stem-loop binding activity and cleavage; positive regulation of G1/S transition of mitotic cell cycle; and regulation of chromatin organization. Located in nuclear body. Part of U7 snRNP and telomerase holoenzyme complex. Implicated in Aicardi-Goutieres syndrome. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:30860](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30860) · Entrez [134353](https://www.ncbi.nlm.nih.gov/gene/134353) · UniProt [P83369](https://www.uniprot.org/uniprotkb/P83369) · Ensembl [ENSG00000155858](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000155858)

## Data

Gene col 7924: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7924); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7924, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7924]; `tensor/DDL_lfc|DDL_z.npy` [7924]; `embed/gene_vectors.npy` [7924]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7924 or target_col == 7924). Every well: [[LSM11 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LSM11.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
