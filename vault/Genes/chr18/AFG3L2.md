---
symbol: "AFG3L2"
type: "gene"
col: 6510
ensembl_id: "ENSG00000141385"
name: "AFG3 like matrix AAA peptidase subunit 2"
location: "18p11.21"
module: 1
arm: "+"
pooled_cpm: 75.17
n_lines_expressing: 49
n_dd_up: 11
n_dd_down: 2
n_dd_up_clean: 6
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/001"]
generated_by: "tahoemap"
---

# AFG3L2

*AFG3 like matrix AAA peptidase subunit 2* — 18p11.21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.35× (z +10.1, q 4e-21, up in 30 of 47 measured lines) ⚠ cell-cycle shift, explains ~43% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 1.43× (z +9.3, q 6e-18, up in 31 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Tucidinostat (drug)]] 0.5 µM: 0.780× (z -6.5, q 5e-08, down in 33 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 2 lines (HEC-1-A 0.541×, RKO 0.471×; ⚠ cell-cycle shift, explains ~0% of this change); [[Auranofin (drug)]] 5 µM in 1 line (A-427 0.517×); [[Niclosamide (olamine) (drug)]] 5 µM in 1 line (SNU-1 0.350×; ⚠ toxic; cell-cycle shift, explains ~84% of this change); [[TAK-901 (drug)]] 5 µM in 1 line (SNU-1 0.0926×).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CLUH]] (+0.61, fdr 7e-06), [[SPOUT1]] (+0.60, fdr 1e-05), [[RIOK1]] (+0.56, fdr 2e-05); moves opposite to [[RTCA-AS1]] (-0.56, fdr 4e-04), [[TMSB4X]] (-0.52, fdr 4e-05), [[ITM2C]] (-0.51, fdr 3e-05).
> It sits in the **+** arm of [[Module 001]] (rRNA processing).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TERT]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 8 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6510.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **1.35×** | +10.1 | 4e-21 | 30/47 (AsPC-1, COLO 205, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.43×** | +9.3 | 6e-18 | 31/47 (HOP62, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.34×** | +7.6 | 4e-12 | 32/47 (NCI-H460, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **1.28×** | +6.3 | 4e-08 | 25/47 (HOP62, NCI-H1573, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~80% of this change | **1.25×** | +5.8 | 9e-07 | 23/48 (COLO 205, LS 180, …) | all doses, flat | composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **1.24×** | +5.6 | 2e-06 | 23/47 (HOP62, A-172, …) | rises with dose |  |
| [[EX229 (drug)]] 5 µM |  | **1.71×** | +5.6 | 2e-06 | 32/47 (NCI-H460, MIA PaCa-2, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **1.68×** | +5.4 | 4e-06 | 28/47 (NCI-H460, MIA PaCa-2, …) | top dose only | noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~59% of this change | 1.20× | +4.7 | 1e-04 | 21/47 (NCI-H1573, HOP62, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~65% of this change | 1.20× | +4.5 | 4e-04 | 20/47 (AsPC-1, NCI-H1573, …) | rises with dose | composition shift |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.53×** | +4.4 | 5e-04 | 20/47 (NCI-H460, SNU-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **1.47×** | +4.0 | 0.003 | 15/47 (MIA PaCa-2, NCI-H460, …) | top dose only | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 1.15× | +3.7 | 0.011 | 15/47 (MIA PaCa-2, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[EX229 (drug)]] 0.05 µM |  | 1.15× | +3.4 | 0.026 | 12/47 (LoVo, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~41% of this change | 1.12× | +3.0 | 0.091 | 19/47 (SW480, HOP62, …) | rises with dose |  |
| [[venetoclax (drug)]] 5 µM |  | **1.33×** | +3.0 | 0.093 | 10/47 (NCI-H460, SNU-1, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 6510.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 2 lines (HEC-1-A 0.541×, RKO 0.471×; ⚠ cell-cycle shift, explains ~0% of this change); [[Auranofin (drug)]] 5 µM in 1 line (A-427 0.517×); [[Niclosamide (olamine) (drug)]] 5 µM in 1 line (SNU-1 0.350×; ⚠ toxic; cell-cycle shift, explains ~84% of this change); [[TAK-901 (drug)]] 5 µM in 1 line (SNU-1 0.0926×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.780×** | -6.5 | 5e-08 | 33/47 (HOP62, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.830×** | -6.1 | 3e-07 | 23/47 (KATO III, SNU-1, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 5 µM |  | 0.744× | -3.1 | 0.36 | 13/48 (SNU-1, J82, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.14 per unit of S-phase module lfc, +0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6510. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 89.0 | 0 | 2 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.618× (z -9.4) ⚠ cell-cycle shift, would explain all of this change |
| [[SNU-1 (line)]] | wt | 93.3 | 0 | 2 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.350× (z -9.9) ⚠ toxic; cell-cycle shift, explains ~84% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.0926× (z -9.4) |
| [[A-427 (line)]] | wt | 225 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.517× (z -10.9) |
| [[AsPC-1 (line)]] | alt | 66.2 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.33× (z +13.8) ⚠ cell-cycle shift, explains ~43% of this change | — |
| [[C32 (line)]] | wt | 61.6 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.21× (z +10.1) ⚠ cell-cycle shift, explains ~43% of this change | — |
| [[COLO 205 (line)]] | alt | 41.0 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.92× (z +10.4) ⚠ cell-cycle shift, explains ~43% of this change | — |
| [[HOP62 (line)]] | alt | 109 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.21× (z +12.8) | — |
| [[HT-29 (line)]] | alt | 91.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 2.08× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | — |
| [[NCI-H1573 (line)]] | alt | 55.7 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.98× (z +9.3) ⚠ cell-cycle shift, explains ~43% of this change | — |
| [[NCI-H1792 (line)]] | alt | 37.2 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.37× (z +9.4) ⚠ cell-cycle shift, explains ~43% of this change | — |
| [[RKO (line)]] | wt | 103 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.471× (z -8.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 71.3 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 53.5 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 48.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 85.6 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 107 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 105 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 13.9 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 56.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 57.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 74.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 83.8 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 107 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 56.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 51.2 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 97.2 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 66.0 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 112 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 57.9 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 74.0 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 135 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 66.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 52.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 115 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 35.1 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 56.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 66.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 120 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 32.7 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 80.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 47.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 64.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 66.4 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 42.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 55.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 58.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 52.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 71.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 99.9 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 74.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6510), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CLUH]] | +0.61 | +0.58 / +0.62 | both halves | 7e-06 |  |
| [[SPOUT1]] | +0.60 | +0.53 / +0.62 | both halves | 1e-05 |  |
| [[RIOK1]] | +0.56 | +0.54 / +0.48 | both halves | 2e-05 |  |
| [[PDCD11]] | +0.56 | +0.49 / +0.60 | both halves | 1e-05 | STRING 579 |
| [[EIF5B]] | +0.56 | +0.61 / +0.51 | both halves | 1e-05 | STRING 436 |
| [[NOP14]] | +0.56 | +0.66 / +0.55 | both halves | 1e-05 |  |
| [[RRP1]] | +0.55 | +0.43 / +0.60 | both halves | 3e-05 |  |
| [[PWP2]] | +0.55 | +0.42 / +0.58 | both halves | 4e-05 |  |
| [[IMP4]] | +0.55 | +0.52 / +0.61 | both halves | 1e-05 |  |
| [[POGK]] | +0.55 | +0.58 / +0.52 | both halves | 1e-05 |  |
| [[RBM28]] | +0.55 | +0.56 / +0.51 | both halves | 1e-05 |  |
| [[LETM1]] | +0.55 | +0.57 / +0.60 | both halves | 1e-05 | pathway: Mitochondrial calcium ion transport; STRING 415 |

## Genes that move opposite

*15 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RTCA-AS1]] | -0.56 | -0.24 / -0.46 | both halves | 4e-04 |  |
| [[TMSB4X]] | -0.52 | -0.41 / -0.65 | both halves | 4e-05 |  |
| [[ITM2C]] | -0.51 | -0.44 / -0.57 | both halves | 3e-05 |  |
| [[PSAP]] | -0.50 | -0.42 / -0.58 | both halves | 4e-05 |  |
| [[LAPTM4A]] | -0.50 | -0.57 / -0.52 | both halves | 1e-05 |  |
| [[MKLN1-AS]] | -0.50 | -0.07 / -0.56 | ⚠ one half (not replicated) | 0.004 |  |
| [[ITM2B]] | -0.50 | -0.37 / -0.53 | both halves | 8e-05 |  |
| [[VAMP1]] | -0.50 | -0.27 / -0.54 | both halves | 3e-04 |  |
| [[SRP14]] | -0.50 | -0.31 / -0.43 | both halves | 2e-04 |  |
| [[ERO1B]] | -0.49 | -0.14 / -0.61 | ⚠ one half (not replicated) | 0.002 |  |
| [[IDS]] | -0.48 | -0.48 / -0.60 | both halves | 2e-05 |  |
| [[YPEL5]] | -0.48 | -0.37 / -0.48 | both halves | 8e-05 |  |
| [[GNAS]] | -0.47 | -0.30 / -0.47 | both halves | 2e-04 |  |
| [[MXD1]] | -0.47 | -0.47 / -0.58 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TERT]] | B | TERT activity raises AFG3L2's level | lines that do not express TERT (13) vs lines expressing it (37) | 1.51× lower at baseline in the lines without TERT | 0.040 | ⚠ within organs, on part of the lines; also absent: SAMD11, MIR1915HG, LNC-LBCS |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 001]] — rRNA processing; 298 genes; this gene is in the **+** arm (projection on the module's main direction 0.539). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-16.8, -40.9); signed map (1.5, -47.7). **Vector** length 83.5, 18.6% of its response variance represented; |z| ≥ 3 in 721 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +6.0 | +7.6 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | +4.1 | +10.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.0 | +9.3 |
|  | [[EX229 (drug)]] 5 µM |  | +3.6 | +5.6 |
|  | [[TAK-733 (drug)]] 5 µM |  | +3.2 | +5.4 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +3.0 | +4.4 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +2.8 | +4.0 |
|  | [[venetoclax (drug)]] 5 µM |  | +2.7 | +3.0 |
| fall | [[Tucidinostat (drug)]] 0.5 µM |  | -5.3 | -6.5 |
|  | [[Auranofin (drug)]] 5 µM |  | -5.3 | -2.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -5.2 | -6.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.9 | -2.0 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -3.2 | -2.4 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -2.3 | -2.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.6 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | AFG3 like matrix AAA peptidase subunit 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 18p11.21 — chr18:12,328,944-12,377,227 (-) |
| Ensembl biotype | protein_coding |
| Also known as | SPAX5; previously SCA28 |
| Gene groups (HGNC) | AAA ATPases |
| Hallmark sets | OXIDATIVE_PHOSPHORYLATION |
| Reactome | 4 pathways, smallest: Processing of SMDT1; Mitochondrial calcium ion transport; Mitochondrial protein degradation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y4W6](https://www.uniprot.org/uniprotkb/Q9Y4W6) (Mitochondrial inner membrane m-AAA protease component AFG3L2):

> Catalytic component of the m-AAA protease, a protease that plays a key role in proteostasis of inner mitochondrial membrane proteins, and which is essential for axonal and neuron development. AFG3L2 possesses both ATPase and protease activities: the ATPase activity is required to unfold substrates, threading them into the internal proteolytic cavity for hydrolysis into small peptide fragments. The m-AAA protease carries out quality control in the inner membrane of the mitochondria by mediating …

**Summary**, from NCBI Gene [10939](https://www.ncbi.nlm.nih.gov/gene/10939):

> This gene encodes a protein localized in mitochondria and closely related to paraplegin. The paraplegin gene is responsible for an autosomal recessive form of hereditary spastic paraplegia. This gene is a candidate gene for other hereditary spastic paraplegias or neurodegenerative disorders. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:315](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:315) · Entrez [10939](https://www.ncbi.nlm.nih.gov/gene/10939) · UniProt [Q9Y4W6](https://www.uniprot.org/uniprotkb/Q9Y4W6) · Ensembl [ENSG00000141385](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000141385)

## Data

Gene col 6510: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6510); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6510, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6510]; `tensor/DDL_lfc|DDL_z.npy` [6510]; `embed/gene_vectors.npy` [6510]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6510 or target_col == 6510). Every well: [[AFG3L2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/AFG3L2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
