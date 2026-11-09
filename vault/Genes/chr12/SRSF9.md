---
symbol: "SRSF9"
type: "gene"
col: 3280
ensembl_id: "ENSG00000111786"
name: "serine and arginine rich splicing factor 9"
location: "12q24.31"
module: 20
arm: "-"
pooled_cpm: 83.69
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 0
n_dd_up_clean: 0
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/020", "evidence-flagged-only"]
generated_by: "tahoemap"
---

# SRSF9

*serine and arginine rich splicing factor 9* — 12q24.31

## At a glance

> [!summary] In this data
> ⚠ It is in the vector space only through drug-doses that carry an alert for it (its significant pooled drug-doses and per-line responses; `embed/genes.parquet` evidence_flagged_only): its vector, partners and module rest on changes that may come from what those drug-doses did to the cells rather than from its own regulation.
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.51× (z +9.9, q 2e-20, up in 47 of 49 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 11 lines (A498 4.22×, A549 4.17×, SHP-77 3.97×, PANC-1 3.33×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change); [[Dinaciclib (drug)]] 5 µM in 3 lines (A-172 3.33×, A498 4.01×, PANC-1 3.28×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (NCI-H2030 2.97×; ⚠ cell-cycle shift, would explain all of this change).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Epirubicin (hydrochloride) (drug)]] 5 µM in 1 line (SK-MEL-2 0.321×; ⚠ cell-cycle shift, explains ~0% of this change).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DRAP1]] (+0.58, fdr 1e-05), [[KCTD11]] (+0.57, fdr 7e-06), [[CCDC88A]] (+0.56, fdr 8e-05); moves opposite to [[TMEM268]] (-0.65, fdr 1e-05), [[ANGEL2]] (-0.62, fdr 2e-05), [[SUPV3L1]] (-0.62, fdr 1e-05).
> It sits in the **-** arm of [[Module 020]] (Cap-dependent Translation Initiation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[NNT]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 4 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3280.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 11 lines (A498 4.22×, A549 4.17×, SHP-77 3.97×, PANC-1 3.33×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change); [[Dinaciclib (drug)]] 5 µM in 3 lines (A-172 3.33×, A498 4.01×, PANC-1 3.28×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (NCI-H2030 2.97×; ⚠ cell-cycle shift, would explain all of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **2.51×** | +9.9 | 2e-20 | 47/49 (A498, A549, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **2.17×** | +8.0 | 3e-13 | 40/43 (A-172, A498, …) | all doses, stronger at high dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~49% of this change | **1.64×** | +5.3 | 2e-05 | 43/48 (PANC-1, A-427, …) | inconsistent across doses | low cells (technical?) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **1.74×** | +4.9 | 1e-04 | 34/45 (A-427, A498, …) | all doses, stronger at high dose | composition shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 3280.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Epirubicin (hydrochloride) (drug)]] 5 µM in 1 line (SK-MEL-2 0.321×; ⚠ cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Anethole trithione (drug)]] 0.5 µM |  | 0.731× | -3.4 | 0.42 | 34/48 (RPMI-7951, MIA PaCa-2, …) | rises with dose |  |
| [[GSK1059615 (drug)]] 5 µM |  | 0.485× | -3.2 | 0.43 | 34/49 (CHP-212, LoVo, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.16 per unit of S-phase module lfc, +0.45 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3280. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 77.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.33× (z +11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[A498 (line)]] | wt | 55.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.22× (z +11.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 85.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.80× (z +10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[NCI-H2030 (line)]] | alt | 68.3 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.97× (z +11.6) ⚠ cell-cycle shift, would explain all of this change | — |
| [[NCI-H460 (line)]] | wt | 71.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.82× (z +9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[PANC-1 (line)]] | alt | 91.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.33× (z +10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[A549 (line)]] | wt | 70.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.17× (z +11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[HEC-1-A (line)]] | alt | 95.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.98× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[HOP62 (line)]] | alt | 84.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.62× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[HS-578T (line)]] | alt | 70.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.68× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[HT-29 (line)]] | alt | 99.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.70× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[KATO III (line)]] | alt | 91.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.92× (z +10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[NCI-H23 (line)]] | alt | 115 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.36× (z +10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[SHP-77 (line)]] | alt | 82.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.97× (z +11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 71.2 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.321× (z -8.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SNU-423 (line)]] | alt | 60.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.41× (z +9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[SW480 (line)]] | alt | 77.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.12× (z +10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[A-427 (line)]] | wt | 95.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 90.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 81.9 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 94.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 95.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 50.1 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 89.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 72.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 83.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 87.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 149 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 84.4 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 52.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 68.2 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 97.0 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 118 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 97.3 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 95.6 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 116 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 65.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 70.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 88.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 82.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 80.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 49.4 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 113 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 78.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 62.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 76.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 96.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 79.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 75.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 86.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3280), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*47 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DRAP1]] | +0.58 | +0.50 / +0.59 | both halves | 1e-05 |  |
| [[KCTD11]] | +0.57 | +0.60 / +0.63 | both halves | 7e-06 |  |
| [[CCDC88A]] | +0.56 | +0.49 / +0.37 | both halves | 8e-05 |  |
| [[METTL23]] | +0.56 | +0.55 / +0.65 | both halves | 1e-05 |  |
| [[TXNDC17]] | +0.54 | +0.44 / +0.54 | both halves | 3e-05 |  |
| [[RGP1]] | +0.54 | +0.45 / +0.47 | both halves | 3e-05 |  |
| [[GGT7]] | +0.54 | +0.54 / +0.35 | both halves | 1e-04 |  |
| [[MAPK8IP3]] | +0.53 | +0.53 / +0.32 | both halves | 2e-04 |  |
| [[GALE]] | +0.53 | +0.47 / +0.54 | both halves | 2e-05 |  |
| [[GOLT1A]] | +0.52 | +0.45 / +0.51 | both halves | 3e-05 |  |
| [[SYP]] | +0.52 | +0.35 / +0.35 | both halves | 1e-04 |  |
| [[ST3GAL5]] | +0.52 | +0.40 / +0.36 | both halves | 9e-05 |  |

