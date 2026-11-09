---
symbol: "LSM8"
type: "gene"
col: 4889
ensembl_id: "ENSG00000128534"
name: "LSM8 homolog, U6 small nuclear RNA associated"
location: "7q31.31"
module: 15
arm: "+"
pooled_cpm: 41.31
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 2
n_dd_up_clean: 9
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/015"]
generated_by: "tahoemap"
---

# LSM8

*LSM8 homolog, U6 small nuclear RNA associated* — 7q31.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.69× (z +13.6, q 2e-39, up in 42 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[TAK-901 (drug)]] 5 µM: 0.436× (z -8.0, q 8e-13, down in 38 of 49 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 3 lines (Panc 03.27 0.173×, HEC-1-A 0.264×, SW480 0.396×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (NCI-H23 0.122×, C-33 A 0.151×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change); [[Dinaciclib (drug)]] 0.5 µM in 1 line (RKO 0.209×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TRAPPC13]] (+0.70, fdr 7e-06), [[TMEM267]] (+0.66, fdr 1e-05), [[RWDD3]] (+0.65, fdr 1e-05); moves opposite to [[CORO1C]] (-0.60, fdr 1e-05), [[CDC42]] (-0.56, fdr 8e-06), [[CAPZB]] (-0.55, fdr 1e-05).
> It sits in the **+** arm of [[Module 015]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 6 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4889.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.69×** | +13.6 | 2e-39 | 42/48 (SW1417, SW 900, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.83×** | +10.7 | 3e-24 | 37/47 (SW480, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.68×** | +9.2 | 9e-18 | 37/48 (SW480, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.34×** | +7.6 | 5e-12 | 30/48 (C32, LoVo, …) | rises with dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.45×** | +6.6 | 4e-09 | 33/48 (SW480, C32, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.31×** | +5.0 | 5e-05 | 23/48 (C32, C-33 A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~15% of this change | **1.29×** | +4.7 | 2e-04 | 23/47 (NCI-H23, A-172, …) | inconsistent across doses | low cells (technical?) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~19% of this change | **1.25×** | +4.0 | 0.004 | 21/48 (LoVo, C32, …) | rises with dose | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.24×** | +4.0 | 0.004 | 21/48 (PANC-1, RKO, …) | top dose only |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.24×** | +4.0 | 0.004 | 21/48 (LoVo, NCI-H23, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~25% of this change | **1.24×** | +3.8 | 0.007 | 18/47 (A-172, NCI-H23, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | 1.19× | +3.3 | 0.053 | 16/48 (A-172, CFPAC-1, …) | rises with dose |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.27×** | +3.2 | 0.068 | 15/48 (Hs 766T, A549, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | 1.18× | +3.1 | 0.076 | 9/48 (NCI-H2347, HEC-1-A, …) | inconsistent across doses |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.26×** | +3.1 | 0.076 | 13/47 (HCT15, Hs 766T, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 4889.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 3 lines (Panc 03.27 0.173×, HEC-1-A 0.264×, SW480 0.396×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (NCI-H23 0.122×, C-33 A 0.151×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change); [[Dinaciclib (drug)]] 0.5 µM in 1 line (RKO 0.209×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **0.436×** | -8.0 | 8e-13 | 38/49 (PANC-1, SW480, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.503×** | -6.6 | 1e-08 | 30/48 (C32, SW480, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | 0.839× | -3.1 | 0.38 | 18/39 (Panc 03.27, HEC-1-A, …) | top dose only | composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.15 per unit of S-phase module lfc, +0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4889. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 41.5 | 2 (1 ⚠) | 1 (1 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.12× (z +9.7) | [[Dinaciclib (drug)]] 5 µM 0.396× (z -11.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[MIA PaCa-2 (line)]] | alt | 33.7 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.82× (z +11.5) | — |
| [[Panc 03.27 (line)]] | alt | 37.3 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.08× (z +8.7) | [[Dinaciclib (drug)]] 5 µM 0.173× (z -14.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[RKO (line)]] | wt | 60.1 | 1 | 1 (1 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.86× (z +8.8) | [[Dinaciclib (drug)]] 0.5 µM 0.209× (z -13.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[C-33 A (line)]] | alt | 61.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.151× (z -15.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change |
| [[C32 (line)]] | wt | 83.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.48× (z +12.7) | — |
| [[HEC-1-A (line)]] | alt | 37.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.264× (z -13.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HS-578T (line)]] | alt | 32.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.64× (z +11.1) | — |
| [[LoVo (line)]] | wt | 53.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.86× (z +10.4) | — |
| [[NCI-H23 (line)]] | alt | 51.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.122× (z -18.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change |
| [[PANC-1 (line)]] | alt | 38.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.97× (z +11.0) | — |
| [[SK-MEL-2 (line)]] | alt | 47.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.41× (z +10.3) | — |
| [[SW 900 (line)]] | alt | 42.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.09× (z +12.8) | — |
| [[SW1417 (line)]] | alt | 55.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.45× (z +13.0) | — |
| [[A-172 (line)]] | wt | 50.2 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 31.3 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 83.9 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 30.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 58.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 31.7 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 30.8 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 29.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 29.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 33.1 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 38.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 30.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 24.4 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 30.3 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 32.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 50.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 30.2 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 38.8 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 55.7 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 32.7 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 49.2 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 29.9 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 33.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 34.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 32.1 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 39.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 36.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 43.1 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 32.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 38.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 34.6 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 32.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 43.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 53.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 48.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4889), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*72 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TRAPPC13]] | +0.70 | +0.61 / +0.64 | both halves | 7e-06 |  |
| [[TMEM267]] | +0.66 | +0.57 / +0.61 | both halves | 1e-05 |  |
| [[RWDD3]] | +0.65 | +0.49 / +0.66 | both halves | 1e-05 |  |
| [[C2orf42]] | +0.63 | +0.51 / +0.58 | both halves | 1e-05 |  |
| [[MFSD8]] | +0.62 | +0.54 / +0.58 | both halves | 1e-05 |  |
| [[C8orf76]] | +0.60 | +0.31 / +0.70 | both halves | 2e-04 |  |
| [[MORN4]] | +0.59 | +0.50 / +0.60 | both halves | 1e-05 |  |
| [[PLPP5]] | +0.59 | +0.48 / +0.55 | both halves | 2e-05 |  |
| [[ORMDL1]] | +0.59 | +0.53 / +0.55 | both halves | 1e-05 |  |
| [[CDC37L1]] | +0.59 | +0.56 / +0.58 | both halves | 1e-05 |  |
| [[ZCCHC8]] | +0.58 | +0.46 / +0.43 | both halves | 3e-05 |  |
| [[FAHD2A]] | +0.58 | +0.49 / +0.59 | both halves | 1e-05 |  |

## Genes that move opposite

*28 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CORO1C]] | -0.60 | -0.59 / -0.56 | both halves | 1e-05 |  |
| [[CDC42]] | -0.56 | -0.58 / -0.61 | both halves | 8e-06 |  |
| [[CAPZB]] | -0.55 | -0.54 / -0.50 | both halves | 1e-05 |  |
| [[STIP1]] | -0.55 | -0.36 / -0.61 | both halves | 9e-05 |  |
| [[SERBP1]] | -0.54 | -0.32 / -0.46 | both halves | 2e-04 |  |
| [[BCKDK]] | -0.54 | -0.62 / -0.36 | both halves | 9e-05 |  |
| [[TGOLN2]] | -0.54 | -0.47 / -0.56 | both halves | 2e-05 |  |
| [[CCT2]] | -0.54 | -0.36 / -0.57 | both halves | 9e-05 |  |
| [[EFTUD2]] | -0.53 | -0.49 / -0.55 | both halves | 1e-05 | pathway: Processing of Capped Intron-Containing Pre-mRNA; STRING 999 |
| [[YWHAQ]] | -0.53 | -0.43 / -0.62 | both halves | 4e-05 |  |
| [[TPM3]] | -0.53 | -0.54 / -0.49 | both halves | 1e-05 |  |
| [[NOC2L]] | -0.53 | -0.44 / -0.45 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers LSM8's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 3.4% of all compounds | 0.095 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 015]]; 210 genes; this gene is in the **+** arm (projection on the module's main direction 0.562). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-13.9, 21.4); signed map (-0.6, 0.8). **Vector** length 88.4, 19.7% of its response variance represented; |z| ≥ 3 in 730 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +4.5 | +10.7 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +4.4 | +9.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.7 | +4.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.1 | +13.6 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +3.1 | +6.6 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +2.0 | +2.2 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.9 | +2.1 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +1.8 | +1.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +1.6 | +2.1 |
| fall | [[TAK-901 (drug)]] 5 µM |  | -5.6 | -8.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | -5.2 | -3.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | -5.1 | -6.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | -4.9 | +0.6 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.2 | +2.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.1 | -1.0 |
|  | [[Omeprazole (drug)]] 0.05 µM |  | -1.9 | -2.4 |
|  | [[Diphenhydramine (drug)]] 0.5 µM |  | -1.8 | -1.7 |
|  | [[Apalutamide (drug)]] 0.5 µM |  | -1.6 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | LSM8 homolog, U6 small nuclear RNA associated |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q31.31 — chr7:118,184,144-118,204,035 (+) |
| Ensembl biotype | protein_coding |
| Also known as | YJR022W |
| Gene groups (HGNC) | LSm proteins |
| Reactome | 4 pathways, smallest: mRNA Splicing - Major Pathway; mRNA Splicing; Processing of Capped Intron-Containing Pre-mRNA |
| Matched by | ensembl_id |

**Function**, from UniProt [O95777](https://www.uniprot.org/uniprotkb/O95777) (U6 snRNA-associated Sm-like protein LSm8):

> Plays a role in pre-mRNA splicing as component of the U4/U6-U5 tri-snRNP complex that is involved in spliceosome assembly, and as component of the precatalytic spliceosome (spliceosome B complex). The heptameric LSM2-8 complex binds specifically to the 3'-terminal U-tract of U6 snRNA.

**Summary**, from NCBI Gene [51691](https://www.ncbi.nlm.nih.gov/gene/51691):

> This gene encodes a member of the like-Sm family of proteins. The encoded protein consists of a closed barrel shape, made up of five anti-parallel beta strands and an alpha helix. This protein partners with six paralogs to form a heteroheptameric ring which transiently binds U6 small nuclear RNAs and is involved in the general maturation of RNA in the nucleus. [provided by RefSeq, Jan 2010]

**Accessions** — [HGNC:20471](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20471) · Entrez [51691](https://www.ncbi.nlm.nih.gov/gene/51691) · UniProt [O95777](https://www.uniprot.org/uniprotkb/O95777) · Ensembl [ENSG00000128534](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000128534)

## Data

Gene col 4889: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4889); `tables/drug_effects.parquet` (18 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4889, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4889]; `tensor/DDL_lfc|DDL_z.npy` [4889]; `embed/gene_vectors.npy` [4889]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4889 or target_col == 4889). Every well: [[LSM8 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LSM8.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
