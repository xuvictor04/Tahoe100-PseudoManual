---
symbol: "MLX"
type: "gene"
col: 2994
ensembl_id: "ENSG00000108788"
name: "MAX dimerization protein MLX"
location: "17q21.2"
module: 26
arm: "-"
pooled_cpm: 17.07
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 24
n_dd_up_clean: 5
n_dd_down_clean: 22
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/026"]
generated_by: "tahoemap"
---

# MLX

*MAX dimerization protein MLX* — 17q21.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 1.27× (z +3.9, q 0.057, up in 16 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 24 drug-doses (2 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.491× (z -16.3, q 0e+00, down in 44 of 47 measured lines).
> Its strongest partners by |cos| (88 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 12 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GPS1]] (+0.66, fdr 1e-05), [[APEH]] (+0.63, fdr 1e-05), [[DPM2]] (+0.61, fdr 1e-05); moves opposite to [[C2]] (-0.65, fdr 2e-05), [[KLRK1-AS1]] (-0.62, fdr 2e-04), [[CEACAM16-AS1]] (-0.62, fdr 2e-05).
> It sits in the **-** arm of [[Module 026]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[EPS15-AS1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 1 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2994.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **1.27×** | +3.9 | 0.057 | 16/48 (KATO III, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~4% here); position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.25×** | +3.6 | 0.057 | 18/44 (NCI-H23, SW 900, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here); position effect removed |
| [[Pralsetinib (drug)]] 5 µM |  | **1.51×** | +3.5 | 0.057 | 9/45 (RKO, NCI-H2030, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Bisoprolol (hemifumarate) (drug)]] 0.5 µM |  | **1.24×** | +3.5 | 0.057 | 10/47 (SNU-423, HEC-1-A, …) | inconsistent across doses |  |
| [[Abemaciclib (drug)]] 5 µM |  | **1.51×** | +3.5 | 0.057 | 8/48 (CFPAC-1, SW480, …) | top dose only | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM |  | **1.23×** | +3.4 | 0.066 | 10/48 (CFPAC-1, KATO III, …) | rises with dose | cell-cycle shift (explains ~4% here); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 2 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 24 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2994.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.491×** | -16.3 | 0e+00 | 44/47 (SW 900, hTERT-HPNE, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.555×** | -13.5 | 4e-39 | 36/47 (SK-MEL-2, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.590×** | -8.6 | 2e-15 | 35/48 (AsPC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.621×** | -7.7 | 1e-12 | 26/46 (KATO III, SNU-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.660×** | -6.5 | 9e-09 | 27/46 (HOP62, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.680×** | -6.3 | 4e-08 | 29/47 (hTERT-HPNE, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.680×** | -6.0 | 1e-07 | 26/48 (SW 900, C32, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.710×** | -5.6 | 2e-06 | 24/47 (hTERT-HPNE, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Verteporfin (drug)]] 5 µM |  | **0.726×** | -5.0 | 3e-05 | 19/47 (A498, AsPC-1, …) | top dose only | position effect removed |
| [[Trametinib (drug)]] 0.5 µM |  | **0.781×** | -5.0 | 3e-05 | 20/48 (RKO, NCI-H23, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 5 µM |  | **0.742×** | -5.0 | 3e-05 | 19/48 (NCI-H1792, SNU-1, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM |  | **0.779×** | -4.4 | 4e-04 | 17/48 (SNU-1, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **0.754×** | -4.4 | 4e-04 | 19/46 (HEC-1-A, NCI-H23, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.599×** | -4.4 | 5e-04 | 20/48 (NCI-H2030, hTERT-HPNE, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.773×** | -4.0 | 0.002 | 18/44 (C-33 A, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Binimetinib (drug)]] 0.05 µM |  | 0.841× | -3.8 | 0.005 | 14/48 (NCI-H460, NCI-H2030, …) | all doses, stronger at high dose |  |
| [[Bergenin (drug)]] 0.5 µM |  | **0.796×** | -3.7 | 0.007 | 14/46 (HCT15, PANC-1, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.03 per unit of S-phase module lfc, -0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2994. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[hTERT-HPNE (line)]] | wt | 24.5 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.213× (z -12.3) |
| [[A-172 (line)]] | wt | 26.0 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.226× (z -10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.395× (z -10.0) |
| [[C32 (line)]] | wt | 13.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.233× (z -10.5) |
| [[HOP62 (line)]] | alt | 17.3 | 0 | 2 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.241× (z -9.5) |
| [[Hs 766T (line)]] | wt | 15.9 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.145× (z -10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~76% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.324× (z -9.0) |
| [[NCI-H1792 (line)]] | alt | 13.2 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.235× (z -11.8) |
| [[NCI-H2030 (line)]] | alt | 36.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.370× (z -10.6) |
| [[NCI-H460 (line)]] | wt | 13.7 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.385× (z -10.6) |
| [[RKO (line)]] | wt | 24.2 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.129× (z -12.2) |
| [[SNU-423 (line)]] | alt | 14.0 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.339× (z -9.1) |
| [[A-427 (line)]] | wt | 17.7 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.190× (z -11.5) |
| [[A498 (line)]] | wt | 18.4 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.438× (z -9.4) |
| [[AsPC-1 (line)]] | alt | 14.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.335× (z -9.0) |
| [[KATO III (line)]] | alt | 20.9 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0866× (z -17.1) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 18.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.175× (z -11.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~76% of this change |
| [[MIA PaCa-2 (line)]] | alt | 19.3 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.240× (z -12.3) |
| [[NCI-H23 (line)]] | alt | 15.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.299× (z -10.9) |
| [[NCI-H2347 (line)]] | alt | 19.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.444× (z -8.9) |
| [[PANC-1 (line)]] | alt | 11.4 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.424× (z -9.7) |
| [[SK-MEL-2 (line)]] | alt | 17.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.251× (z -10.9) |
| [[SNU-1 (line)]] | wt | 19.1 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0901× (z -11.3) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 13.0 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.157× (z -13.4) |
| [[A549 (line)]] | wt | 21.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 9.90 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 19.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 23.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 10.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 19.6 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 19.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 19.7 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 11.4 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 16.4 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 20.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 13.0 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 14.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2994), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*36 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GPS1]] | +0.66 | +0.51 / +0.53 | both halves | 1e-05 |  |
| [[APEH]] | +0.63 | +0.50 / +0.52 | both halves | 1e-05 |  |
| [[DPM2]] | +0.61 | +0.50 / +0.49 | both halves | 1e-05 |  |
| [[CNEP1R1]] | +0.61 | +0.61 / +0.31 | both halves | 2e-04 |  |
| [[FBXW2]] | +0.61 | +0.57 / +0.46 | both halves | 3e-05 |  |
| [[TWF2]] | +0.59 | +0.59 / +0.24 | both halves | 4e-04 |  |
| [[RNF216P1]] | +0.59 | +0.62 / +0.25 | both halves | 4e-04 |  |
| [[TTLL12]] | +0.58 | +0.50 / +0.39 | both halves | 5e-05 |  |
| [[BLTP2]] | +0.58 | +0.61 / +0.39 | both halves | 5e-05 |  |
| [[BCKDK]] | +0.57 | +0.45 / +0.43 | both halves | 3e-05 |  |
| [[STN1]] | +0.57 | +0.56 / +0.33 | both halves | 1e-04 |  |
| [[RALB]] | +0.57 | +0.59 / +0.38 | both halves | 6e-05 |  |

## Genes that move opposite

*64 of its nearest partners move opposite, 12 of them with an alert (⚠; 12 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[C2]] | -0.65 | -0.67 / -0.47 | both halves | 2e-05 |  |
| [[KLRK1-AS1]] | -0.62 | -0.57 / -0.30 | both halves | 2e-04 |  |
| [[CEACAM16-AS1]] | -0.62 | -0.55 / -0.48 | both halves | 2e-05 |  |
| [[PABPN1]] | -0.61 | -0.62 / -0.52 | both halves | 1e-05 |  |
| [[KMT2E-AS1]] | -0.61 | -0.53 / -0.26 | both halves | 3e-04 |  |
| [[PPP1R15B-AS1]] | -0.61 | -0.52 / -0.44 | both halves | 3e-05 |  |
| [[ARGLU1]] | -0.60 | -0.43 / -0.45 | both halves | 3e-05 |  |
| [[SPEN-AS1]] | -0.59 | -0.60 / -0.32 | both halves | 2e-04 |  |
| [[KMO]] | -0.59 | -0.59 / -0.32 | both halves | 2e-04 |  |
| [[UNK]] | -0.59 | -0.58 / -0.34 | both halves | 1e-04 |  |
| [[HOXA-AS2]] | -0.59 | -0.53 / -0.34 | both halves | 1e-04 |  |
| [[STX17-DT]] | -0.59 | -0.64 / -0.32 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EPS15-AS1]] | B | EPS15-AS1 activity lowers MLX's level | lines that do not express EPS15-AS1 (12) vs lines expressing it (38) | 1.24× higher at baseline in the lines without EPS15-AS1 | 0.092 | ⚠ within organs, on part of the lines; also absent: RND1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 026]]; 163 genes; this gene is in the **-** arm (projection on the module's main direction -0.527). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.40).
- **Nodal map** (x, y) = (13.6, 21.9); signed map (-27.1, -43.9). **Vector** length 89.0, 17.6% of its response variance represented; |z| ≥ 3 in 909 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM |  | +5.5 | +3.9 |
|  | [[Panobinostat (drug)]] 5 µM |  | +5.0 | +3.4 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +4.7 | +2.0 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | +2.7 | +3.6 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.6 | +1.5 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +2.4 | +3.5 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | +1.9 | +1.9 |
|  | [[Dexamethasone (drug)]] 5 µM |  | +1.7 | +2.7 |
|  | [[Mebendazole (drug)]] 5 µM |  | +1.6 | +1.8 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.6 | -0.5 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -5.5 | -16.3 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -4.4 | -6.5 |
|  | [[Trametinib (drug)]] 5 µM |  | -3.7 | -4.4 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -3.7 | -13.5 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -3.6 | -5.0 |
|  | [[Binimetinib (drug)]] 0.05 µM |  | -3.5 | -3.8 |
|  | [[Binimetinib (drug)]] 5 µM |  | -3.5 | -5.0 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -3.5 | -4.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.8 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | MAX dimerization protein MLX |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q21.2 — chr17:42,567,072-42,573,239 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MAD7, MXD7, bHLHd13; previously TCFL4 |
| Gene groups (HGNC) | Basic helix-loop-helix proteins; MAX dimerization proteins |
| Reactome | 2 pathways, smallest: ChREBP activates metabolic gene expression; Integration of energy metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UH92](https://www.uniprot.org/uniprotkb/Q9UH92) (Max-like protein X):

> Transcription regulator. Forms a sequence-specific DNA-binding protein complex with MAD1, MAD4, MNT, WBSCR14 and MLXIP which recognizes the core sequence 5'-CACGTG-3'. The TCFL4-MAD1, TCFL4-MAD4, TCFL4-WBSCR14 complexes are transcriptional repressors. Plays a role in transcriptional activation of glycolytic target genes. Involved in glucose-responsive gene regulation.

**Summary**, from NCBI Gene [6945](https://www.ncbi.nlm.nih.gov/gene/6945):

> The product of this gene belongs to the family of basic helix-loop-helix leucine zipper (bHLH-Zip) transcription factors. These factors form heterodimers with Mad proteins and play a role in proliferation, determination and differentiation. This gene product may act to diversify Mad family function by its restricted association with a subset of the Mad family of transcriptional repressors, namely, Mad1 and Mad4. Alternatively spliced transcript variants encoding different isoforms have been …

**Accessions** — [HGNC:11645](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11645) · Entrez [6945](https://www.ncbi.nlm.nih.gov/gene/6945) · UniProt [Q9UH92](https://www.uniprot.org/uniprotkb/Q9UH92) · Ensembl [ENSG00000108788](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000108788)

## Data

Gene col 2994: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2994); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2994, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2994]; `tensor/DDL_lfc|DDL_z.npy` [2994]; `embed/gene_vectors.npy` [2994]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2994 or target_col == 2994). Every well: [[MLX — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MLX.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
