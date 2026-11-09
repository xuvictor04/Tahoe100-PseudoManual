---
symbol: "ZBTB5"
type: "gene"
col: 9701
ensembl_id: "ENSG00000168795"
name: "zinc finger and BTB domain containing 5"
location: "9p13.2"
module: 41
arm: "+"
pooled_cpm: 30.27
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 6
n_dd_up_clean: 9
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/041"]
generated_by: "tahoemap"
---

# ZBTB5

*zinc finger and BTB domain containing 5* — 9p13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.99× (z +14.5, q 8e-45, up in 40 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.590× (z -7.8, q 3e-12, down in 30 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Belumosudil (drug)]] 5 µM: 0.720× (z -4.7, q 5e-04, down in 24 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ELP5]] (+0.56, fdr 2e-05), [[PEX13]] (+0.54, fdr 2e-05), [[ZNF33A]] (+0.50, fdr 1e-05); moves opposite to [[RAP1GDS1]] (-0.50, fdr 3e-05), [[ZEB1]] (-0.49, fdr 5e-05), [[HSPA4]] (-0.48, fdr 4e-05).
> It sits in the **+** arm of [[Module 041]] (Intra-Golgi and retrograde Golgi-to-ER traffic).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 1 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9701.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.99×** | +14.5 | 8e-45 | 40/47 (MIA PaCa-2, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **5.49×** | +13.2 | 2e-37 | 44/48 (PANC-1, MIA PaCa-2, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **3.01×** | +8.6 | 2e-15 | 30/48 (SW480, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.67×** | +7.6 | 4e-12 | 38/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.52×** | +6.3 | 4e-08 | 28/48 (SW480, RKO, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.45×** | +5.6 | 3e-06 | 24/48 (SW480, MIA PaCa-2, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.43×** | +5.3 | 9e-06 | 24/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.37×** | +4.7 | 2e-04 | 24/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.34×** | +4.4 | 7e-04 | 24/47 (PANC-1, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.32×** | +4.0 | 0.004 | 20/48 (NCI-H460, A498, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 3 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9701.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.590×** | -7.8 | 3e-12 | 30/44 (SHP-77, SK-MEL-2, …) | two highest doses | cell-cycle shift (explains ~21% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.608×** | -7.1 | 4e-10 | 26/37 (KATO III, SW 900, …) | two highest doses | cell-cycle shift (explains ~20% here); composition shift |
| [[Belumosudil (drug)]] 5 µM |  | **0.720×** | -4.7 | 5e-04 | 24/48 (PANC-1, NCI-H2030, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.827×** | -4.0 | 0.009 | 25/48 (SW480, A-427, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.769×** | -3.7 | 0.020 | 20/47 (NCI-H23, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~13% here); position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~15% of this change | **0.783×** | -3.5 | 0.046 | 15/48 (NCI-H23, SNU-1, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.10 per unit of S-phase module lfc, -0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9701. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 72.1 | 5 | 0 | [[TAK-901 (drug)]] 5 µM 14.7× (z +14.9) | — |
| [[NCI-H460 (line)]] | wt | 19.2 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.18× (z +13.5) | — |
| [[SW480 (line)]] | alt | 31.1 | 3 | 1 (1 ⚠) | [[PH-797804 (drug)]] 5 µM 5.78× (z +9.5) | [[Dinaciclib (drug)]] 0.5 µM 0.357× (z -10.8) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 44.7 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.91× (z +9.1) | [[Dinaciclib (drug)]] 5 µM 0.236× (z -13.9) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 80.0 | 1 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.22× (z +10.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.500× (z -8.8) ⚠ cell-cycle shift, explains ~47% of this change · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.371× (z -8.6) |
| [[SNU-423 (line)]] | alt | 23.7 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.222× (z -10.9) ⚠ toxic; transcription drop · without an alert: [[HI-TOPK-032 (drug)]] 0.05 µM 0.222× (z -10.3) |
| [[A-172 (line)]] | wt | 26.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.54× (z +10.2) | — |
| [[HEC-1-A (line)]] | alt | 22.2 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 8.12× (z +9.3) | — |
| [[MIA PaCa-2 (line)]] | alt | 26.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.83× (z +15.5) | — |
| [[NCI-H2347 (line)]] | alt | 14.8 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.38× (z +9.2) | [[Dinaciclib (drug)]] 0.05 µM 0.269× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SK-MEL-2 (line)]] | alt | 29.2 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.48× (z +12.6) | [[Dinaciclib (drug)]] 0.5 µM 0.144× (z -13.9) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 41.8 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.42× (z +10.1) | [[Dinaciclib (drug)]] 0.5 µM 0.174× (z -10.1) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 28.1 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.62× (z +9.3) | [[Dinaciclib (drug)]] 5 µM 0.0965× (z -15.4) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 36.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.53× (z +10.9) | — |
| [[AN3 CA (line)]] | alt | 35.6 | 0 | 1 | — | [[Vitamin K4 (drug)]] 0.5 µM 0.124× (z -8.7) |
| [[C-33 A (line)]] | alt | 40.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.269× (z -8.7) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 15.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.90× (z +8.9) | — |
| [[HCT15 (line)]] | alt | 36.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.105× (z -12.2) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 21.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.152× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[KATO III (line)]] | alt | 36.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0786× (z -17.8) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 22.7 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 10.9× (z +9.2) | — |
| [[NCI-H2030 (line)]] | alt | 20.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.32× (z +8.5) | — |
| [[SHP-77 (line)]] | alt | 27.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0976× (z -15.7) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 15.1 | 0 | 1 | — | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM 0.116× (z -9.3) |
| [[A-427 (line)]] | wt | 26.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 30.1 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 21.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 10.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 46.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 24.1 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 44.0 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 22.8 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 35.7 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 23.7 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 23.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 21.5 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 31.4 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 28.0 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 28.9 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 27.2 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 20.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 22.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 26.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 36.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 24.7 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 21.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 23.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 32.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 28.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 33.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9701), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*59 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ELP5]] | +0.56 | +0.56 / +0.48 | both halves | 2e-05 |  |
| [[PEX13]] | +0.54 | +0.58 / +0.47 | both halves | 2e-05 |  |
| [[ZNF33A]] | +0.50 | +0.51 / +0.52 | both halves | 1e-05 | same gene group |
| [[SENP2]] | +0.50 | +0.49 / +0.42 | both halves | 4e-05 |  |
| [[ATG13]] | +0.49 | +0.44 / +0.51 | both halves | 3e-05 |  |
| [[ILF3-DT]] | +0.49 | +0.56 / +0.42 | both halves | 4e-05 |  |
| [[SERTAD3]] | +0.49 | +0.55 / +0.38 | both halves | 7e-05 |  |
| [[TEN1]] | +0.48 | +0.47 / +0.49 | both halves | 2e-05 |  |
| [[STK19]] | +0.48 | +0.52 / +0.41 | both halves | 4e-05 |  |
| [[BBOF1]] | +0.47 | +0.48 / +0.37 | both halves | 8e-05 |  |
| [[DIABLO]] | +0.47 | +0.59 / +0.34 | both halves | 1e-04 |  |
| [[ZNF136]] | +0.47 | +0.44 / +0.43 | both halves | 3e-05 | same gene group |

## Genes that move opposite

*41 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RAP1GDS1]] | -0.50 | -0.50 / -0.45 | both halves | 3e-05 |  |
| [[ZEB1]] | -0.49 | -0.44 / -0.40 | both halves | 5e-05 | same gene group |
| [[HSPA4]] | -0.48 | -0.42 / -0.46 | both halves | 4e-05 |  |
| [[HSPH1]] | -0.47 | -0.55 / -0.36 | both halves | 9e-05 |  |
| [[CCT5]] | -0.46 | -0.50 / -0.33 | both halves | 1e-04 |  |
| [[GALNT14]] | -0.45 | -0.42 / -0.34 | both halves | 1e-04 |  |
| [[KANK1]] | -0.44 | -0.43 / -0.38 | both halves | 6e-05 |  |
| [[CNKSR2]] | -0.44 | -0.40 / -0.37 | both halves | 8e-05 |  |
| [[SMAGP]] | -0.44 | -0.45 / -0.37 | both halves | 9e-05 |  |
| [[CCT6A]] | -0.44 | -0.38 / -0.41 | both halves | 6e-05 |  |
| [[KIF21A]] | -0.44 | -0.44 / -0.33 | both halves | 1e-04 |  |
| [[AHCYL2]] | -0.44 | -0.38 / -0.42 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises ZBTB5's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Mitoxantrone) | 60% of the class's compounds vs 1.4% of all compounds | 0.026 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[TOP2B]] | B | TOP2B activity raises ZBTB5's level | compounds that target TOP2B: 2 of 2 lower it (Doxorubicin, Mitoxantrone) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; shared targets; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 041]] — Intra-Golgi and retrograde Golgi-to-ER traffic; 111 genes; this gene is in the **+** arm (projection on the module's main direction 0.348). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (4.5, -35.1); signed map (-12.4, 2.6). **Vector** length 74.7, 14.5% of its response variance represented; |z| ≥ 3 in 931 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +6.1 | +13.2 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +3.4 | +14.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +3.2 | +2.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +2.7 | +0.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.4 | +8.6 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | +1.6 | +0.6 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +1.5 | +0.3 |
|  | [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | +1.3 | +1.3 |
|  | [[Trametinib (drug)]] 0.05 µM |  | +1.3 | +2.0 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -4.9 | -3.0 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -4.2 | -3.7 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -4.0 | -0.7 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~15% of this change | -3.7 | -3.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.5 | -1.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.3 | -4.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.7 | -1.7 |
|  | [[EX229 (drug)]] 5 µM |  | -2.6 | -2.1 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.6 | -2.9 |

## What is on record

|  |  |
|---|---|
| Name | zinc finger and BTB domain containing 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9p13.2 — chr9:37,438,102-37,465,450 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0354 |
| Gene groups (HGNC) | Zinc fingers C2H2-type; BTB domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [O15062](https://www.uniprot.org/uniprotkb/O15062) (Zinc finger and BTB domain-containing protein 5):

> May be involved in transcriptional regulation.

**Summary**, from NCBI Gene [9925](https://www.ncbi.nlm.nih.gov/gene/9925):

> Enables DNA-binding transcription repressor activity, RNA polymerase II-specific and RNA polymerase II transcription regulatory region sequence-specific DNA binding activity. Involved in negative regulation of transcription by RNA polymerase II. Located in nucleus. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:23836](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23836) · Entrez [9925](https://www.ncbi.nlm.nih.gov/gene/9925) · UniProt [O15062](https://www.uniprot.org/uniprotkb/O15062) · Ensembl [ENSG00000168795](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000168795)

## Data

Gene col 9701: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9701); `tables/drug_effects.parquet` (16 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9701, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9701]; `tensor/DDL_lfc|DDL_z.npy` [9701]; `embed/gene_vectors.npy` [9701]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9701 or target_col == 9701). Every well: [[ZBTB5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZBTB5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
