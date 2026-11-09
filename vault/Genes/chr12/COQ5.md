---
symbol: "COQ5"
type: "gene"
col: 3172
ensembl_id: "ENSG00000110871"
name: "coenzyme Q5, methyltransferase"
location: "12q24.31"
module: 28
arm: "+"
pooled_cpm: 12.43
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 14
n_dd_up_clean: 8
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 1
direction_downstream: 1
tags: ["gene", "module/028"]
generated_by: "tahoemap"
---

# COQ5

*coenzyme Q5, methyltransferase* — 12q24.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.71× (z +11.1, q 5e-26, up in 32 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (4 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.431× (z -12.3, q 4e-32, down in 37 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DZIP3]] (+0.75, fdr 7e-06), [[ZBED9]] (+0.75, fdr 2e-05), [[NAIF1]] (+0.74, fdr 1e-05); moves opposite to [[TPST2]] (-0.65, fdr 1e-05), [[PIP4K2A]] (-0.64, fdr 1e-05), [[SNHG30]] (-0.63, fdr 1e-05).
> It sits in the **+** arm of [[Module 028]] (Intraflagellar transport).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[FGF12]] → it (grade C ⚠); 1 goes from it, the strongest it → [[USP40]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 5 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3172.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.71×** | +11.1 | 5e-26 | 32/44 (HEC-1-A, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.62×** | +10.0 | 3e-21 | 35/47 (NCI-H2030, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.84×** | +9.0 | 4e-17 | 23/35 (SW 900, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.89×** | +9.0 | 4e-17 | 18/24 (SW480, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.77×** | +8.4 | 7e-15 | 29/44 (LoVo, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.79×** | +8.2 | 2e-14 | 35/46 (LoVo, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.65×** | +7.4 | 1e-11 | 34/46 (PANC-1, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.51×** | +5.6 | 1e-06 | 15/30 (NCI-H1573, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.47×** | +5.4 | 3e-06 | 23/46 (NCI-H460, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.11× | +5.1 | 2e-05 | 4/48 (MIA PaCa-2, BT-474, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.35×** | +4.1 | 0.002 | 14/42 (SW480, LoVo, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Ponatinib (drug)]] 5 µM |  | **1.25×** | +3.3 | 0.052 | 11/47 (LoVo, KATO III, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~13% of this change | 1.24× | +3.0 | 0.10 | 10/41 (PANC-1, Panc 03.27, …) | inconsistent across doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 4 with an alert ⚠. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3172.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.431×** | -12.3 | 4e-32 | 37/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.458×** | -11.4 | 1e-27 | 33/47 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.475×** | -10.9 | 3e-25 | 36/46 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.479×** | -10.8 | 8e-25 | 32/45 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.634×** | -6.7 | 3e-09 | 26/47 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.671×** | -5.8 | 5e-07 | 21/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.680×** | -5.6 | 2e-06 | 24/45 (NCI-H460, SW480, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.703×** | -5.0 | 5e-05 | 18/41 (J82, PANC-1, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.714×** | -4.9 | 5e-05 | 20/46 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.737×** | -4.5 | 5e-04 | 16/47 (NCI-H460, CFPAC-1, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.733×** | -4.0 | 0.003 | 15/45 (MIA PaCa-2, KATO III, …) | inconsistent across doses | cell-cycle shift (explains ~4% here); position effect removed |
| [[EX229 (drug)]] 5 µM |  | **0.600×** | -3.9 | 0.005 | 14/44 (A498, PANC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~41% of this change | **0.799×** | -3.1 | 0.070 | 13/38 (SHP-77, LoVo, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.807×** | -3.1 | 0.070 | 15/46 (LoVo, HCT15, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.24 per unit of S-phase module lfc, +0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3172. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 23.6 | 0 | 6 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.189× (z -17.1) |
| [[SW480 (line)]] | alt | 12.0 | 1 (1 ⚠) | 4 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 3.30× (z +8.7) ⚠ toxic; transcription drop | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.212× (z -11.8) |
| [[HT-29 (line)]] | alt | 8.70 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.145× (z -9.6) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.168× (z -8.9) |
| [[hTERT-HPNE (line)]] | wt | 9.71 | 0 | 2 | — | [[Canagliflozin (drug)]] 5 µM 0.0976× (z -9.0) |
| [[LoVo (line)]] | wt | 14.9 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.24× (z +12.3) | [[Digitoxin (drug)]] 5 µM 0.249× (z -10.3) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 12.7 | 0 | 2 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.117× (z -10.7) ⚠ cell-cycle shift, explains ~50% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.311× (z -8.6) |
| [[A498 (line)]] | wt | 9.74 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.67× (z +8.6) | — |
| [[BT-474 (line)]] | alt | 17.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.82× (z +10.7) | — |
| [[COLO 205 (line)]] | alt | 15.9 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.161× (z -8.9) |
| [[H4 (line)]] | wt | 12.7 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0871× (z -8.9) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 14.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.52× (z +12.8) | — |
| [[LS 180 (line)]] | wt | 11.6 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.187× (z -8.9) |
| [[NCI-H2030 (line)]] | alt | 8.80 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.52× (z +9.3) | — |
| [[SW 900 (line)]] | alt | 9.58 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.127× (z -9.0) ⚠ transcription drop; cell-cycle shift, explains ~13% of this change |
| [[A-172 (line)]] | wt | 9.49 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 14.8 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 14.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 7.22 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 6.49 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 9.34 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 5.64 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 12.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 9.85 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 9.91 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 9.52 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 10.7 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 8.11 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 18.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 8.41 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 15.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.43 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 9.44 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 7.01 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 11.7 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.67 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3172), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DZIP3]] | +0.75 | +0.82 / +0.59 | both halves | 7e-06 |  |
| [[ZBED9]] | +0.75 | +0.85 / +0.48 | both halves | 2e-05 |  |
| [[NAIF1]] | +0.74 | +0.81 / +0.56 | both halves | 1e-05 |  |
| [[FAM200A]] | +0.74 | +0.86 / +0.46 | both halves | 3e-05 |  |
| [[METTL18]] | +0.74 | +0.82 / +0.54 | both halves | 1e-05 |  |
| [[ZNF620]] | +0.73 | +0.83 / +0.48 | both halves | 2e-05 |  |
| [[IFT74]] | +0.73 | +0.79 / +0.56 | both halves | 1e-05 |  |
| [[SMIM19]] | +0.71 | +0.71 / +0.61 | both halves | 7e-06 |  |
| [[DARS1]] | +0.71 | +0.74 / +0.58 | both halves | 8e-06 |  |
| [[PEX12]] | +0.71 | +0.82 / +0.49 | both halves | 1e-05 |  |
| [[ZNF181]] | +0.71 | +0.80 / +0.45 | both halves | 3e-05 |  |
| [[ZNF429]] | +0.71 | +0.79 / +0.35 | both halves | 1e-04 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TPST2]] | -0.65 | -0.73 / -0.49 | both halves | 1e-05 |  |
| [[PIP4K2A]] | -0.64 | -0.67 / -0.49 | both halves | 1e-05 |  |
| [[SNHG30]] | -0.63 | -0.71 / -0.55 | both halves | 1e-05 |  |
| [[LPCAT4]] | -0.62 | -0.68 / -0.45 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FGF12]] | C | FGF12 activity raises COQ5's level | lines that do not express FGF12 (4) vs lines expressing it (46) | 1.56× lower at baseline in the lines without FGF12 | 0.054 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: FAM182B, ENSG00000261341, WDR35; maybe low, not absent |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[USP40]] | C | COQ5's natural level strengthens USP40's drug response | COQ5's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.65, reverse +0.12; direction not clear | 0.048 | ⚠ tissue can mimic it; precision caveat; direction unclear |

## Where it sits

- **Module**: [[Module 028]] — Intraflagellar transport; 154 genes; this gene is in the **+** arm (projection on the module's main direction 0.805). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-28.2, 7.1); signed map (7.4, -23.6). **Vector** length 79.7, 15.0% of its response variance represented; |z| ≥ 3 in 874 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +8.8 | +10.0 |
|  | [[Harringtonine (drug)]] 5 µM |  | +8.2 | +8.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +7.2 | +8.4 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +6.2 | +7.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.9 | +11.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.7 | +5.4 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +3.0 | +4.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.0 | -1.6 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.5 | +0.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.4 | +3.3 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -4.3 | -11.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -3.4 | -10.9 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -3.4 | -10.8 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -3.2 | -4.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -3.2 | -12.3 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.1 | -5.6 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.8 | -1.7 |
|  | [[EX229 (drug)]] 5 µM |  | -1.7 | -3.9 |
|  | [[Gefitinib (drug)]] 5 µM |  | -1.4 | -1.7 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -1.3 | -2.9 |

## What is on record

|  |  |
|---|---|
| Name | coenzyme Q5, methyltransferase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q24.31 — chr12:120,503,279-120,534,434 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MGC4767 |
| Gene groups (HGNC) | 7BS small molecule methyltransferases; Small molecule methyltransferases |
| Hallmark sets | ADIPOGENESIS |
| Reactome | 3 pathways, smallest: Ubiquinol biosynthesis; Metabolism of cofactors; Metabolism of vitamins and cofactors |
| Matched by | ensembl_id |

**Function**, from UniProt [Q5HYK3](https://www.uniprot.org/uniprotkb/Q5HYK3) (2-methoxy-6-polyprenyl-1,4-benzoquinol methylase, mitochondrial):

> Methyltransferase required for the conversion of 2-decaprenyl-6-methoxy-1,4-benzoquinol (DDMQH2) to 2-decaprenyl-3-methyl-6-methoxy-1,4-benzoquinol (DMQH2).

**Summary**, from NCBI Gene [84274](https://www.ncbi.nlm.nih.gov/gene/84274):

> Enables 2-methoxy-6-polyprenyl-1,4-benzoquinol methyltransferase activity. Involved in methylation and ubiquinone biosynthetic process. Located in mitochondrial inner membrane and mitochondrial matrix. Part of protein-containing complex. Implicated in primary coenzyme Q10 deficiency 9. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:28722](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28722) · Entrez [84274](https://www.ncbi.nlm.nih.gov/gene/84274) · UniProt [Q5HYK3](https://www.uniprot.org/uniprotkb/Q5HYK3) · Ensembl [ENSG00000110871](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000110871)

## Data

Gene col 3172: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3172); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3172, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3172]; `tensor/DDL_lfc|DDL_z.npy` [3172]; `embed/gene_vectors.npy` [3172]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3172 or target_col == 3172). Every well: [[COQ5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/COQ5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
