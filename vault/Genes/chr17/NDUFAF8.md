---
symbol: "NDUFAF8"
type: "gene"
col: 13427
ensembl_id: "ENSG00000224877"
name: "NADH:ubiquinone oxidoreductase complex assembly factor 8"
location: "17q25.3"
module: 48
arm: "+"
pooled_cpm: 9.86
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 0
n_dd_up_clean: 1
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/048"]
generated_by: "tahoemap"
---

# NDUFAF8

*NADH:ubiquinone oxidoreductase complex assembly factor 8* — 17q25.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (11 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 6.65× (z +12.8, q 2e-34, up in 33 of 33 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change. The strongest without an alert is [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM: 1.47× (z +3.6, q 0.016, up in 18 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 9 lines (SW480 7.87×, LoVo 10.7×, HOP62 9.89×, PANC-1 6.65×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change); [[Dinaciclib (drug)]] 5 µM in 2 lines (KATO III 8.25×, SW480 6.09×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Belinostat (drug)]] 0.5 µM in 1 line (RKO 0.0728×; ⚠ cell-cycle shift, would explain all of this change); [[Penfluridol (drug)]] 0.5 µM in 1 line (SNU-423 0.0696×).
> Its strongest partners by |cos| (96 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 8 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ATP5MF]] (+0.60, fdr 1e-05), [[NDUFA13]] (+0.60, fdr 1e-05, ⚠ NDUFA13 in the vector space only through flagged drug-doses), [[NDUFB2]] (+0.59, fdr 2e-05), [[DNPH1]] (+0.59, fdr 1e-05); moves opposite to [[HAPSTR1]] (-0.50, fdr 4e-05), [[TLN1]] (-0.48, fdr 2e-05), [[STYX]] (-0.45, fdr 1e-04).
> It sits in the **+** arm of [[Module 048]] (Aerobic respiration and respiratory electron transport).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[MRPL12]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 11 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13427.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 9 lines (SW480 7.87×, LoVo 10.7×, HOP62 9.89×, PANC-1 6.65×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change); [[Dinaciclib (drug)]] 5 µM in 2 lines (KATO III 8.25×, SW480 6.09×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **6.65×** | +12.8 | 2e-34 | 33/33 (SW480, LoVo, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **5.33×** | +10.8 | 6e-25 | 19/19 (KATO III, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **4.65×** | +9.6 | 2e-19 | 24/25 (HOP62, LoVo, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | **2.54×** | +6.3 | 5e-08 | 36/45 (PANC-1, SW480, …) | top dose only | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.57×** | +6.1 | 1e-07 | 31/37 (NCI-H2030, CFPAC-1, …) | inconsistent across doses | cell-cycle shift (explains ~9% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~41% of this change | **2.16×** | +5.2 | 2e-05 | 24/36 (SW 900, hTERT-HPNE, …) | inconsistent across doses | low cells (technical?) |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.82×** | +4.0 | 0.005 | 26/46 (LS 180, SW480, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~63% of this change | **1.86×** | +4.0 | 0.005 | 25/46 (NCI-H1792, HS-578T, …) | rises with dose | composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.47×** | +3.6 | 0.016 | 18/48 (HOP62, A498, …) | top dose only |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | **1.46×** | +3.6 | 0.016 | 24/48 (A-172, A-427, …) | top dose only | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~86% of this change | **1.66×** | +3.4 | 0.034 | 21/47 (NCI-H1573, PANC-1, …) | rises with dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~60% of this change | **1.64×** | +3.3 | 0.042 | 20/46 (SW480, NCI-H460, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 13427.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Belinostat (drug)]] 0.5 µM in 1 line (RKO 0.0728×; ⚠ cell-cycle shift, would explain all of this change); [[Penfluridol (drug)]] 0.5 µM in 1 line (SNU-423 0.0696×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tirabrutinib (drug)]] 0.05 µM |  | 0.613× | -3.1 | 0.65 | 14/47 (HEC-1-A, H4, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.54 per unit of S-phase module lfc, +0.49 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13427. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[KATO III (line)]] | alt | 15.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 8.25× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | — |
| [[SW480 (line)]] | alt | 10.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.87× (z +10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | — |
| [[A498 (line)]] | wt | 13.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.59× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | — |
| [[HOP62 (line)]] | alt | 7.00 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 9.89× (z +9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | — |
| [[LoVo (line)]] | wt | 7.08 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 10.7× (z +9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 6.53 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 12.6× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | — |
| [[NCI-H1792 (line)]] | alt | 6.45 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 11.5× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | — |
| [[NCI-H2030 (line)]] | alt | 16.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.16× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | — |
| [[PANC-1 (line)]] | alt | 13.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.65× (z +9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | — |
| [[RKO (line)]] | wt | 9.55 | 0 | 1 (1 ⚠) | — | [[Belinostat (drug)]] 0.5 µM 0.0728× (z -9.5) ⚠ cell-cycle shift, would explain all of this change |
| [[SNU-423 (line)]] | alt | 6.39 | 0 | 1 | — | [[Penfluridol (drug)]] 0.5 µM 0.0696× (z -8.5) |
| [[A-172 (line)]] | wt | 9.06 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 22.7 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 12.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 6.93 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.05 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 6.30 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 6.77 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.54 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 4.39 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 25.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 5.60 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 8.27 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.33 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 19.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 8.05 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.70 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 6.15 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 6.42 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 12.7 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 9.89 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 9.68 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 14.4 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 4.94 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.27 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 9.53 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 9.54 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 8.75 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.93 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 7.03 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 9.91 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.01 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.75 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 8.20 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 9.69 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13427), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 8 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATP5MF]] | +0.60 | +0.61 / +0.55 | both halves | 1e-05 | pathway: Aerobic respiration and respiratory electron transport |
| [[NDUFA13]] ⚠ | +0.60 | +0.52 / +0.55 | both halves | 1e-05 | pathway: Aerobic respiration and respiratory electron transport; ⚠ in the vector space only through flagged drug-doses |
| [[NDUFB2]] | +0.59 | +0.48 / +0.53 | both halves | 2e-05 | pathway: Aerobic respiration and respiratory electron transport |
| [[DNPH1]] | +0.59 | +0.51 / +0.67 | both halves | 1e-05 |  |
| [[NDUFB1]] | +0.58 | +0.54 / +0.56 | both halves | 1e-05 | pathway: Aerobic respiration and respiratory electron transport |
| [[PURPL]] | +0.58 | +0.52 / +0.53 | both halves | 1e-05 |  |
| [[TRIAP1]] | +0.57 | +0.46 / +0.61 | both halves | 2e-05 |  |
| [[TIMM13]] | +0.56 | +0.52 / +0.64 | both halves | 1e-05 |  |
| [[TIMM10]] | +0.55 | +0.54 / +0.58 | both halves | 1e-05 |  |
| [[NDUFS6]] | +0.54 | +0.46 / +0.54 | both halves | 2e-05 | pathway: Aerobic respiration and respiratory electron transport |
| [[NTPCR]] | +0.54 | +0.42 / +0.56 | both halves | 4e-05 |  |
| [[PTCHD4]] | +0.53 | +0.48 / +0.54 | both halves | 2e-05 |  |
| [[COPS9]] | +0.53 | +0.51 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HAPSTR1]] | -0.50 | -0.41 / -0.51 | both halves | 4e-05 |  |
| [[TLN1]] | -0.48 | -0.49 / -0.48 | both halves | 2e-05 |  |
| [[STYX]] | -0.45 | -0.35 / -0.44 | both halves | 1e-04 |  |
| [[UAP1]] | -0.43 | -0.40 / -0.38 | both halves | 7e-05 |  |
| [[CALU]] | -0.43 | -0.34 / -0.50 | both halves | 1e-04 |  |
| [[GOLGA3]] | -0.42 | -0.45 / -0.38 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MRPL12]] | C | MRPL12's natural level strengthens NDUFAF8's drug response | MRPL12's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.66, reverse +0.10; direction clear | 0.037 | ⚠ tissue can mimic it; precision caveat |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 048]] — Aerobic respiration and respiratory electron transport; 93 genes; this gene is in the **+** arm (projection on the module's main direction 0.395). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.37).
- **Nodal map** (x, y) = (-50.7, -16.6); signed map (-38.1, -26.1). **Vector** length 51.4, 9.93% of its response variance represented; |z| ≥ 3 in 602 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | +3.4 | +6.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.7 | +3.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | +2.5 | +12.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~60% of this change | +2.5 | +3.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +2.5 | +6.1 |
|  | [[Amsacrine (drug)]] 5 µM |  | +1.9 | +2.5 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.5 | +1.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.4 | +2.2 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.4 | -0.0 |
| fall | [[GSK1059615 (drug)]] 5 µM |  | -1.5 | -2.5 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | -1.5 | -1.6 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.4 | -1.4 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.4 | -1.8 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.3 | +0.2 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.3 | -2.8 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.3 | -0.4 |

## What is on record

|  |  |
|---|---|
| Name | NADH:ubiquinone oxidoreductase complex assembly factor 8 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q25.3 — chr17:81,239,305-81,241,310 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously C17orf89 |
| Gene groups (HGNC) | Mitochondrial respiratory chain complex assembly factors |
| Reactome | 3 pathways, smallest: Complex I biogenesis; Respiratory electron transport; Aerobic respiration and respiratory electron transport |
| Matched by | ensembl_id |

**Function**, from UniProt [A1L188](https://www.uniprot.org/uniprotkb/A1L188) (NADH dehydrogenase):

> Involved in the assembly of mitochondrial NADH:ubiquinone oxidoreductase complex (complex I, MT-ND1). Required to stabilize NDUFAF5.

**Summary**, from NCBI Gene [284184](https://www.ncbi.nlm.nih.gov/gene/284184):

> Involved in mitochondrial respiratory chain complex I assembly. Located in mitochondrial matrix. Implicated in nuclear type mitochondrial complex I deficiency 34. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:33551](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:33551) · Entrez [284184](https://www.ncbi.nlm.nih.gov/gene/284184) · UniProt [A1L188](https://www.uniprot.org/uniprotkb/A1L188) · Ensembl [ENSG00000224877](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000224877)

## Data

Gene col 13427: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13427); `tables/drug_effects.parquet` (13 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13427, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13427]; `tensor/DDL_lfc|DDL_z.npy` [13427]; `embed/gene_vectors.npy` [13427]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13427 or target_col == 13427). Every well: [[NDUFAF8 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NDUFAF8.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