## Genes that move opposite

*53 of its nearest partners move opposite, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM268]] | -0.65 | -0.65 / -0.49 | both halves | 1e-05 |  |
| [[ANGEL2]] | -0.62 | -0.53 / -0.47 | both halves | 2e-05 |  |
| [[SUPV3L1]] | -0.62 | -0.53 / -0.51 | both halves | 1e-05 |  |
| [[PMS2]] | -0.58 | -0.50 / -0.53 | both halves | 1e-05 |  |
| [[SETMAR]] | -0.58 | -0.40 / -0.46 | both halves | 5e-05 |  |
| [[PON2]] | -0.56 | -0.52 / -0.58 | both halves | 1e-05 |  |
| [[STRADB]] | -0.55 | -0.54 / -0.44 | both halves | 3e-05 |  |
| [[RPUSD4]] | -0.54 | -0.45 / -0.60 | both halves | 3e-05 |  |
| [[SLC9B2]] | -0.53 | -0.45 / -0.44 | both halves | 3e-05 |  |
| [[APEX1]] | -0.53 | -0.48 / -0.50 | both halves | 2e-05 |  |
| [[NAXD]] | -0.53 | -0.37 / -0.52 | both halves | 9e-05 |  |
| [[EPM2A]] | -0.52 | -0.37 / -0.27 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NNT]] | B | NNT activity lowers SRSF9's level | lines that do not express NNT (6) vs lines expressing it (44) | 1.17× higher at baseline in the lines without NNT | 0.058 | ⚠ within organs, on part of the lines; co-absent genes |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 020]] — Cap-dependent Translation Initiation; 191 genes; this gene is in the **-** arm (projection on the module's main direction -0.415). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- ⚠ **In the space only through flagged drug-doses**: its significant pooled drug-doses and per-line responses all carry an alert (`embed/genes.parquet` evidence_flagged_only), so its module and partners may reflect what those drug-doses did to the cells.
- **Nodal map** (x, y) = (-9.1, 14.9); signed map (3.4, 24.5). **Vector** length 64.1, 19.4% of its response variance represented; |z| ≥ 3 in 439 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.7 | +1.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | +2.6 | +1.8 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +2.6 | +1.2 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +2.4 | +2.0 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +2.2 | +1.7 |
|  | [[Ritonavir (drug)]] 5 µM |  | +1.5 | +2.8 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +1.4 | +1.2 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.4 | -0.8 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +1.4 | +1.7 |
|  | [[Belinostat (drug)]] 0.05 µM |  | +1.2 | +2.1 |
| fall | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -4.3 | +1.1 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -4.2 | +0.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -4.2 | +0.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | -3.8 | +4.9 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -3.5 | -2.2 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.0 | +0.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | -1.6 | -1.3 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.4 | +1.7 |
|  | [[Pralsetinib (drug)]] 5 µM |  | -1.4 | +0.3 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.4 | -3.2 |

## What is on record

|  |  |
|---|---|
| Name | serine and arginine rich splicing factor 9 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q24.31 — chr12:120,461,672-120,495,946 (-) |
| Ensembl biotype | protein_coding |
| Also known as | SRp30c; previously SFRS9 |
| Gene groups (HGNC) | RNA binding motif containing; Serine and arginine rich splicing factors |
| Reactome | 11 pathways, smallest: Transport of Mature mRNA derived from an Intron-Containing Transcript; Transport of Mature Transcript to Cytoplasm; mRNA Polyadenylation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q13242](https://www.uniprot.org/uniprotkb/Q13242) (Serine/arginine-rich splicing factor 9):

> Plays a role in constitutive splicing and can modulate the selection of alternative splice sites. Represses the splicing of MAPT/Tau exon 10.

**Summary**, from NCBI Gene [8683](https://www.ncbi.nlm.nih.gov/gene/8683):

> The protein encoded by this gene is a member of the serine/arginine (SR)-rich family of pre-mRNA splicing factors, which constitute part of the spliceosome. Each of these factors contains an RNA recognition motif (RRM) for binding RNA and an RS domain for binding other proteins. The RS domain is rich in serine and arginine residues and facilitates interaction between different SR splicing factors. In addition to being critical for mRNA splicing, the SR proteins have also been shown to be …

**Accessions** — [HGNC:10791](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10791) · Entrez [8683](https://www.ncbi.nlm.nih.gov/gene/8683) · UniProt [Q13242](https://www.uniprot.org/uniprotkb/Q13242) · Ensembl [ENSG00000111786](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000111786)

## Data

Gene col 3280: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3280); `tables/drug_effects.parquet` (6 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3280, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3280]; `tensor/DDL_lfc|DDL_z.npy` [3280]; `embed/gene_vectors.npy` [3280]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3280 or target_col == 3280). Every well: [[SRSF9 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SRSF9.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
