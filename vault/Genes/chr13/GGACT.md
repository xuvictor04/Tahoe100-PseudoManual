---
symbol: "GGACT"
type: "gene"
col: 5615
ensembl_id: "ENSG00000134864"
name: "gamma-glutamylamine cyclotransferase"
location: "13q32.3"
module: 1
arm: "+"
pooled_cpm: 4.71
n_lines_expressing: 49
n_dd_up: 8
n_dd_down: 20
n_dd_up_clean: 5
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/001"]
generated_by: "tahoemap"
---

# GGACT

*gamma-glutamylamine cyclotransferase* — 13q32.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.30× (z +7.4, q 6e-11, up in 3 of 6 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Panobinostat (drug)]] 5 µM: 1.84× (z +5.7, q 5e-06, up in 20 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 20 drug-doses (6 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.280× (z -11.8, q 3e-29, down in 38 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[B3GALT9]] (+0.69, fdr 1e-05), [[ZFP41]] (+0.61, fdr 1e-05), [[ZFP62]] (+0.59, fdr 1e-05); moves opposite to [[COG7]] (-0.59, fdr 1e-05), [[TESK2]] (-0.55, fdr 3e-05), [[UBR2]] (-0.54, fdr 1e-05).
> It sits in the **+** arm of [[Module 001]] (rRNA processing).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 3 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5615.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.30×** | +7.4 | 6e-11 | 3/6 (SNU-423, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **1.84×** | +5.7 | 5e-06 | 20/45 (SW480, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.81×** | +5.1 | 7e-05 | 3/11 (A498, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.67×** | +4.8 | 2e-04 | 15/45 (SW480, HOP62, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.34×** | +3.8 | 0.014 | 8/45 (SW480, SW1417, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | **1.33×** | +3.7 | 0.021 | 9/44 (NCI-H1792, SW1417, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.67×** | +3.6 | 0.022 | 0/20 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM |  | **1.45×** | +3.5 | 0.036 | 12/45 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | 1.41× | +3.1 | 0.11 | 13/45 (COLO 205, SHP-77, …) | all doses, flat | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 6 with an alert ⚠. 20 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5615.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.280×** | -11.8 | 3e-29 | 38/45 (LOX-IMVI, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.380×** | -8.7 | 1e-15 | 28/43 (KATO III, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | **0.434×** | -7.7 | 2e-12 | 28/35 (SW480, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.468×** | -7.0 | 3e-10 | 24/43 (KATO III, HEC-1-A, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.478×** | -6.8 | 1e-09 | 26/45 (LS 180, SNU-423, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~78% of this change | **0.596×** | -6.8 | 1e-09 | 20/36 (HEC-1-A, A549, …) | top dose only | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.475×** | -6.6 | 2e-09 | 25/43 (LS 180, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.508×** | -6.0 | 1e-07 | 16/28 (LS 180, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.551×** | -5.5 | 2e-06 | 21/45 (A-427, HOP62, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.546×** | -5.3 | 7e-06 | 20/39 (C32, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.569×** | -5.0 | 3e-05 | 19/42 (SHP-77, KATO III, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~72% of this change | **0.636×** | -4.0 | 0.003 | 16/42 (HEC-1-A, SNU-423, …) | top dose only | composition shift |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.623×** | -3.3 | 0.038 | 5/45 (SW1417, HCT15, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.699×** | -3.3 | 0.038 | 12/41 (PANC-1, RKO, …) | all doses, stronger at high dose |  |
| [[Naproxen (drug)]] 5 µM |  | **0.700×** | -3.2 | 0.060 | 10/38 (HOP62, HT-29, …) | top dose only |  |
| [[EX229 (drug)]] 0.05 µM |  | **0.700×** | -3.1 | 0.066 | 8/43 (HS-578T, HOP62, …) | inconsistent across doses |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.710×** | -3.0 | 0.078 | 11/35 (HEC-1-A, Panc 03.27, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Allopurinol (drug)]] 0.05 µM |  | **0.721×** | -3.0 | 0.078 | 6/45 (CFPAC-1, LOX-IMVI, …) | inconsistent across doses |  |
| [[Quinidine (15% dihydroquinidine) (drug)]] 0.5 µM |  | **0.652×** | -3.0 | 0.078 | 3/45 (SK-MEL-2, A549, …) | inconsistent across doses | noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.542×** | -3.0 | 0.087 | 8/34 (SW480, HOP62, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.11 per unit of S-phase module lfc, -0.59 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5615. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 7.89 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.174× (z -9.6) ⚠ cell-cycle shift, explains ~78% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.0904× (z -9.0) |
| [[LS 180 (line)]] | wt | 5.29 | 0 | 3 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0581× (z -10.5) ⚠ toxic · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0640× (z -10.2) |
| [[HEC-1-A (line)]] | alt | 34.5 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.272× (z -14.0) ⚠ cell-cycle shift, explains ~78% of this change |
| [[KATO III (line)]] | alt | 6.18 | 0 | 2 | — | [[Digitoxin (drug)]] 0.5 µM 0.0722× (z -10.1) |
| [[SW480 (line)]] | alt | 4.39 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0573× (z -12.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.123× (z -8.6) |
| [[HOP62 (line)]] | alt | 3.23 | 0 | 1 | — | [[Naproxen (drug)]] 5 µM 0.0654× (z -9.2) |
| [[MIA PaCa-2 (line)]] | alt | 4.90 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0444× (z -11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change |
| [[NCI-H1573 (line)]] | alt | 5.10 | 0 | 1 | — | [[Malotilate (drug)]] 0.05 µM 0.0547× (z -9.9) |
| [[NCI-H2347 (line)]] | alt | 2.87 | 0 | 1 | — | [[Proglumide (drug)]] 0.05 µM 0.0732× (z -9.5) |
| [[PANC-1 (line)]] | alt | 2.27 | 0 | 1 | — | [[Temsirolimus (drug)]] 0.5 µM 0.0924× (z -8.7) |
| [[RPMI-7951 (line)]] | alt | 3.91 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0896× (z -9.4) ⚠ cell-cycle shift, explains ~78% of this change |
| [[SNU-423 (line)]] | alt | 5.86 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0886× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change |
| [[A-172 (line)]] | wt | 2.68 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 2.83 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.99 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 8.05 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.69 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.08 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.87 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.88 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.46 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.16 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.56 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.65 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.29 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.75 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.77 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.41 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.74 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 5.24 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 5.12 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 5.49 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.09 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.10 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.51 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 5.69 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.79 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.32 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.54 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.86 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.00 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 5.03 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.52 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.848 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 2.35 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 9.41 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.44 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.40 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.97 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5615), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*68 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[B3GALT9]] | +0.69 | +0.72 / +0.55 | both halves | 1e-05 |  |
| [[ZFP41]] | +0.61 | +0.58 / +0.52 | both halves | 1e-05 |  |
| [[ZFP62]] | +0.59 | +0.53 / +0.60 | both halves | 1e-05 |  |
| [[TXNRD3]] | +0.58 | +0.56 / +0.60 | both halves | 1e-05 | STRING 502 |
| [[TMEM185B]] | +0.57 | +0.52 / +0.58 | both halves | 1e-05 |  |
| [[ZBTB47]] | +0.57 | +0.57 / +0.48 | both halves | 2e-05 |  |
| [[ZNF239]] | +0.57 | +0.54 / +0.62 | both halves | 1e-05 |  |
| [[IQCH]] | +0.56 | +0.60 / +0.45 | both halves | 3e-05 |  |
| [[PAK1IP1]] | +0.54 | +0.56 / +0.49 | both halves | 1e-05 |  |
| [[ARPIN]] | +0.54 | +0.52 / +0.49 | both halves | 1e-05 |  |
| [[KPNA1]] | +0.53 | +0.49 / +0.53 | both halves | 2e-05 |  |
| [[B3GALT6]] | +0.53 | +0.63 / +0.39 | both halves | 5e-05 |  |

## Genes that move opposite

*32 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[COG7]] | -0.59 | -0.51 / -0.56 | both halves | 1e-05 |  |
| [[TESK2]] | -0.55 | -0.43 / -0.52 | both halves | 3e-05 |  |
| [[UBR2]] | -0.54 | -0.49 / -0.55 | both halves | 1e-05 |  |
| [[UBE4B]] | -0.54 | -0.48 / -0.56 | both halves | 2e-05 |  |
| [[FAM117A]] | -0.52 | -0.26 / -0.51 | both halves | 3e-04 |  |
| [[NSD3]] | -0.52 | -0.43 / -0.53 | both halves | 3e-05 |  |
| [[PMS2P4-1]] | -0.50 | -0.43 / -0.51 | both halves | 3e-05 |  |
| [[EMSY]] | -0.49 | -0.44 / -0.51 | both halves | 3e-05 |  |
| [[EGFL8]] | -0.49 | -0.42 / -0.49 | both halves | 4e-05 |  |
| [[KLC4]] | -0.49 | -0.29 / -0.55 | both halves | 2e-04 |  |
| [[CEP57]] | -0.49 | -0.36 / -0.50 | both halves | 1e-04 |  |
| [[MFSD11]] | -0.49 | -0.32 / -0.51 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity lowers GGACT's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity lowers GGACT's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 001]] — rRNA processing; 298 genes; this gene is in the **+** arm (projection on the module's main direction 0.404). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-11.9, -28.6); signed map (8.4, -50.4). **Vector** length 53.8, 7.23% of its response variance represented; |z| ≥ 3 in 1,109 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.7 | +5.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.8 | +7.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.7 | +1.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.3 | +3.6 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.0 | +2.9 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.7 | +2.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.3 | -3.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.3 | +3.8 |
| fall | [[Auranofin (drug)]] 5 µM |  | -3.1 | -7.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -2.5 | -11.8 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -2.2 | -5.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -2.1 | -6.6 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -2.1 | -6.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.5 | -5.0 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -1.4 | -2.8 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.4 | -3.3 |
|  | [[Gefitinib (drug)]] 5 µM |  | -1.2 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | gamma-glutamylamine cyclotransferase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 13q32.3 — chr13:100,530,164-100,589,528 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously A2LD1 |
| Gene groups (HGNC) | Carbon-nitrogen lyases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BVM4](https://www.uniprot.org/uniprotkb/Q9BVM4) (Gamma-glutamylaminecyclotransferase):

> Contributes to degradation of proteins cross-linked by transglutaminases by degrading the cross-link between a lysine and a glutamic acid residue. Catalyzes the formation of 5-oxo-L-proline from L-gamma-glutamyl-L-epsilon-lysine. Inactive with L-gamma-glutamyl-alpha-amino acid substrates such as L-gamma-glutamyl-L-alpha-cysteine and L-gamma-glutamyl-L-alpha-alanine.

**Summary**, from NCBI Gene [87769](https://www.ncbi.nlm.nih.gov/gene/87769):

> The protein encoded by this gene aids in the proteolytic degradation of crosslinked fibrin by breaking down isodipeptide L-gamma-glutamyl-L-epsilon-lysine, a byproduct of fibrin degradation. The reaction catalyzed by the encoded gamma-glutamylaminecyclotransferase produces 5-oxo-L-proline and a free alkylamine. Two transcript variants encoding the same protein have been found for this gene.[provided by RefSeq, Aug 2010]

**Accessions** — [HGNC:25100](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25100) · Entrez [87769](https://www.ncbi.nlm.nih.gov/gene/87769) · UniProt [Q9BVM4](https://www.uniprot.org/uniprotkb/Q9BVM4) · Ensembl [ENSG00000134864](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000134864)

## Data

Gene col 5615: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5615); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5615, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5615]; `tensor/DDL_lfc|DDL_z.npy` [5615]; `embed/gene_vectors.npy` [5615]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5615 or target_col == 5615). Every well: [[GGACT — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GGACT.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
