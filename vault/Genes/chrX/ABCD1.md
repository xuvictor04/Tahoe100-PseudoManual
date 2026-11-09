---
symbol: "ABCD1"
type: "gene"
col: 2199
ensembl_id: "ENSG00000101986"
name: "ATP binding cassette subfamily D member 1"
location: "Xq28"
module: 2
arm: "+"
pooled_cpm: 7.03
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 13
n_dd_up_clean: 5
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/002"]
generated_by: "tahoemap"
---

# ABCD1

*ATP binding cassette subfamily D member 1* — Xq28

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (8 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.54× (z +11.8, q 2e-29, up in 36 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (7 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.405× (z -11.4, q 2e-27, down in 29 of 40 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Harringtonine (drug)]] 5 µM: 0.390× (z -10.9, q 3e-25, down in 26 of 43 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TINF2]] (+0.62, fdr 1e-05), [[TESK1]] (+0.56, fdr 9e-05), [[NOTCH1]] (+0.56, fdr 1e-05); moves opposite to [[YEATS4]] (-0.50, fdr 5e-05), [[TIMM9]] (-0.50, fdr 6e-05), [[SCAF11]] (-0.47, fdr 6e-05).
> It sits in the **+** arm of [[Module 002]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 8 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2199.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.54×** | +11.8 | 2e-29 | 36/47 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~14% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.32×** | +10.7 | 3e-24 | 32/45 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~13% here); position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.10×** | +7.6 | 7e-12 | 15/29 (SW480, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~1% here); composition shift; noisy plate (z scaled); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.87×** | +7.3 | 5e-11 | 5/13 (PANC-1, SW1417, …) | all doses, flat | cell-cycle shift (explains ~5% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.80×** | +6.9 | 6e-10 | 9/19 (SW1417, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~7% here); composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.41×** | +6.2 | 7e-08 | 17/40 (RKO, KATO III, …) | rises with dose | position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **1.52×** | +5.3 | 9e-06 | 15/47 (SW480, PANC-1, …) | top dose only | cell-cycle shift (explains ~21% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.54×** | +5.0 | 3e-05 | 14/38 (C32, RKO, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.29×** | +4.5 | 3e-04 | 11/45 (LS 180, NCI-H460, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~47% of this change | **1.43×** | +4.2 | 0.001 | 8/32 (LoVo, AsPC-1, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.23×** | +3.7 | 0.012 | 10/47 (RKO, Hs 766T, …) | rises with dose | position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.33×** | +3.7 | 0.012 | 6/33 (COLO 205, SW480, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **1.29×** | +3.3 | 0.044 | 7/43 (A498, RKO, …) | rises with dose | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 8 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2199.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.405×** | -11.4 | 2e-27 | 29/40 (Hs 766T, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.390×** | -10.9 | 3e-25 | 26/43 (A-172, J82, …) | rises with dose | cell-cycle shift (explains ~23% here); composition shift; position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.428×** | -10.7 | 1e-24 | 35/47 (HT-29, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.531×** | -8.0 | 2e-13 | 27/44 (NCI-H2030, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.543×** | -7.7 | 1e-12 | 21/42 (SW480, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.582×** | -6.8 | 8e-10 | 23/47 (NCI-H460, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.606×** | -6.3 | 2e-08 | 18/37 (A-172, A549, …) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.605×** | -5.8 | 4e-07 | 18/35 (NCI-H2030, LS 180, …) | rises with dose | cell-cycle shift (explains ~9% here); position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **0.443×** | -5.4 | 5e-06 | 17/42 (Panc 03.27, HOP62, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~13% here); composition shift; noisy plate (z scaled) |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **0.712×** | -4.3 | 0.001 | 17/44 (SK-MEL-2, LS 180, …) | all doses, flat |  |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.726×** | -4.0 | 0.003 | 20/45 (LoVo, SHP-77, …) | all doses, stronger at high dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.745×** | -3.7 | 0.010 | 13/47 (SNU-1, NCI-H23, …) | inconsistent across doses |  |
| [[Radotinib (drug)]] 5 µM |  | 0.836× | -3.2 | 0.063 | 7/44 (H4, A-427, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **0.737×** | -3.1 | 0.082 | 11/45 (NCI-H460, A-427, …) | rises with dose | noisy plate (z scaled); position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.930× | -3.0 | 0.096 | 7/48 (NCI-H23, HOP62, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.32 per unit of S-phase module lfc, -0.48 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2199. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 22.6 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.159× (z -16.1) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.120× (z -12.0) |
| [[C32 (line)]] | wt | 6.89 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.98× (z +9.0) ⚠ cell-cycle shift, would explain all of this change | [[Digitoxin (drug)]] 5 µM 0.117× (z -8.6) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 13.1 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.161× (z -9.8) |
| [[NCI-H2030 (line)]] | alt | 5.49 | 0 | 2 | — | [[Bexarotene (drug)]] 0.05 µM 0.0623× (z -11.2) |
| [[A549 (line)]] | wt | 3.22 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0485× (z -9.1) ⚠ cell-cycle shift, explains ~35% of this change |
| [[HepG2_C3A (line)]] | wt | 13.3 | 0 | 1 | — | [[Clofarabine (drug)]] 5 µM 0.0607× (z -10.1) |
| [[Hs 766T (line)]] | wt | 9.92 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0512× (z -13.7) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 10.2 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.118× (z -10.3) |
| [[J82 (line)]] | alt | 5.63 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.0755× (z -9.3) |
| [[MIA PaCa-2 (line)]] | alt | 7.00 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0992× (z -9.8) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 11.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.236× (z -10.4) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H460 (line)]] | wt | 5.70 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.201× (z -8.5) |
| [[RKO (line)]] | wt | 8.47 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.0968× (z -8.9) |
| [[SW1417 (line)]] | alt | 7.62 | 0 | 1 (1 ⚠) | — | [[Pimozide (drug)]] 0.5 µM 0.173× (z -8.5) ⚠ transcription drop |
| [[SW480 (line)]] | alt | 6.11 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.145× (z -11.4) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 4.79 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 5.59 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 6.02 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.85 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.36 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 6.80 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 4.93 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.50 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 8.81 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 5.94 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.97 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.20 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 7.67 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 4.15 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.31 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 9.68 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 2.12 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.15 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 5.80 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.97 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.71 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.89 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.59 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.55 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 9.04 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 5.59 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.55 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 33.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.92 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 7.11 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 9.29 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.95 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.10 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.10 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2199), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TINF2]] | +0.62 | +0.56 / +0.49 | both halves | 1e-05 |  |
| [[TESK1]] | +0.56 | +0.36 / +0.58 | both halves | 9e-05 |  |
| [[NOTCH1]] | +0.56 | +0.62 / +0.50 | both halves | 1e-05 |  |
| [[HAPSTR1]] | +0.56 | +0.48 / +0.49 | both halves | 2e-05 |  |
| [[PNP]] | +0.55 | +0.56 / +0.50 | both halves | 1e-05 |  |
| [[MAN2B2]] | +0.54 | +0.36 / +0.54 | both halves | 1e-04 |  |
| [[CEP170B]] | +0.54 | +0.56 / +0.43 | both halves | 3e-05 |  |
| [[KCTD5]] | +0.53 | +0.55 / +0.47 | both halves | 2e-05 |  |
| [[SBF1]] | +0.52 | +0.38 / +0.45 | both halves | 7e-05 |  |
| [[PPP4C]] | +0.52 | +0.36 / +0.55 | both halves | 1e-04 |  |
| [[NR1H2]] | +0.52 | +0.51 / +0.40 | both halves | 5e-05 |  |
| [[FERMT3]] | +0.51 | +0.56 / +0.38 | both halves | 6e-05 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[YEATS4]] | -0.50 | -0.39 / -0.53 | both halves | 5e-05 |  |
| [[TIMM9]] | -0.50 | -0.38 / -0.45 | both halves | 6e-05 | pathway: Protein localization |
| [[SCAF11]] | -0.47 | -0.39 / -0.38 | both halves | 6e-05 |  |
| [[FIGN]] | -0.46 | -0.32 / -0.36 | both halves | 2e-04 |  |
| [[XPA]] | -0.46 | -0.41 / -0.32 | both halves | 2e-04 |  |
| [[NAPEPLD]] | -0.44 | -0.29 / -0.36 | both halves | 3e-04 |  |
| [[GPR15]] | -0.44 | -0.41 / -0.39 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers ABCD1's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Idarubicin, Mitoxantrone) | 60% of the class's compounds vs 2.5% of all compounds | 0.065 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 002]]; 248 genes; this gene is in the **+** arm (projection on the module's main direction 0.529). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.21).
- **Nodal map** (x, y) = (15.9, -6.8); signed map (-9.5, 30.8). **Vector** length 57.0, 7.65% of its response variance represented; |z| ≥ 3 in 1,073 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.5 | +7.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.1 | +7.6 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | +2.5 | +3.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.0 | +6.9 |
|  | [[Panobinostat (drug)]] 5 µM |  | +2.0 | +11.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.6 | +0.8 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +1.5 | +2.0 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +1.1 | +1.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.0 | +1.5 |
|  | [[Saquinavir (drug)]] 0.5 µM |  | +1.0 | +2.2 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -2.8 | -10.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -2.7 | -7.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | -2.6 | -6.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.2 | -0.7 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.2 | -8.0 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.9 | -2.8 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -1.6 | -1.2 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.4 | +0.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.3 | +0.0 |

## What is on record

|  |  |
|---|---|
| Name | ATP binding cassette subfamily D member 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xq28 — chrX:153,724,856-153,744,755 (+) |
| Ensembl biotype | protein_coding |
| Also known as | AMN, ALDP, adrenoleukodystrophy; previously ALD |
| Gene groups (HGNC) | ATP binding cassette subfamily D |
| Hallmark sets | BILE_ACID_METABOLISM, PEROXISOME |
| Reactome | 14 pathways, smallest: Linoleic acid (LA) metabolism; Beta-oxidation of very long chain fatty acids; alpha-linolenic (omega3) and linoleic (omega6) acid metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [P33897](https://www.uniprot.org/uniprotkb/P33897) (ATP-binding cassette sub-family D member 1):

> ATP-dependent transporter of the ATP-binding cassette (ABC) family involved in the transport of very long chain fatty acid (VLCFA)-CoA from the cytosol to the peroxisome lumen. Coupled to the ATP-dependent transporter activity also has a fatty acyl-CoA thioesterase activity (ACOT) and hydrolyzes VLCFA-CoA into VLCFA prior their ATP-dependent transport into peroxisomes, the ACOT activity is essential during this transport process. Thus, plays a role in regulation of VLCFAs and energy metabolism …

**Summary**, from NCBI Gene [215](https://www.ncbi.nlm.nih.gov/gene/215):

> The protein encoded by this gene is a member of the superfamily of ATP-binding cassette (ABC) transporters. ABC proteins transport various molecules across extra- and intra-cellular membranes. ABC genes are divided into seven distinct subfamilies (ABC1, MDR/TAP, MRP, ALD, OABP, GCN20, White). This protein is a member of the ALD subfamily, which is involved in peroxisomal import of fatty acids and/or fatty acyl-CoAs in the organelle. All known peroxisomal ABC transporters are half transporters …

**Accessions** — [HGNC:61](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:61) · Entrez [215](https://www.ncbi.nlm.nih.gov/gene/215) · UniProt [P33897](https://www.uniprot.org/uniprotkb/P33897) · Ensembl [ENSG00000101986](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000101986)

## Data

Gene col 2199: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2199); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2199, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2199]; `tensor/DDL_lfc|DDL_z.npy` [2199]; `embed/gene_vectors.npy` [2199]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2199 or target_col == 2199). Every well: [[ABCD1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ABCD1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
