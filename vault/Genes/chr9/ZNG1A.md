---
symbol: "ZNG1A"
type: "gene"
col: 10296
ensembl_id: "ENSG00000172785"
name: "Zn regulated GTPase metalloprotein activator 1A"
location: "9p24.3"
module: 28
arm: "+"
pooled_cpm: 19.35
n_lines_expressing: 50
n_dd_up: 24
n_dd_down: 1
n_dd_up_clean: 12
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/028"]
generated_by: "tahoemap"
---

# ZNG1A

*Zn regulated GTPase metalloprotein activator 1A* — 9p24.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (12 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.73× (z +13.3, q 1e-37, up in 33 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[PH-797804 (drug)]] 5 µM: 0.596× (z -4.7, q 0.002, down in 13 of 44 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 1 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Temsirolimus (drug)]] 0.5 µM in 1 line (H4 0.0896×); [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM in 1 line (hTERT-HPNE 0.0759×); [[AZD2858 (drug)]] 0.5 µM in 1 line (A-427 0.0937×; ⚠ toxic); [[Glycyrrhizic acid (drug)]] 0.5 µM in 1 line (BT-474 0.0870×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNG1B]] (+0.82, fdr 7e-06), [[GOLGA1]] (+0.70, fdr 7e-06), [[RPAP2]] (+0.64, fdr 7e-06); moves opposite to [[LMTK2]] (-0.58, fdr 2e-05), [[STRN]] (-0.54, fdr 1e-04), [[ILRUN]] (-0.53, fdr 6e-05).
> It sits in the **+** arm of [[Module 028]] (Intraflagellar transport).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[ASCC3]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 15 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10296.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.73×** | +13.3 | 1e-37 | 33/47 (NCI-H460, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.06×** | +12.5 | 4e-33 | 35/47 (NCI-H460, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **2.06×** | +11.5 | 2e-28 | 26/36 (SW480, SNU-423, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | **2.00×** | +11.5 | 2e-28 | 26/31 (SW480, KATO III, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | **1.90×** | +11.1 | 2e-26 | 30/40 (SW480, C-33 A, …) | all doses, flat | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.51×** | +10.1 | 6e-22 | 32/47 (HT-29, KATO III, …) | top dose only | cell-cycle shift (explains ~18% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.75×** | +9.2 | 2e-18 | 33/47 (COLO 205, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **1.59×** | +8.0 | 8e-14 | 31/48 (A498, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **1.57×** | +7.7 | 6e-13 | 36/48 (A498, A-172, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **1.53×** | +7.3 | 2e-11 | 23/47 (KATO III, A-172, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.52×** | +7.2 | 3e-11 | 29/48 (NCI-H460, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.47×** | +6.4 | 7e-09 | 21/45 (MIA PaCa-2, A-172, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.45×** | +6.1 | 4e-08 | 25/47 (HOP62, SW480, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.42×** | +6.1 | 5e-08 | 21/48 (NCI-H460, HEC-1-A, …) | all doses, stronger at high dose | position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.41×** | +5.6 | 7e-07 | 21/46 (HOP62, SW480, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.30×** | +4.2 | 0.001 | 14/46 (NCI-H460, HEC-1-A, …) | all doses, stronger at high dose | low cells (technical?) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.35×** | +3.7 | 0.006 | 8/44 (HOP62, J82, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **1.49×** | +3.6 | 0.010 | 10/47 (NCI-H460, MIA PaCa-2, …) | top dose only | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.47×** | +3.4 | 0.016 | 6/45 (MIA PaCa-2, NCI-H460, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[venetoclax (drug)]] 5 µM |  | **1.44×** | +3.3 | 0.024 | 5/43 (SW 900, Hs 766T, …) | top dose only | noisy plate (z scaled) |
| [[vincristine (drug)]] 0.5 µM |  | **1.29×** | +3.1 | 0.046 | 10/47 (HS-578T, HCT15, …) | two highest doses | low cells (technical?); noisy plate (z scaled); position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.14× | +3.1 | 0.046 | 9/48 (SW1417, SNU-1, …) | rises with dose |  |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | 1.18× | +2.8 | 0.088 | 7/45 (HS-578T, RPMI-7951, …) | inconsistent across doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 10296.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 1 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Temsirolimus (drug)]] 0.5 µM in 1 line (H4 0.0896×); [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM in 1 line (hTERT-HPNE 0.0759×); [[AZD2858 (drug)]] 0.5 µM in 1 line (A-427 0.0937×; ⚠ toxic); [[Glycyrrhizic acid (drug)]] 0.5 µM in 1 line (BT-474 0.0870×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[PH-797804 (drug)]] 5 µM |  | **0.596×** | -4.7 | 0.002 | 13/44 (H4, SK-MEL-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | 0.871× | -3.4 | 0.18 | 12/48 (Panc 03.27, HOP62, …) | rises with dose |  |
| [[TAK-901 (drug)]] 0.05 µM |  | 0.820× | -3.3 | 0.21 | 10/47 (C32, RKO, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.34 per unit of S-phase module lfc, +0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10296. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 26.1 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.95× (z +10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.03× (z +9.7) | — |
| [[KATO III (line)]] | alt | 31.7 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.77× (z +12.2) | — |
| [[A-427 (line)]] | wt | 17.7 | 0 | 2 (1 ⚠) | — | [[AZD2858 (drug)]] 0.5 µM 0.0937× (z -10.2) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.219× (z -9.2) |
| [[NCI-H460 (line)]] | wt | 22.8 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.03× (z +14.0) | — |
| [[A-172 (line)]] | wt | 20.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.28× (z +8.5) | — |
| [[BT-474 (line)]] | alt | 7.79 | 0 | 1 | — | [[Glycyrrhizic acid (drug)]] 0.5 µM 0.0870× (z -9.5) |
| [[C-33 A (line)]] | alt | 22.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.83× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | — |
| [[COLO 205 (line)]] | alt | 12.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.51× (z +8.5) | — |
| [[H4 (line)]] | wt | 19.5 | 0 | 1 | — | [[Temsirolimus (drug)]] 0.5 µM 0.0896× (z -11.1) |
| [[HCT15 (line)]] | alt | 44.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.58× (z +9.1) | — |
| [[HEC-1-A (line)]] | alt | 27.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.22× (z +9.6) | — |
| [[hTERT-HPNE (line)]] | wt | 11.9 | 0 | 1 | — | [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM 0.0759× (z -11.1) |
| [[SNU-423 (line)]] | alt | 23.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 3.92× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[SW 900 (line)]] | alt | 16.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.38× (z +9.4) | — |
| [[A498 (line)]] | wt | 21.2 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 13.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 22.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 8.41 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 19.3 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 15.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 25.2 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 23.3 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 15.7 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 27.5 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 29.0 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 20.2 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 27.8 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 27.6 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 9.83 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 6.23 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 20.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 22.4 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 28.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 9.60 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 29.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 28.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 18.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10296), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*77 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNG1B]] | +0.82 | +0.85 / +0.76 | both halves | 7e-06 | same gene group; STRING 929 |
| [[GOLGA1]] | +0.70 | +0.68 / +0.60 | both halves | 7e-06 |  |
| [[RPAP2]] | +0.64 | +0.65 / +0.64 | both halves | 7e-06 |  |
| [[UBE2V2]] | +0.63 | +0.63 / +0.63 | both halves | 7e-06 |  |
| [[TIMMDC1]] | +0.62 | +0.72 / +0.52 | both halves | 1e-05 |  |
| [[RAD50]] | +0.61 | +0.67 / +0.54 | both halves | 1e-05 |  |
| [[CCAR1]] | +0.60 | +0.67 / +0.59 | both halves | 7e-06 |  |
| [[POLI]] | +0.59 | +0.60 / +0.53 | both halves | 1e-05 |  |
| [[AIMP1]] | +0.59 | +0.67 / +0.50 | both halves | 1e-05 |  |
| [[TRIP11]] | +0.57 | +0.73 / +0.41 | both halves | 4e-05 |  |
| [[CHMP4A]] | +0.57 | +0.67 / +0.45 | both halves | 3e-05 |  |
| [[ICE2]] | +0.57 | +0.64 / +0.44 | both halves | 3e-05 |  |

## Genes that move opposite

*23 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LMTK2]] | -0.58 | -0.60 / -0.48 | both halves | 2e-05 |  |
| [[STRN]] | -0.54 | -0.67 / -0.35 | both halves | 1e-04 |  |
| [[ILRUN]] | -0.53 | -0.63 / -0.38 | both halves | 6e-05 |  |
| [[FOXK1]] | -0.52 | -0.64 / -0.39 | both halves | 5e-05 |  |
| [[NFATC3]] | -0.51 | -0.62 / -0.30 | both halves | 2e-04 |  |
| [[TECR]] | -0.51 | -0.59 / -0.39 | both halves | 6e-05 |  |
| [[MFSD14CP]] | -0.50 | -0.60 / -0.39 | both halves | 5e-05 |  |
| [[SEC11A]] | -0.50 | -0.62 / -0.37 | both halves | 8e-05 |  |
| [[LPCAT4]] | -0.50 | -0.64 / -0.36 | both halves | 9e-05 |  |
| [[ABHD12]] | -0.50 | -0.65 / -0.31 | both halves | 2e-04 |  |
| [[PTK7]] | -0.50 | -0.57 / -0.38 | both halves | 7e-05 |  |
| [[UBE2G1]] | -0.50 | -0.64 / -0.29 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ASCC3]] | C | ASCC3's natural level weakens ZNG1A's drug response | ASCC3's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.62, reverse -0.20; direction not clear | 0.096 | ⚠ tissue can mimic it; precision caveat; direction unclear |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 028]] — Intraflagellar transport; 154 genes; this gene is in the **+** arm (projection on the module's main direction 0.536). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-24.1, 17.1); signed map (8.6, -16.4). **Vector** length 63.7, 10.5% of its response variance represented; |z| ≥ 3 in 823 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.4 | +12.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.0 | +6.1 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +3.9 | +7.2 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +3.2 | +13.3 |
|  | [[Harringtonine (drug)]] 5 µM |  | +2.7 | +9.2 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.4 | +4.2 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +1.7 | +3.6 |
|  | [[TAK-733 (drug)]] 5 µM |  | +1.6 | +2.7 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +1.5 | +1.0 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -3.0 | -0.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.4 | -3.0 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -2.3 | +1.6 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -2.3 | -0.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.7 | +1.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.5 | -4.7 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.5 | +2.4 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.4 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | Zn regulated GTPase metalloprotein activator 1A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9p24.3 — chr9:120,837-179,147 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously CBWD1 |
| Gene groups (HGNC) | Zn regulated GTPase metalloprotein activator 1 family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BRT8](https://www.uniprot.org/uniprotkb/Q9BRT8) (Zinc-regulated GTPase metalloprotein activator 1A):

> Zinc chaperone that directly transfers zinc cofactor to target metalloproteins, thereby activating them. Catalyzes zinc insertion into the active site of methionine aminopeptidase METAP1, which function to cleave the initiator methionine from polypeptides during or after protein translation. Mechanistically, the N-terminal psi-PxLVp motif binds to the C6H2-type zinc finger of inactive form of METAP1. After formation of the docked complex, zinc is transferred from the CXCC motif in the GTPase …

**Summary**, from NCBI Gene [55871](https://www.ncbi.nlm.nih.gov/gene/55871):

> Predicted to enable GTPase activity; zinc chaperone activity; and zinc ion binding activity. Involved in kidney development. Predicted to be located in nucleus. Predicted to be active in cytoplasm. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:17134](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17134) · Entrez [55871](https://www.ncbi.nlm.nih.gov/gene/55871) · UniProt [Q9BRT8](https://www.uniprot.org/uniprotkb/Q9BRT8) · Ensembl [ENSG00000172785](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000172785)

## Data

Gene col 10296: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10296); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10296, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10296]; `tensor/DDL_lfc|DDL_z.npy` [10296]; `embed/gene_vectors.npy` [10296]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10296 or target_col == 10296). Every well: [[ZNG1A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZNG1A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
