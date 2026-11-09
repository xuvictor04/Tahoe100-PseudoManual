---
symbol: "SNAP47"
type: "gene"
col: 6792
ensembl_id: "ENSG00000143740"
name: "synaptosome associated protein 47"
location: "1q42.13"
module: 127
arm: "+"
pooled_cpm: 17.25
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 10
n_dd_up_clean: 4
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/127"]
generated_by: "tahoemap"
---

# SNAP47

*synaptosome associated protein 47* — 1q42.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 5 µM: 1.80× (z +8.8, q 1e-15, up in 40 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (8 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.689× (z -7.8, q 2e-12, down in 33 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 11 here, 4 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 4 lines (NCI-H1573 0.104×, HOP62 0.139×, A549 0.131×, MIA PaCa-2 0.170×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 3 lines (NCI-H2030 0.103×, PANC-1 0.271×, NCI-H460 0.294×; ⚠ toxic; transcription drop); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (HOP62 0.392×, NCI-H2347 0.413×); [[Hesperidin (drug)]] 0.05 µM in 1 line (COLO 205 0.0457×); [[Canagliflozin (drug)]] 0.05 µM in 1 line (BT-474 0.177×).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CANT1]] (+0.60, fdr 4e-05), [[ABCF3]] (+0.59, fdr 2e-05), [[TRIM32]] (+0.58, fdr 1e-05); moves opposite to [[INTS6-AS1]] (-0.51, fdr 1e-04), [[LARP1B]] (-0.51, fdr 1e-04), [[SPATA1]] (-0.50, fdr 2e-04).
> It is in [[Module 127]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6792.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **1.80×** | +8.8 | 1e-15 | 40/48 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.65×** | +7.5 | 2e-11 | 37/48 (SW480, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.61×** | +7.1 | 2e-10 | 30/47 (SW480, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.33×** | +6.6 | 5e-09 | 28/48 (BT-474, PANC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 8 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6792.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 11 here, 4 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 4 lines (NCI-H1573 0.104×, HOP62 0.139×, A549 0.131×, MIA PaCa-2 0.170×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 3 lines (NCI-H2030 0.103×, PANC-1 0.271×, NCI-H460 0.294×; ⚠ toxic; transcription drop); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (HOP62 0.392×, NCI-H2347 0.413×); [[Hesperidin (drug)]] 0.05 µM in 1 line (COLO 205 0.0457×); [[Canagliflozin (drug)]] 0.05 µM in 1 line (BT-474 0.177×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.689×** | -7.8 | 2e-12 | 33/47 (HOP62, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.621×** | -6.5 | 2e-08 | 24/47 (RKO, SNU-423, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **0.649×** | -6.4 | 2e-08 | 29/40 (C-33 A, NCI-H1573, …) | all doses, flat | composition shift; position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.655×** | -5.8 | 1e-06 | 25/45 (C-33 A, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~19% here); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.664×** | -5.6 | 3e-06 | 17/28 (NCI-H2030, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~22% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.702×** | -4.9 | 1e-04 | 17/34 (NCI-H1573, HOP62, …) | all doses, flat | cell-cycle shift (explains ~16% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.756×** | -4.2 | 0.002 | 22/47 (RPMI-7951, A-427, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **0.760×** | -4.1 | 0.003 | 17/48 (LoVo, NCI-H460, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | **0.774×** | -3.8 | 0.009 | 19/46 (NCI-H23, J82, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.800×** | -3.3 | 0.050 | 18/46 (NCI-H460, NCI-H1573, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.06 per unit of S-phase module lfc, -0.33 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6792. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[BT-474 (line)]] | alt | 22.2 | 3 (2 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 13.1× (z +22.4) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 26.3× (z +10.5) | [[Canagliflozin (drug)]] 0.05 µM 0.177× (z -9.9) |
| [[HOP62 (line)]] | alt | 15.4 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.139× (z -13.0) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.392× (z -9.4) |
| [[MIA PaCa-2 (line)]] | alt | 22.0 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.40× (z +11.2) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 0.05 µM 0.170× (z -10.6) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 19.6 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.104× (z -13.9) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 15.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.131× (z -11.7) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 21.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.186× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[COLO 205 (line)]] | alt | 16.3 | 0 | 1 | — | [[Hesperidin (drug)]] 0.05 µM 0.0457× (z -13.8) |
| [[H4 (line)]] | wt | 21.9 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.134× (z -9.0) ⚠ transcription drop; cell-cycle shift, would explain all of this change |
| [[Hs 766T (line)]] | wt | 15.3 | 0 | 1 | — | [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM 0.214× (z -8.9) |
| [[J82 (line)]] | alt | 14.2 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.47× (z +16.2) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[NCI-H2030 (line)]] | alt | 17.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.103× (z -13.7) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 17.0 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.207× (z -9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change |
| [[NCI-H2347 (line)]] | alt | 19.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.413× (z -9.2) |
| [[NCI-H460 (line)]] | wt | 20.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.294× (z -9.3) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 22.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.271× (z -11.3) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 18.5 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.204× (z -8.6) |
| [[SNU-1 (line)]] | wt | 16.5 | 0 | 1 | — | [[Temsirolimus (drug)]] 0.5 µM 0.117× (z -9.1) |
| [[SW 900 (line)]] | alt | 23.6 | 0 | 1 | — | [[Belzutifan (drug)]] 5 µM 0.0661× (z -9.5) |
| [[SW48 (line)]] | wt | 19.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.167× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[A-172 (line)]] | wt | 16.0 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 16.9 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 18.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 9.71 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 21.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 22.2 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 20.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 10.2 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 12.2 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 16.7 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 13.0 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 19.5 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 21.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 16.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6792), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*71 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CANT1]] | +0.60 | +0.57 / +0.41 | both halves | 4e-05 |  |
| [[ABCF3]] | +0.59 | +0.48 / +0.56 | both halves | 2e-05 |  |
| [[TRIM32]] | +0.58 | +0.58 / +0.56 | both halves | 1e-05 |  |
| [[SNRNP200]] | +0.58 | +0.59 / +0.46 | both halves | 3e-05 |  |
| [[PRPF31]] | +0.57 | +0.49 / +0.47 | both halves | 2e-05 |  |
| [[VTA1]] | +0.57 | +0.57 / +0.39 | both halves | 6e-05 |  |
| [[ESS2]] | +0.57 | +0.59 / +0.28 | both halves | 3e-04 |  |
| [[BCKDK]] | +0.56 | +0.46 / +0.38 | both halves | 6e-05 |  |
| [[RNF40]] | +0.55 | +0.46 / +0.49 | both halves | 2e-05 |  |
| [[HIF1AN]] | +0.55 | +0.38 / +0.51 | both halves | 7e-05 |  |
| [[TBC1D13]] | +0.55 | +0.55 / +0.39 | both halves | 6e-05 |  |
| [[EXOC3]] | +0.55 | +0.47 / +0.49 | both halves | 2e-05 |  |

## Genes that move opposite

*29 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[INTS6-AS1]] | -0.51 | -0.37 / -0.34 | both halves | 1e-04 |  |
| [[LARP1B]] | -0.51 | -0.49 / -0.32 | both halves | 1e-04 |  |
| [[SPATA1]] | -0.50 | -0.32 / -0.48 | both halves | 2e-04 |  |
| [[EHBP1-AS1]] | -0.50 | -0.24 / -0.57 | both halves | 4e-04 |  |
| [[PRDM2]] | -0.50 | -0.41 / -0.30 | both halves | 2e-04 |  |
| [[UNC79]] | -0.50 | -0.33 / -0.40 | both halves | 1e-04 |  |
| [[EPM2A-DT]] | -0.49 | -0.30 / -0.45 | both halves | 2e-04 |  |
| [[PKN2-AS1]] | -0.49 | -0.38 / -0.38 | both halves | 7e-05 |  |
| [[LINC02608]] | -0.49 | -0.31 / -0.41 | both halves | 2e-04 |  |
| [[DENND6A-AS1]] | -0.49 | -0.28 / -0.48 | both halves | 3e-04 |  |
| [[IGF2BP3]] | -0.49 | -0.37 / -0.38 | both halves | 8e-05 |  |
| [[PPP1R12A-AS2]] | -0.49 | -0.33 / -0.36 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity lowers SNAP47's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 0.8% of all compounds | 0.044 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 127]]; 37 genes; every member is in the + arm (projection on the module's main direction 0.657). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.27; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-33.2, -3.3); signed map (-14.2, -28.6). **Vector** length 60.8, 8.91% of its response variance represented; |z| ≥ 3 in 936 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +4.3 | +6.6 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +2.9 | +7.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.8 | +1.3 |
|  | [[Panobinostat (drug)]] 5 µM |  | +2.5 | +8.8 |
|  | [[Belinostat (drug)]] 5 µM |  | +2.2 | +7.1 |
|  | [[Imiquimod (hydrochloride) (drug)]] 0.05 µM |  | +1.0 | +0.9 |
|  | [[Bisoprolol (hemifumarate) (drug)]] 0.5 µM |  | +0.8 | +1.3 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | +0.8 | +1.8 |
|  | [[Pentoxifylline (drug)]] 5 µM |  | +0.7 | +1.8 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -6.0 | -7.8 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -4.8 | -2.8 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -4.8 | -6.5 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -2.6 | -5.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.0 | -0.4 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.0 | -0.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.8 | +1.6 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.2 | -2.6 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -1.2 | -0.3 |

## What is on record

|  |  |
|---|---|
| Name | synaptosome associated protein 47 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q42.13 — chr1:227,728,200-227,781,826 (+) |
| Ensembl biotype | protein_coding |
| Also known as | SVAP1, SNAP-47; previously C1orf142 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q5SQN1](https://www.uniprot.org/uniprotkb/Q5SQN1) (Synaptosomal-associated protein 47):

> Plays a role in intracellular membrane fusion.

**Summary**, from NCBI Gene [116841](https://www.ncbi.nlm.nih.gov/gene/116841):

> Predicted to enable SNAP receptor activity. Predicted to be involved in synaptic vesicle fusion to presynaptic active zone membrane and synaptic vesicle priming. Predicted to act upstream of or within long-term synaptic potentiation. Located in BLOC-1 complex. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:30669](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30669) · Entrez [116841](https://www.ncbi.nlm.nih.gov/gene/116841) · UniProt [Q5SQN1](https://www.uniprot.org/uniprotkb/Q5SQN1) · Ensembl [ENSG00000143740](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000143740)

## Data

Gene col 6792: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6792); `tables/drug_effects.parquet` (14 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6792, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6792]; `tensor/DDL_lfc|DDL_z.npy` [6792]; `embed/gene_vectors.npy` [6792]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6792 or target_col == 6792). Every well: [[SNAP47 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SNAP47.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
