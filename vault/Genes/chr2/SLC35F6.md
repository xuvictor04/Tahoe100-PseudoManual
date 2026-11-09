---
symbol: "SLC35F6"
type: "gene"
col: 13128
ensembl_id: "ENSG00000213699"
name: "solute carrier family 35 member F6"
location: "2p23.3"
module: 24
arm: "-"
pooled_cpm: 9.4
n_lines_expressing: 50
n_dd_up: 18
n_dd_down: 2
n_dd_up_clean: 12
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 1
tags: ["gene", "module/024"]
generated_by: "tahoemap"
---

# SLC35F6

*solute carrier family 35 member F6* — 2p23.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.94× (z +10.9, q 9e-25, up in 15 of 18 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 2.42× (z +9.3, q 5e-18, up in 41 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[TAK-901 (drug)]] 5 µM: 0.486× (z -4.0, q 0.028, down in 16 of 46 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (A-427 0.131×; ⚠ cell-cycle shift, explains ~0% of this change); [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 1 line (A-427 0.205×; ⚠ cell-cycle shift, explains ~94% of this change); [[Almonertinib (mesylate) (drug)]] 0.05 µM in 1 line (AsPC-1 0.0838×); [[Acetazolamide (drug)]] 0.5 µM in 1 line (NCI-H1792 0.0806×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF518B]] (+0.68, fdr 7e-06), [[PSME3]] (+0.68, fdr 7e-06), [[SNX19]] (+0.68, fdr 7e-06); moves opposite to [[NDUFA2]] (-0.66, fdr 1e-05), [[TRIM7-AS2]] (-0.64, fdr 1e-05), [[GNRH1]] (-0.63, fdr 1e-05).
> It sits in the **-** arm of [[Module 024]] (Aerobic respiration and respiratory electron transport).
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 1 goes from it, the strongest it → cells under [[ERK5-IN-2 (drug)]] 0.5 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 6 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13128.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.94×** | +10.9 | 9e-25 | 15/18 (A498, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift; position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **2.42×** | +9.3 | 5e-18 | 41/47 (MIA PaCa-2, KATO III, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.34×** | +8.9 | 1e-16 | 24/35 (A498, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.91×** | +6.3 | 6e-08 | 14/24 (A498, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift; position effect removed |
| [[Belumosudil (drug)]] 5 µM |  | **1.70×** | +5.4 | 1e-05 | 24/47 (PANC-1, MIA PaCa-2, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.58×** | +4.8 | 2e-04 | 17/47 (NCI-H460, A-172, …) | inconsistent across doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.56×** | +4.6 | 3e-04 | 15/37 (PANC-1, A-427, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.56×** | +4.6 | 3e-04 | 19/47 (HepG2/C3A, A549, …) | top dose only | cell-cycle shift (explains ~16% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.52×** | +4.4 | 7e-04 | 18/45 (KATO III, SNU-423, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.51×** | +4.3 | 8e-04 | 17/46 (SW480, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **1.52×** | +4.2 | 0.001 | 20/45 (SW480, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.45×** | +3.8 | 0.006 | 15/47 (A549, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); position effect removed |
| [[Erlotinib (drug)]] 5 µM |  | **1.46×** | +3.8 | 0.006 | 13/47 (A-427, NCI-H23, …) | top dose only | position effect removed |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.43×** | +3.7 | 0.009 | 17/47 (A498, HEC-1-A, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.44×** | +3.6 | 0.012 | 13/45 (A-172, BT-474, …) | inconsistent across doses | cell-cycle shift (explains ~14% here) |
| [[Neratinib (maleate) (drug)]] 0.5 µM |  | **1.36×** | +3.2 | 0.047 | 11/45 (A498, J82, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Bestatin (hydrochloride) (drug)]] 0.5 µM |  | **1.34×** | +3.0 | 0.077 | 6/47 (SW1417, A-172, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 13128.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (A-427 0.131×; ⚠ cell-cycle shift, explains ~0% of this change); [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 1 line (A-427 0.205×; ⚠ cell-cycle shift, explains ~94% of this change); [[Almonertinib (mesylate) (drug)]] 0.05 µM in 1 line (AsPC-1 0.0838×); [[Acetazolamide (drug)]] 0.5 µM in 1 line (NCI-H1792 0.0806×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **0.486×** | -4.0 | 0.028 | 16/46 (LoVo, RKO, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~4% here); composition shift; noisy plate (z scaled) |
| [[Verteporfin (drug)]] 5 µM |  | **0.684×** | -3.9 | 0.028 | 19/45 (SNU-423, A-427, …) | rises with dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.901× | -3.8 | 0.028 | 7/48 (HOP62, AN3 CA, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | 0.564× | -3.2 | 0.22 | 11/42 (LoVo, SW1417, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Diammonium Glycyrrhizinate (drug)]] 5 µM |  | 0.816× | -3.1 | 0.25 | 10/48 (Hs 766T, SW 1088, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.22 per unit of S-phase module lfc, -0.23 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13128. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 19.7 | 0 | 2 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.131× (z -11.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A498 (line)]] | wt | 25.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.91× (z +9.2) ⚠ toxic; transcription drop | — |
| [[AsPC-1 (line)]] | alt | 5.57 | 0 | 1 | — | [[Almonertinib (mesylate) (drug)]] 0.05 µM 0.0838× (z -8.9) |
| [[NCI-H1792 (line)]] | alt | 3.78 | 0 | 1 | — | [[Acetazolamide (drug)]] 0.5 µM 0.0806× (z -8.6) |
| [[A-172 (line)]] | wt | 12.0 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 11.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 8.84 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 5.93 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 7.28 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 4.47 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.96 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 6.48 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 6.05 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 7.34 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 7.27 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 5.14 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 5.65 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 6.28 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 9.16 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.22 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 8.79 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 4.81 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 6.78 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 9.49 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 7.88 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 7.69 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.73 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.48 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 8.71 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.65 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 8.52 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 13.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 9.41 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 6.89 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 7.58 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 9.04 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 4.48 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 6.39 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.70 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 7.06 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 9.03 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13128), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*57 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF518B]] | +0.68 | +0.61 / +0.70 | both halves | 7e-06 |  |
| [[PSME3]] | +0.68 | +0.71 / +0.62 | both halves | 7e-06 |  |
| [[SNX19]] | +0.68 | +0.64 / +0.67 | both halves | 7e-06 |  |
| [[ZNF460]] | +0.67 | +0.53 / +0.67 | both halves | 1e-05 |  |
| [[PRELID3B]] | +0.65 | +0.54 / +0.70 | both halves | 1e-05 |  |
| [[AP5B1]] | +0.65 | +0.63 / +0.58 | both halves | 7e-06 |  |
| [[PTPN11]] | +0.65 | +0.59 / +0.63 | both halves | 7e-06 |  |
| [[ABCF2]] | +0.65 | +0.63 / +0.64 | both halves | 7e-06 |  |
| [[OCRL]] | +0.64 | +0.61 / +0.65 | both halves | 7e-06 |  |
| [[TEX261]] | +0.64 | +0.59 / +0.64 | both halves | 7e-06 |  |
| [[LIN7C]] | +0.63 | +0.63 / +0.61 | both halves | 7e-06 |  |
| [[WDR77]] | +0.63 | +0.65 / +0.59 | both halves | 7e-06 |  |

## Genes that move opposite

*43 of its nearest partners move opposite, 4 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NDUFA2]] | -0.66 | -0.55 / -0.69 | both halves | 1e-05 |  |
| [[TRIM7-AS2]] | -0.64 | -0.56 / -0.61 | both halves | 1e-05 |  |
| [[GNRH1]] | -0.63 | -0.52 / -0.70 | both halves | 1e-05 |  |
| [[COX6B1]] | -0.62 | -0.54 / -0.62 | both halves | 1e-05 |  |
| [[RPS29]] | -0.62 | -0.55 / -0.63 | both halves | 1e-05 |  |
| [[AFMID]] | -0.61 | -0.59 / -0.61 | both halves | 7e-06 |  |
| [[UQCRB]] ⚠ | -0.61 | -0.53 / -0.61 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[TBC1D22A-DT]] | -0.61 | -0.61 / -0.63 | both halves | 7e-06 |  |
| [[PTMAP2]] ⚠ | -0.61 | -0.55 / -0.57 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[SNHG25]] | -0.61 | -0.52 / -0.62 | both halves | 1e-05 |  |
| [[DCTN6-DT]] | -0.60 | -0.57 / -0.58 | both halves | 1e-05 |  |
| [[SNHG19]] | -0.60 | -0.58 / -0.54 | both halves | 1e-05 |  |
| [[LINC01118]] | -0.60 | -0.58 / -0.55 | both halves | 1e-05 |  |
| [[RPL23A]] | -0.59 | -0.50 / -0.66 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[ERK5-IN-2 (drug)]] 0.5 µM | C | SLC35F6's natural level lowers the cells' numbers under ERK5-IN-2 0.5 µM (makes them more sensitive) | SLC35F6's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.62 | 0.430 over the table, 0.045 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

## Where it sits

- **Module**: [[Module 024]] — Aerobic respiration and respiratory electron transport; 179 genes; this gene is in the **-** arm (projection on the module's main direction -0.512). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-32.2, -20.5); signed map (-7.6, -39.0). **Vector** length 82.2, 15.1% of its response variance represented; |z| ≥ 3 in 935 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +6.9 | +9.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.6 | +10.9 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +4.4 | +4.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.2 | +8.9 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +4.0 | +4.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.7 | +5.4 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +3.2 | +3.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.5 | +2.2 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +2.5 | +0.9 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -3.4 | -1.8 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.3 | -3.9 |
|  | [[TAK-901 (drug)]] 5 µM |  | -1.9 | -4.0 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | -1.8 | -2.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.7 | -3.2 |
|  | [[Trimetrexate (drug)]] 5 µM |  | -1.7 | -0.8 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | -1.7 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | solute carrier family 35 member F6 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p23.3 — chr2:26,764,284-26,781,231 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ20555, ANT2BP, TANGO9; previously C2orf18 |
| Gene groups (HGNC) | Solute carrier family 35 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8N357](https://www.uniprot.org/uniprotkb/Q8N357) (Solute carrier family 35 member F6):

> Involved in the maintenance of mitochondrial membrane potential in pancreatic ductal adenocarcinoma (PDAC) cells. Promotes pancreatic ductal adenocarcinoma (PDAC) cell growth. May play a role as a nucleotide-sugar transporter.

**Summary**, from NCBI Gene [54978](https://www.ncbi.nlm.nih.gov/gene/54978):

> Predicted to enable transmembrane transporter activity. Involved in negative regulation of mitochondrial outer membrane permeabilization involved in apoptotic signaling pathway and positive regulation of cell population proliferation. Located in lysosomal membrane and mitochondrion. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:26055](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26055) · Entrez [54978](https://www.ncbi.nlm.nih.gov/gene/54978) · UniProt [Q8N357](https://www.uniprot.org/uniprotkb/Q8N357) · Ensembl [ENSG00000213699](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000213699)

## Data

Gene col 13128: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13128); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13128, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13128]; `tensor/DDL_lfc|DDL_z.npy` [13128]; `embed/gene_vectors.npy` [13128]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13128 or target_col == 13128). Every well: [[SLC35F6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SLC35F6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
