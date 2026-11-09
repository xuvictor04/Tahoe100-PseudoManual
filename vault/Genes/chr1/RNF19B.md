---
symbol: "RNF19B"
type: "gene"
col: 3801
ensembl_id: "ENSG00000116514"
name: "ring finger protein 19B"
location: "1p35.1"
module: 59
arm: "+"
pooled_cpm: 52.56
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 7
n_dd_up_clean: 9
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/059"]
generated_by: "tahoemap"
---

# RNF19B

*ring finger protein 19B* — 1p35.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (3 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 3.20× (z +9.9, q 3e-20, up in 40 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.521× (z -10.6, q 2e-23, down in 36 of 45 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[NG25 (drug)]] 5 µM: 0.552× (z -5.0, q 9e-05, down in 26 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[BBC3]] (+0.58, fdr 1e-05), [[NINJ1]] (+0.58, fdr 1e-05), [[RILP]] (+0.55, fdr 3e-05); moves opposite to [[ABCE1]] (-0.57, fdr 1e-05), [[XRCC5]] (-0.56, fdr 3e-05), [[ARMC6]] (-0.55, fdr 2e-05).
> It sits in the **+** arm of [[Module 059]] (Amino acids regulate mTORC1).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[RNF144B]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 3 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3801.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **3.20×** | +9.9 | 3e-20 | 40/49 (C32, A-172, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.42×** | +8.0 | 3e-13 | 32/47 (SW480, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.47×** | +6.0 | 4e-07 | 32/47 (NCI-H1792, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.39×** | +5.4 | 1e-05 | 26/48 (KATO III, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **1.76×** | +4.8 | 2e-04 | 21/47 (C32, SW48, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.30×** | +4.2 | 0.002 | 25/47 (MIA PaCa-2, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.29×** | +4.1 | 0.004 | 21/48 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | 1.19× | +4.0 | 0.004 | 19/48 (SW480, hTERT-HPNE, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.24×** | +3.5 | 0.032 | 16/48 (NCI-H460, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~14% of this change | **1.23×** | +3.4 | 0.038 | 16/48 (HOP62, hTERT-HPNE, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.24×** | +3.4 | 0.038 | 21/48 (J82, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Cytarabine (drug)]] 5 µM |  | **1.23×** | +3.2 | 0.062 | 12/48 (NCI-H460, RKO, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[PF-06260933 (drug)]] 5 µM |  | **1.46×** | +3.2 | 0.063 | 15/48 (J82, CFPAC-1, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 5 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3801.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.521×** | -10.6 | 2e-23 | 36/45 (NCI-H1573, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.525×** | -10.0 | 3e-21 | 26/36 (LS 180, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[NG25 (drug)]] 5 µM |  | **0.552×** | -5.0 | 9e-05 | 26/47 (hTERT-HPNE, NCI-H1792, …) | top dose only | cell-cycle shift (explains ~2% here); noisy plate (z scaled) |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~9% of this change | **0.831×** | -4.2 | 0.003 | 20/48 (NCI-H2347, H4, …) | top dose only | position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.939× | -3.6 | 0.031 | 3/49 (NCI-H23, NCI-H2030, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **0.802×** | -3.6 | 0.031 | 22/48 (BT-474, Hs 766T, …) | top dose only |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.658×** | -3.6 | 0.031 | 16/48 (A549, NCI-H1573, …) | top dose only | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~15% of this change | **0.791×** | -3.5 | 0.031 | 20/39 (CFPAC-1, LS 180, …) | all doses, stronger at high dose | composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.05 per unit of S-phase module lfc, -0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3801. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[Hs 766T (line)]] | wt | 215 | 1 | 3 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 9.21× (z +9.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.297× (z -14.3) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H2347 (line)]] | alt | 63.9 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.313× (z -11.5) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 109 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.206× (z -15.7) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 86.7 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.110× (z -20.2) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 32.2 | 2 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.15× (z +9.8) | [[Dinaciclib (drug)]] 5 µM 0.323× (z -9.2) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 51.2 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.264× (z -10.9) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 79.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.268× (z -12.4) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 43.9 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 28.9× (z +10.5) | — |
| [[hTERT-HPNE (line)]] | wt | 103 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 15.3× (z +10.1) | [[Dinaciclib (drug)]] 5 µM 0.238× (z -9.8) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 26.9 | 2 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.95× (z +10.5) | — |
| [[MIA PaCa-2 (line)]] | alt | 35.2 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.44× (z +9.0) | [[Dinaciclib (drug)]] 0.5 µM 0.289× (z -8.8) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 75.7 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0809× (z -19.1) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 108 | 1 (1 ⚠) | 1 (1 ⚠) | [[Niclosamide (olamine) (drug)]] 5 µM 3.41× (z +10.4) ⚠ toxic | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.500× (z -8.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 45.3 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 11.8× (z +10.1) | — |
| [[A549 (line)]] | wt | 71.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.322× (z -10.6) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 40.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.161× (z -10.3) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 37.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.00× (z +9.2) | — |
| [[HS-578T (line)]] | alt | 90.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.334× (z -8.5) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 43.5 | 0 | 1 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.141× (z -8.8) ⚠ toxic |
| [[SNU-1 (line)]] | wt | 23.9 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.49× (z +8.5) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[SW1417 (line)]] | alt | 42.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.16× (z +8.9) | — |
| [[SW480 (line)]] | alt | 21.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.19× (z +9.8) | — |
| [[A-427 (line)]] | wt | 26.1 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 64.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 29.8 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 29.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 23.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 14.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 38.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 35.7 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 27.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 36.9 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 40.7 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 60.1 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 24.3 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 64.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 65.7 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 35.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 49.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 27.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 32.5 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 54.4 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 29.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 26.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 20.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 46.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 53.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 44.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 44.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 30.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3801), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*56 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BBC3]] | +0.58 | +0.52 / +0.56 | both halves | 1e-05 |  |
| [[NINJ1]] | +0.58 | +0.49 / +0.61 | both halves | 1e-05 | pathway: HALLMARK_P53_PATHWAY |
| [[RILP]] | +0.55 | +0.46 / +0.52 | both halves | 3e-05 |  |
| [[EFNB1]] | +0.55 | +0.45 / +0.56 | both halves | 3e-05 |  |
| [[CNNM4]] | +0.54 | +0.44 / +0.52 | both halves | 3e-05 |  |
| [[ARRDC2]] | +0.53 | +0.40 / +0.56 | both halves | 5e-05 |  |
| [[ABCG1]] | +0.53 | +0.38 / +0.54 | both halves | 6e-05 |  |
| [[SUSD6]] | +0.53 | +0.48 / +0.52 | both halves | 2e-05 |  |
| [[PTGES]] | +0.52 | +0.41 / +0.54 | both halves | 4e-05 |  |
| [[IRAK2]] | +0.52 | +0.44 / +0.55 | both halves | 3e-05 |  |
| [[ABTB2]] | +0.52 | +0.40 / +0.55 | both halves | 5e-05 |  |
| [[DCTN6-DT]] | +0.52 | +0.50 / +0.46 | both halves | 2e-05 |  |

## Genes that move opposite

*44 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ABCE1]] | -0.57 | -0.49 / -0.60 | both halves | 1e-05 |  |
| [[XRCC5]] | -0.56 | -0.43 / -0.54 | both halves | 3e-05 |  |
| [[ARMC6]] | -0.55 | -0.52 / -0.48 | both halves | 2e-05 |  |
| [[ZRANB3]] | -0.53 | -0.53 / -0.48 | both halves | 2e-05 |  |
| [[MRPS27]] | -0.52 | -0.49 / -0.52 | both halves | 1e-05 |  |
| [[CAPRIN1]] | -0.52 | -0.34 / -0.52 | both halves | 1e-04 |  |
| [[NUP188]] | -0.52 | -0.45 / -0.46 | both halves | 3e-05 |  |
| [[NUP155]] | -0.52 | -0.38 / -0.54 | both halves | 7e-05 |  |
| [[PPIL1]] | -0.51 | -0.49 / -0.45 | both halves | 3e-05 |  |
| [[MCM3AP]] | -0.51 | -0.38 / -0.48 | both halves | 6e-05 |  |
| [[TRRAP]] | -0.50 | -0.32 / -0.51 | both halves | 2e-04 |  |
| [[CEP20]] | -0.50 | -0.44 / -0.45 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RNF144B]] | B | RNF144B activity raises RNF19B's level | lines that do not express RNF144B (15) vs lines expressing it (35) | 1.44× lower at baseline in the lines without RNF144B | 0.059 | ⚠ within organs, on part of the lines; also absent: SPTLC3, TMEM92-AS1, ITGA2; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 059]] — Amino acids regulate mTORC1; 80 genes; this gene is in the **+** arm (projection on the module's main direction 0.492). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (24.1, -1.4); signed map (46.9, -1.2). **Vector** length 98.0, 23.7% of its response variance represented; |z| ≥ 3 in 1,034 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +4.5 | +4.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.4 | +2.4 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift | +3.3 | +2.4 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +2.6 | +1.2 |
|  | [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift | +2.4 | +1.3 |
|  | [[Amsacrine (drug)]] 5 µM |  | +2.3 | +2.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.1 | +1.9 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +2.0 | -0.3 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -5.0 | -2.6 |
|  | [[NG25 (drug)]] 5 µM |  | -4.4 | -5.0 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.3 | -3.6 |
|  | [[TAK-733 (drug)]] 5 µM |  | -4.0 | -3.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -3.2 | +5.4 |
|  | [[EX229 (drug)]] 5 µM |  | -2.7 | -2.0 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -2.6 | -1.2 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.4 | -0.8 |

## What is on record

|  |  |
|---|---|
| Name | ring finger protein 19B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p35.1 — chr1:32,936,445-32,964,809 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ90005, NKLAM; previously IBRDC3 |
| Gene groups (HGNC) | Ring finger proteins; RBR E3 ubiquitin ligases |
| Hallmark sets | TNFA_SIGNALING_VIA_NFKB, P53_PATHWAY |
| Reactome | 8 pathways, smallest: Activation of STAT3 by cadherin engagement; Adherens junctions interactions; Cell-cell junction organization |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6ZMZ0](https://www.uniprot.org/uniprotkb/Q6ZMZ0) (E3 ubiquitin-protein ligase RNF19B):

> E3 ubiquitin-protein ligase which accepts ubiquitin from E2 ubiquitin-conjugating enzymes UBE2L3 and UBE2L6 in the form of a thioester and then directly transfers the ubiquitin to targeted substrates, such as UCKL1. Involved in the cytolytic activity of natural killer cells and cytotoxic T-cells. Protects against staurosporin-induced cell death.

**Summary**, from NCBI Gene [127544](https://www.ncbi.nlm.nih.gov/gene/127544):

> This gene encodes a multi-pass membrane protein containing two RING-type and one IBR-type zinc finger motifs. The encoded protin is an E3 ubiquitin-protein ligase that plays a role in the cytotoxic effects of natural killer (NK) cells. Alternative splicing results in multiple transcript variants. There are pseudogenes for this gene on chromosomes X and Y in a possible pseudoautosomal region. [provided by RefSeq, Jul 2014]

**Accessions** — [HGNC:26886](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26886) · Entrez [127544](https://www.ncbi.nlm.nih.gov/gene/127544) · UniProt [Q6ZMZ0](https://www.uniprot.org/uniprotkb/Q6ZMZ0) · Ensembl [ENSG00000116514](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000116514)

## Data

Gene col 3801: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3801); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3801, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3801]; `tensor/DDL_lfc|DDL_z.npy` [3801]; `embed/gene_vectors.npy` [3801]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3801 or target_col == 3801). Every well: [[RNF19B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RNF19B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
