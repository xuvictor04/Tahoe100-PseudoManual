---
symbol: "PPP1R3D"
type: "gene"
col: 5379
ensembl_id: "ENSG00000132825"
name: "protein phosphatase 1 regulatory subunit 3D"
location: "20q13.33"
module: 12
arm: "+"
pooled_cpm: 6.04
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 12
n_dd_up_clean: 7
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/012"]
generated_by: "tahoemap"
---

# PPP1R3D

*protein phosphatase 1 regulatory subunit 3D* — 20q13.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (3 with an alert ⚠); the strongest is [[Adagrasib (drug)]] 0.05 µM: 1.21× (z +6.8, q 8e-09, up in 13 of 48 measured lines) ⚠ position not correctable. The strongest without an alert is [[Selinexor (drug)]] 5 µM: 1.43× (z +5.2, q 5e-05, up in 17 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (5 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.229× (z -15.2, q 0e+00, down in 39 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FAM217B]] (+0.62, fdr 7e-06, ⚠ same locus), [[HEIH]] (+0.61, fdr 1e-05), [[SEPHS2]] (+0.61, fdr 7e-06), [[ZNF32]] (+0.55, fdr 3e-05); moves opposite to [[QSOX2]] (-0.47, fdr 6e-05), [[BRD9]] (-0.46, fdr 2e-04), [[RMRP]] (-0.45, fdr 1e-04).
> It sits in the **+** arm of [[Module 012]] (mRNA Splicing - Major Pathway).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 3 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5379.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | **1.21×** | +6.8 | 8e-09 | 13/48 (NCI-H23, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 5 µM |  | **1.43×** | +5.2 | 5e-05 | 17/46 (NCI-H2030, Hs 766T, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~19% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.68×** | +5.2 | 5e-05 | 4/12 (Hs 766T, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.33×** | +4.1 | 0.005 | 17/40 (PANC-1, HT-29, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **1.41×** | +3.6 | 0.041 | 7/47 (A-172, KATO III, …) | inconsistent across doses |  |
| [[Entrectinib (drug)]] 5 µM |  | **1.40×** | +3.5 | 0.049 | 7/43 (NCI-H1573, RPMI-7951, …) | top dose only | position effect removed |
| [[Adagrasib (drug)]] 5 µM |  | **1.41×** | +3.4 | 0.058 | 9/45 (NCI-H23, NCI-H1792, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.38×** | +3.3 | 0.063 | 7/46 (LoVo, J82, …) | rises with dose | position effect removed |
| [[Cobimetinib (drug)]] 5 µM |  | **1.39×** | +3.3 | 0.069 | 9/42 (LoVo, SK-MEL-2, …) | rises with dose |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.30×** | +3.2 | 0.076 | 7/45 (LoVo, NCI-H1573, …) | all doses, flat | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 0.5 µM |  | 1.35× | +3.1 | 0.11 | 11/42 (RKO, A-427, …) | rises with dose | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 5 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5379.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.229×** | -15.2 | 0e+00 | 39/47 (SW480, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.317×** | -11.9 | 6e-30 | 31/39 (HT-29, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.325×** | -11.6 | 1e-28 | 35/44 (NCI-H460, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.569×** | -5.8 | 9e-07 | 29/44 (NCI-H1573, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.728×** | -4.6 | 5e-04 | 18/39 (A498, SK-MEL-2, …) | rises with dose | composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **0.442×** | -4.4 | 0.001 | 17/37 (LoVo, PANC-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.648×** | -4.3 | 0.001 | 15/30 (KATO III, LoVo, …) | top dose only | cell-cycle shift (explains ~13% here); position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **0.452×** | -4.3 | 0.001 | 17/43 (J82, RPMI-7951, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~8% here); composition shift; noisy plate (z scaled); position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.665×** | -4.2 | 0.002 | 19/47 (MIA PaCa-2, LOX-IMVI, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.679×** | -4.0 | 0.004 | 12/47 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.684×** | -3.9 | 0.005 | 14/44 (NCI-H460, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.716×** | -3.3 | 0.046 | 18/44 (A498, A-427, …) | inconsistent across doses | composition shift; position effect removed |
| [[Ropivacaine (hydrochloride monohydrate) (drug)]] 5 µM |  | 0.811× | -3.0 | 0.10 | 8/45 (HT-29, COLO 205, …) | rises with dose | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.03 per unit of S-phase module lfc, -0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5379. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 8.26 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.112× (z -17.1) ⚠ cell-cycle shift, explains ~31% of this change |
| [[NCI-H460 (line)]] | wt | 7.79 | 0 | 3 | — | [[Digitoxin (drug)]] 0.05 µM 0.0654× (z -15.3) |
| [[Hs 766T (line)]] | wt | 15.9 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.146× (z -9.2) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.159× (z -8.8) |
| [[HT-29 (line)]] | alt | 15.9 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0696× (z -14.7) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.162× (z -10.1) |
| [[J82 (line)]] | alt | 5.15 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.105× (z -9.6) |
| [[KATO III (line)]] | alt | 6.56 | 0 | 2 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0503× (z -12.9) ⚠ toxic · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.114× (z -9.7) |
| [[LoVo (line)]] | wt | 5.36 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.135× (z -9.5) |
| [[SW480 (line)]] | alt | 5.68 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0777× (z -13.1) |
| [[HCT15 (line)]] | alt | 4.81 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0377× (z -9.0) |
| [[NCI-H1573 (line)]] | alt | 6.02 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0719× (z -10.7) |
| [[NCI-H2030 (line)]] | alt | 7.28 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.124× (z -9.0) |
| [[NCI-H23 (line)]] | alt | 6.98 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0775× (z -9.9) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 6.79 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.156× (z -10.4) |
| [[SK-MEL-2 (line)]] | alt | 9.52 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.211× (z -9.3) ⚠ cell-cycle shift, explains ~31% of this change |
| [[SNU-423 (line)]] | alt | 5.18 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0236× (z -12.5) |
| [[A-172 (line)]] | wt | 2.03 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 7.33 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.76 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 5.97 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.41 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.40 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.57 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.70 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.74 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.09 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.11 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 4.49 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.71 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.49 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.61 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.64 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.93 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 5.10 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.72 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 4.24 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.32 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.14 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.43 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.49 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 6.27 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 6.01 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.56 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 7.86 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.71 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.97 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.00 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.35 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5379), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FAM217B]] | +0.62 | +0.65 / +0.60 | both halves | 7e-06 | STRING 546; ⚠ same locus (0.0 kb: neighbours can correlate without regulation) |
| [[HEIH]] | +0.61 | +0.54 / +0.62 | both halves | 1e-05 |  |
| [[SEPHS2]] | +0.61 | +0.60 / +0.60 | both halves | 7e-06 |  |
| [[ZNF32]] | +0.55 | +0.45 / +0.54 | both halves | 3e-05 |  |
| [[FANCF]] | +0.55 | +0.59 / +0.47 | both halves | 2e-05 |  |
| [[TMEM11]] | +0.55 | +0.37 / +0.56 | both halves | 9e-05 |  |
| [[ZNF639]] | +0.54 | +0.46 / +0.51 | both halves | 3e-05 |  |
| [[ZBTB14]] | +0.54 | +0.44 / +0.50 | both halves | 3e-05 |  |
| [[CDC40]] | +0.53 | +0.50 / +0.46 | both halves | 2e-05 |  |
| [[HDDC3]] | +0.53 | +0.55 / +0.42 | both halves | 4e-05 |  |
| [[MRPL44]] | +0.51 | +0.38 / +0.54 | both halves | 6e-05 |  |
| [[RDH14]] | +0.51 | +0.47 / +0.50 | both halves | 2e-05 |  |
| [[PLEKHA3]] | +0.50 | +0.57 / +0.35 | both halves | 1e-04 |  |

## Genes that move opposite

*14 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[QSOX2]] | -0.47 | -0.44 / -0.38 | both halves | 6e-05 |  |
| [[BRD9]] | -0.46 | -0.30 / -0.49 | both halves | 2e-04 |  |
| [[RMRP]] | -0.45 | -0.35 / -0.49 | both halves | 1e-04 |  |
| [[PPP3CB]] | -0.45 | -0.29 / -0.43 | both halves | 2e-04 |  |
| [[ODF2]] | -0.45 | -0.50 / -0.38 | both halves | 6e-05 |  |
| [[LENG8]] | -0.45 | -0.43 / -0.40 | both halves | 5e-05 |  |
| [[ARHGAP4]] | -0.45 | -0.33 / -0.49 | both halves | 1e-04 |  |
| [[AGRN]] | -0.44 | -0.33 / -0.42 | both halves | 1e-04 |  |
| [[AHCY]] | -0.44 | -0.37 / -0.38 | both halves | 8e-05 |  |
| [[PLCB3]] | -0.44 | -0.55 / -0.39 | both halves | 6e-05 |  |
| [[PDLIM7]] | -0.44 | -0.45 / -0.40 | both halves | 5e-05 |  |
| [[SEPTIN10]] | -0.43 | -0.42 / -0.42 | both halves | 4e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 012]] — mRNA Splicing - Major Pathway; 215 genes; this gene is in the **+** arm (projection on the module's main direction 0.431). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-46.4, -5.4); signed map (-8.7, -9.4). **Vector** length 50.4, 6.62% of its response variance represented; |z| ≥ 3 in 916 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +3.1 | +5.2 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +1.9 | -0.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.7 | +3.3 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | +1.6 | +1.7 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | +1.5 | +2.0 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.4 | +1.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.3 | -1.0 |
|  | [[Adagrasib (drug)]] 5 µM |  | +1.3 | +3.4 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | +1.3 | +3.2 |
| fall | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -2.9 | -15.2 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -2.6 | -11.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -2.4 | -1.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -2.2 | +5.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -2.1 | -5.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.5 | +0.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.4 | +0.4 |
|  | [[TAK-733 (drug)]] 0.05 µM |  | -1.2 | -2.1 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -1.1 | -2.8 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.1 | -0.6 |

## What is on record

|  |  |
|---|---|
| Name | protein phosphatase 1 regulatory subunit 3D |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20q13.33 — chr20:59,936,663-59,940,305 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously PPP1R6 |
| Gene groups (HGNC) | Protein phosphatase 1 regulatory subunits |
| Matched by | ensembl_id |

**Function**, from UniProt [O95685](https://www.uniprot.org/uniprotkb/O95685) (Protein phosphatase 1 regulatory subunit 3D):

> Seems to act as a glycogen-targeting subunit for PP1. PP1 is essential for cell division, and participates in the regulation of glycogen metabolism, muscle contractility and protein synthesis.

**Summary**, from NCBI Gene [5509](https://www.ncbi.nlm.nih.gov/gene/5509):

> Phosphorylation of serine and threonine residues in proteins is a crucial step in the regulation of many cellular functions ranging from hormonal regulation to cell division and even short-term memory. The level of phosphorylation is controlled by the opposing actions of protein kinases and protein phosphatases. Protein phosphatase 1 (PP1) is 1 of 4 major serine/threonine-specific protein phosphatases which have been identified in eukaryotic cells. PP1 associates with various regulatory …

**Accessions** — [HGNC:9294](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9294) · Entrez [5509](https://www.ncbi.nlm.nih.gov/gene/5509) · UniProt [O95685](https://www.uniprot.org/uniprotkb/O95685) · Ensembl [ENSG00000132825](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000132825)

## Data

Gene col 5379: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5379); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5379, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5379]; `tensor/DDL_lfc|DDL_z.npy` [5379]; `embed/gene_vectors.npy` [5379]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5379 or target_col == 5379). Every well: [[PPP1R3D — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PPP1R3D.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
