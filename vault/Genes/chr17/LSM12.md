---
symbol: "LSM12"
type: "gene"
col: 8446
ensembl_id: "ENSG00000161654"
name: "LSM12 homolog"
location: "17q21.31"
module: 33
arm: "+"
pooled_cpm: 32.59
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 6
n_dd_up_clean: 8
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/033"]
generated_by: "tahoemap"
---

# LSM12

*LSM12 homolog* — 17q21.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (2 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 5.35× (z +9.7, q 1e-19, up in 46 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.356× (z -11.9, q 4e-30, down in 32 of 39 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.540× (z -10.4, q 3e-23, down in 43 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SCAP]] (+0.65, fdr 7e-06), [[ZNF410]] (+0.62, fdr 7e-06), [[LHPP]] (+0.61, fdr 2e-05); moves opposite to [[NOTCH2NLB]] (-0.60, fdr 1e-05), [[EEA1]] (-0.58, fdr 3e-05), [[GATAD1]] (-0.56, fdr 1e-05).
> It sits in the **+** arm of [[Module 033]] (MYC targets v2).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 2 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8446.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **5.35×** | +9.7 | 1e-19 | 46/49 (SW480, NCI-H1573, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **4.35×** | +8.5 | 4e-15 | 39/47 (SW480, PANC-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.83×** | +7.3 | 5e-11 | 38/47 (NCI-H460, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.83×** | +7.3 | 5e-11 | 42/48 (NCI-H460, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.72×** | +6.5 | 7e-09 | 33/47 (NCI-H460, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.55×** | +5.3 | 1e-05 | 31/47 (NCI-H460, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.42×** | +4.2 | 0.002 | 29/48 (CFPAC-1, HT-29, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.40×** | +4.1 | 0.003 | 24/48 (NCI-H460, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Oxaliplatin (drug)]] 0.05 µM |  | **1.36×** | +3.5 | 0.025 | 19/48 (MIA PaCa-2, PANC-1, …) | inconsistent across doses | position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.33×** | +3.5 | 0.029 | 23/47 (MIA PaCa-2, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~14% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 3 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8446.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.356×** | -11.9 | 4e-30 | 32/39 (NCI-H460, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.374×** | -11.8 | 9e-30 | 37/44 (A-172, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.540×** | -10.4 | 3e-23 | 43/48 (A498, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.638×** | -5.2 | 3e-05 | 35/48 (SNU-423, C32, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.670×** | -4.4 | 0.001 | 25/44 (A-172, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.704×** | -4.0 | 0.005 | 23/47 (HS-578T, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.01 per unit of S-phase module lfc, -0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8446. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 39.8 | 6 (1 ⚠) | 2 (2 ⚠) | [[Digitoxin (drug)]] 0.5 µM 6.14× (z +15.9) | [[Dinaciclib (drug)]] 5 µM 0.0487× (z -25.4) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 38.0 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.242× (z -11.5) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.431× (z -9.6) |
| [[SW480 (line)]] | alt | 31.5 | 3 | 1 | [[Digitoxin (drug)]] 0.5 µM 2.69× (z +9.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.512× (z -8.9) |
| [[A498 (line)]] | wt | 31.9 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.324× (z -12.3) |
| [[HOP62 (line)]] | alt | 32.4 | 3 | 0 | [[Digitoxin (drug)]] 0.5 µM 4.06× (z +10.1) | — |
| [[NCI-H1792 (line)]] | alt | 29.5 | 3 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 5.82× (z +11.4) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 4.81× (z +10.2) | — |
| [[A-172 (line)]] | wt | 25.8 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.112× (z -14.0) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 34.7 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.146× (z -11.8) ⚠ cell-cycle shift, explains ~26% of this change |
| [[CFPAC-1 (line)]] | alt | 58.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.193× (z -11.0) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 73.4 | 0 | 2 (1 ⚠) | — | [[Temsirolimus (drug)]] 0.5 µM 0.167× (z -8.7) |
| [[HS-578T (line)]] | alt | 29.1 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.233× (z -10.0) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.389× (z -9.2) |
| [[hTERT-HPNE (line)]] | wt | 30.1 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0947× (z -12.0) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 32.7 | 2 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 5.31× (z +11.2) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 5.20× (z +11.1) | — |
| [[SW1417 (line)]] | alt | 35.1 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.393× (z -9.3) |
| [[A-427 (line)]] | wt | 40.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.205× (z -12.2) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 35.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0900× (z -16.3) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 26.7 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.320× (z -9.5) |
| [[HEC-1-A (line)]] | alt | 44.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.136× (z -12.6) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 28.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.286× (z -8.6) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 28.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.272× (z -9.5) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 38.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.306× (z -11.9) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H23 (line)]] | alt | 39.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.205× (z -12.0) ⚠ toxic; transcription drop |
| [[NCI-H661 (line)]] | alt | 45.8 | 0 | 1 | — | [[Temuterkib (drug)]] 0.05 µM 0.0495× (z -9.5) |
| [[PANC-1 (line)]] | alt | 18.4 | 1 | 0 | [[Digitoxin (drug)]] 0.5 µM 2.98× (z +8.7) | — |
| [[RKO (line)]] | wt | 33.8 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.319× (z -10.5) |
| [[SHP-77 (line)]] | alt | 34.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.227× (z -9.5) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 44.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.180× (z -9.9) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 39.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 22.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 43.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 25.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 21.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 34.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 34.6 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 16.2 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 26.1 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 26.5 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 39.2 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 21.5 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 38.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 33.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 36.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 33.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 42.1 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 24.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 19.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 31.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 28.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 45.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8446), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*70 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SCAP]] | +0.65 | +0.59 / +0.62 | both halves | 7e-06 |  |
| [[ZNF410]] | +0.62 | +0.72 / +0.60 | both halves | 7e-06 |  |
| [[LHPP]] | +0.61 | +0.69 / +0.46 | both halves | 2e-05 |  |
| [[SCAF4]] | +0.60 | +0.64 / +0.57 | both halves | 1e-05 |  |
| [[PTGES2]] | +0.58 | +0.52 / +0.51 | both halves | 1e-05 |  |
| [[RRP7BP]] | +0.58 | +0.55 / +0.55 | both halves | 1e-05 |  |
| [[GFOD2]] | +0.57 | +0.65 / +0.45 | both halves | 3e-05 |  |
| [[CPSF4]] | +0.57 | +0.62 / +0.49 | both halves | 1e-05 |  |
| [[NDUFS6]] | +0.57 | +0.50 / +0.56 | both halves | 1e-05 |  |
| [[GVQW3]] | +0.56 | +0.45 / +0.44 | both halves | 3e-05 |  |
| [[OGFOD3]] | +0.55 | +0.66 / +0.38 | both halves | 7e-05 |  |
| [[BRAT1]] | +0.55 | +0.61 / +0.43 | both halves | 4e-05 |  |

## Genes that move opposite

*30 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NOTCH2NLB]] | -0.60 | -0.61 / -0.49 | both halves | 1e-05 |  |
| [[EEA1]] | -0.58 | -0.69 / -0.46 | both halves | 3e-05 |  |
| [[GATAD1]] | -0.56 | -0.65 / -0.52 | both halves | 1e-05 |  |
| [[CHM]] | -0.55 | -0.61 / -0.36 | both halves | 1e-04 |  |
| [[NBPF10]] | -0.53 | -0.60 / -0.52 | both halves | 1e-05 |  |
| [[CCDC90B]] | -0.52 | -0.59 / -0.45 | both halves | 3e-05 |  |
| [[FCF1]] | -0.52 | -0.63 / -0.42 | both halves | 4e-05 |  |
| [[ZC3H6]] | -0.52 | -0.61 / -0.46 | both halves | 3e-05 |  |
| [[IFNAR1]] | -0.52 | -0.47 / -0.48 | both halves | 2e-05 |  |
| [[RIMOC1]] | -0.52 | -0.59 / -0.38 | both halves | 6e-05 |  |
| [[UBE3B]] | -0.51 | -0.62 / -0.39 | both halves | 5e-05 |  |
| [[DYNLRB1]] | -0.51 | -0.44 / -0.55 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises LSM12's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 1.1% of all compounds | 0.017 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 033]] — MYC targets v2; 139 genes; this gene is in the **+** arm (projection on the module's main direction 0.512). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-10.7, -16.1); signed map (-43.6, -23.4). **Vector** length 80.1, 19.1% of its response variance represented; |z| ≥ 3 in 880 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +5.9 | +1.1 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.6 | -1.5 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +3.5 | -1.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.9 | +0.0 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +2.7 | -2.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.2 | -0.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.1 | +8.5 |
|  | [[venetoclax (drug)]] 5 µM |  | +1.8 | +1.8 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +1.4 | -1.1 |
|  | [[Diphenhydramine (drug)]] 5 µM |  | +1.3 | +2.5 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -6.4 | -1.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | -6.4 | -2.4 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -4.2 | -1.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -3.3 | -10.4 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -3.2 | -5.2 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.9 | +0.1 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.9 | +0.0 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -1.9 | -0.7 |
|  | [[Terfenadine (drug)]] 0.5 µM |  | -1.6 | -1.5 |
|  | [[AZD-8055 (drug)]] 0.5 µM |  | -1.5 | -0.5 |

## What is on record

|  |  |
|---|---|
| Name | LSM12 homolog |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q21.31 — chr17:44,034,328-44,067,619 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ30656 |
| Gene groups (HGNC) | LSm proteins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q3MHD2](https://www.uniprot.org/uniprotkb/Q3MHD2) (Protein LSM12):

> Nicotinic acid adenine dinucleotide phosphate (NAADP) binding protein. Confers NAADP sensitivity to the two pore channel complex (TPCs) by acting as TPC accessory protein necessary for NAADP-evoked Ca(2+) release.

**Summary**, from NCBI Gene [124801](https://www.ncbi.nlm.nih.gov/gene/124801):

> Predicted to enable RNA binding activity. Located in cytoplasm. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:26407](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26407) · Entrez [124801](https://www.ncbi.nlm.nih.gov/gene/124801) · UniProt [Q3MHD2](https://www.uniprot.org/uniprotkb/Q3MHD2) · Ensembl [ENSG00000161654](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000161654)

## Data

Gene col 8446: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8446); `tables/drug_effects.parquet` (16 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8446, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8446]; `tensor/DDL_lfc|DDL_z.npy` [8446]; `embed/gene_vectors.npy` [8446]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8446 or target_col == 8446). Every well: [[LSM12 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LSM12.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
