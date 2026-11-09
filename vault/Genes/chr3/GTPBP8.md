---
symbol: "GTPBP8"
type: "gene"
col: 8728
ensembl_id: "ENSG00000163607"
name: "GTP binding protein 8"
location: "3q13.2"
module: 17
arm: "+"
pooled_cpm: 15.88
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 1
n_dd_up_clean: 4
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/017"]
generated_by: "tahoemap"
---

# GTPBP8

*GTP binding protein 8* — 3q13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 1.52× (z +9.2, q 1e-17, up in 16 of 26 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Selinexor (drug)]] 5 µM: 1.29× (z +8.3, q 2e-14, up in 23 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Digitoxin (drug)]] 0.05 µM: 0.803× (z -5.0, q 2e-04, down in 14 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 4 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (Hs 766T 0.158×, H4 0.173×; ⚠ cell-cycle shift, explains ~0% of this change); [[Digitoxin (drug)]] 5 µM in 1 line (C-33 A 0.0761×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (NCI-H1792 0.205×; ⚠ cell-cycle shift, explains ~39% of this change); [[Gallic acid (hydrate) (drug)]] 0.5 µM in 1 line (HepG2/C3A 0.0453×); [[Harringtonine (drug)]] 0.05 µM in 1 line (A-172 0.0932×); [[Decitabine (drug)]] 0.05 µM in 1 line (HepG2/C3A 0.0961×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PIGB]] (+0.57, fdr 2e-05), [[COMMD8]] (+0.56, fdr 3e-05), [[AMACR]] (+0.55, fdr 1e-05); moves opposite to [[NPIPB11]] (-0.54, fdr 5e-05), [[PTRH1]] (-0.52, fdr 3e-04), [[TMEM11-DT]] (-0.48, fdr 1e-04).
> It sits in the **+** arm of [[Module 017]] (Intraflagellar transport).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[ENPP4]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 11 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8728.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.52×** | +9.2 | 1e-17 | 16/26 (A549, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.48×** | +8.9 | 2e-16 | 25/40 (SNU-423, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.29×** | +8.3 | 2e-14 | 23/48 (J82, KATO III, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.35×** | +6.6 | 5e-09 | 21/42 (HEC-1-A, C-33 A, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.23×** | +6.6 | 5e-09 | 15/48 (RKO, LOX-IMVI, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.33×** | +6.0 | 1e-07 | 16/31 (A498, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.25×** | +4.9 | 7e-05 | 15/46 (LS 180, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~12% of this change | **1.23×** | +4.6 | 2e-04 | 14/47 (PANC-1, SK-MEL-2, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~14% of this change | **1.23×** | +4.6 | 2e-04 | 13/47 (A-172, LOX-IMVI, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.22×** | +4.5 | 4e-04 | 9/47 (hTERT-HPNE, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **1.21×** | +4.2 | 0.002 | 12/46 (LS 180, NCI-H2347, …) | rises with dose | composition shift; position effect removed |
| [[Ponatinib (drug)]] 5 µM |  | 1.19× | +4.0 | 0.004 | 5/47 (HS-578T, PANC-1, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.19× | +3.9 | 0.004 | 7/47 (HEC-1-A, J82, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~15% of this change | 1.18× | +3.8 | 0.005 | 14/47 (PANC-1, A-172, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | 1.12× | +3.7 | 0.008 | 16/47 (LS 180, BT-474, …) | all doses, stronger at high dose | composition shift |
| [[Chlorhexidine (diacetate) (drug)]] 5 µM |  | 1.10× | +3.1 | 0.071 | 3/48 (RPMI-7951, SK-MEL-2, …) | top dose only |  |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | 1.14× | +3.0 | 0.089 | 5/47 (HOP62, KATO III, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 2 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 8728.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 4 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (Hs 766T 0.158×, H4 0.173×; ⚠ cell-cycle shift, explains ~0% of this change); [[Digitoxin (drug)]] 5 µM in 1 line (C-33 A 0.0761×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (NCI-H1792 0.205×; ⚠ cell-cycle shift, explains ~39% of this change); [[Gallic acid (hydrate) (drug)]] 0.5 µM in 1 line (HepG2/C3A 0.0453×); [[Harringtonine (drug)]] 0.05 µM in 1 line (A-172 0.0932×); [[Decitabine (drug)]] 0.05 µM in 1 line (HepG2/C3A 0.0961×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.05 µM |  | **0.803×** | -5.0 | 2e-04 | 14/47 (A-172, NCI-H2030, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.858× | -5.0 | 2e-04 | 17/47 (Hs 766T, H4, …) | top dose only |  |
| [[Sildenafil (drug)]] 5 µM |  | 0.840× | -3.8 | 0.023 | 2/47 (PANC-1, BT-474) | rises with dose | plate-row cell shift; position effect removed |
| [[Sonidegib (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.875× | -3.1 | 0.29 | 1/47 (LoVo) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.04 per unit of S-phase module lfc, +0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8728. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HepG2_C3A (line)]] | wt | 11.4 | 0 | 2 | — | [[Gallic acid (hydrate) (drug)]] 0.5 µM 0.0453× (z -12.4) |
| [[A-172 (line)]] | wt | 7.36 | 0 | 1 | — | [[Harringtonine (drug)]] 0.05 µM 0.0932× (z -11.3) |
| [[C-33 A (line)]] | alt | 19.2 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0761× (z -14.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[H4 (line)]] | wt | 10.6 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.173× (z -8.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[Hs 766T (line)]] | wt | 7.63 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.158× (z -11.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H1792 (line)]] | alt | 13.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.205× (z -13.3) ⚠ cell-cycle shift, explains ~39% of this change |
| [[SNU-1 (line)]] | wt | 21.9 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0934× (z -11.4) ⚠ cell-cycle shift, explains ~38% of this change |
| [[A-427 (line)]] | wt | 28.3 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 7.09 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 16.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 22.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 9.04 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 11.0 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 16.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 21.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 24.4 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 22.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 8.74 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 15.8 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 16.1 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 18.4 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 9.46 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 20.8 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 20.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 21.8 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 13.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 19.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 27.2 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 8.37 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 19.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 19.9 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 24.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8728), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*80 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PIGB]] | +0.57 | +0.48 / +0.48 | both halves | 2e-05 |  |
| [[COMMD8]] | +0.56 | +0.44 / +0.59 | both halves | 3e-05 |  |
| [[AMACR]] | +0.55 | +0.51 / +0.55 | both halves | 1e-05 |  |
| [[WDR17]] | +0.54 | +0.35 / +0.61 | both halves | 1e-04 |  |
| [[ADH5]] | +0.54 | +0.32 / +0.60 | both halves | 2e-04 |  |
| [[ZNF33B]] | +0.53 | +0.39 / +0.46 | both halves | 5e-05 |  |
| [[PGGT1B]] | +0.53 | +0.45 / +0.50 | both halves | 3e-05 |  |
| [[KPNA5]] | +0.53 | +0.43 / +0.53 | both halves | 3e-05 |  |
| [[UBXN2B]] | +0.53 | +0.36 / +0.63 | both halves | 1e-04 |  |
| [[RBM18]] | +0.53 | +0.42 / +0.57 | both halves | 4e-05 |  |
| [[MRPL40]] | +0.51 | +0.49 / +0.48 | both halves | 2e-05 |  |
| [[ZDHHC17]] | +0.51 | +0.39 / +0.46 | both halves | 5e-05 |  |

## Genes that move opposite

*20 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NPIPB11]] | -0.54 | -0.40 / -0.48 | both halves | 5e-05 |  |
| [[PTRH1]] | -0.52 | -0.29 / -0.52 | both halves | 3e-04 |  |
| [[TMEM11-DT]] | -0.48 | -0.34 / -0.50 | both halves | 1e-04 |  |
| [[PITPNA]] | -0.46 | -0.29 / -0.49 | both halves | 2e-04 |  |
| [[TBC1D10B]] | -0.46 | -0.38 / -0.50 | both halves | 6e-05 |  |
| [[PDCD6]] | -0.46 | -0.39 / -0.47 | both halves | 5e-05 |  |
| [[DRD4]] | -0.46 | -0.42 / -0.40 | both halves | 5e-05 |  |
| [[FBXW7]] | -0.46 | -0.41 / -0.44 | both halves | 4e-05 |  |
| [[NPLOC4]] | -0.46 | -0.36 / -0.47 | both halves | 1e-04 |  |
| [[TIMM23B-AGAP6]] | -0.45 | -0.26 / -0.38 | both halves | 4e-04 |  |
| [[FAM120B]] | -0.45 | -0.33 / -0.38 | both halves | 1e-04 |  |
| [[SENP5]] | -0.45 | -0.33 / -0.46 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ENPP4]] | B | ENPP4 activity raises GTPBP8's level | lines that do not express ENPP4 (17) vs lines expressing it (33) | 1.59× lower at baseline in the lines without ENPP4 | 0.034 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: ACTR3C, SAMD12, ATP8A1 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 017]] — Intraflagellar transport; 202 genes; this gene is in the **+** arm (projection on the module's main direction 0.521). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-21.3, 3.2); signed map (8.4, -37.3). **Vector** length 50.8, 6.08% of its response variance represented; |z| ≥ 3 in 736 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +3.7 | +8.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.8 | +4.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.7 | +6.6 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | +2.7 | +4.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +2.7 | +6.6 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.5 | +2.7 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +1.4 | +2.4 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +1.2 | -0.4 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -2.6 | -5.0 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -1.6 | +0.5 |
|  | [[Digitoxin (drug)]] 0.05 µM |  | -1.5 | -5.0 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.5 | -2.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.3 | -1.6 |
|  | [[Gallic acid (hydrate) (drug)]] 0.5 µM |  | -1.0 | -1.3 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | -1.0 | -0.2 |
|  | [[Hydroxyurea (drug)]] 5 µM |  | -0.9 | -0.4 |
|  | [[Demeclocycline (drug)]] 5 µM |  | -0.8 | -1.9 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -0.7 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | GTP binding protein 8 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q13.2 — chr3:112,990,984-113,015,060 (+) |
| Ensembl biotype | protein_coding |
| Also known as | HSPC135 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8N3Z3](https://www.uniprot.org/uniprotkb/Q8N3Z3) (GTP-binding protein 8):

> Mitochondrial GTPase required for late-stage maturation of the mitoribosomal large subunit (39S mt-LSU), thereby promoting assembly of functional 55S mitoribosomes, which are required for efficient mitochondrial translation. Also modulates mitochondrial fission in a DNM1L-dependent manner by influencing DNM1L phosphorylation and recruitment to mitochondria.

**Summary**, from NCBI Gene [29083](https://www.ncbi.nlm.nih.gov/gene/29083):

> Predicted to enable GTP binding activity; GTPase activity; and metal ion binding activity. Located in mitochondrion. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:25007](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25007) · Entrez [29083](https://www.ncbi.nlm.nih.gov/gene/29083) · UniProt [Q8N3Z3](https://www.uniprot.org/uniprotkb/Q8N3Z3) · Ensembl [ENSG00000163607](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000163607)

## Data

Gene col 8728: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8728); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8728, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8728]; `tensor/DDL_lfc|DDL_z.npy` [8728]; `embed/gene_vectors.npy` [8728]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8728 or target_col == 8728). Every well: [[GTPBP8 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GTPBP8.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
