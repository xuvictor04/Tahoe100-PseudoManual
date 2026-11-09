---
symbol: "PIP4P1"
type: "gene"
col: 9183
ensembl_id: "ENSG00000165782"
name: "phosphatidylinositol-4,5-bisphosphate 4-phosphatase 1"
location: "14q11.2"
module: 17
arm: "+"
pooled_cpm: 11.27
n_lines_expressing: 50
n_dd_up: 21
n_dd_down: 2
n_dd_up_clean: 17
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 1
direction_downstream: 1
tags: ["gene", "module/017"]
generated_by: "tahoemap"
---

# PIP4P1

*phosphatidylinositol-4,5-bisphosphate 4-phosphatase 1* — 14q11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.10× (z +15.0, q 0e+00, up in 37 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.605× (z -10.2, q 1e-21, down in 35 of 46 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 2 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 3 lines (SNU-423 0.0896×, SW480 0.230×, NCI-H2030 0.209×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 3 lines (A498 0.302×, A-427 0.213×, NCI-H23 0.330×); [[Temsirolimus (drug)]] 0.5 µM in 2 lines (HS-578T 0.0700×, HepG2/C3A 0.0976×); [[Triamcinolone (drug)]] 0.5 µM in 1 line (HCT15 0.0672×).
> Its strongest partners by |cos| (93 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 8 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TBC1D17]] (+0.66, fdr 1e-05), [[ABHD16A]] (+0.59, fdr 3e-05), [[MOSPD2]] (+0.58, fdr 3e-05); moves opposite to [[PHC2-AS1]] (-0.60, fdr 3e-05), [[PDK1-AS1]] (-0.58, fdr 3e-05), [[HSDL2-AS1]] (-0.52, fdr 0.002, ⚠ not reproduced), [[POC1B-AS1]] (-0.50, fdr 5e-04).
> It sits in the **+** arm of [[Module 017]] (Intraflagellar transport).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); 1 goes from it, the strongest it → [[NECAP1]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 4 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9183.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.10×** | +15.0 | 0e+00 | 37/46 (NCI-H460, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **2.39×** | +12.5 | 3e-33 | 44/47 (SW480, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.24×** | +11.6 | 1e-28 | 40/47 (SW480, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.22×** | +11.4 | 3e-28 | 40/47 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.85×** | +8.5 | 2e-15 | 27/42 (LoVo, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~6% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.62×** | +6.9 | 5e-10 | 23/45 (NCI-H460, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.56×** | +6.1 | 8e-08 | 25/46 (A-427, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~16% here); composition shift; position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.50×** | +5.8 | 5e-07 | 23/47 (NCI-H460, LS 180, …) | rises with dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **1.50×** | +5.8 | 5e-07 | 23/45 (RKO, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Cepharanthine (drug)]] 5 µM |  | **1.28×** | +5.0 | 3e-05 | 21/48 (NCI-H2030, NCI-H23, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.41×** | +4.9 | 6e-05 | 19/47 (NCI-H23, SW480, …) | rises with dose |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.58×** | +4.7 | 1e-04 | 13/44 (A-427, SW480, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.42×** | +4.6 | 2e-04 | 17/47 (LoVo, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.38×** | +4.6 | 2e-04 | 19/47 (PANC-1, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Berbamine (drug)]] 5 µM |  | **1.22×** | +3.9 | 0.003 | 9/48 (LoVo, BT-474, …) | rises with dose | position effect removed |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **1.32×** | +3.9 | 0.004 | 10/46 (CHP-212, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 9183.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 2 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 3 lines (SNU-423 0.0896×, SW480 0.230×, NCI-H2030 0.209×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 3 lines (A498 0.302×, A-427 0.213×, NCI-H23 0.330×); [[Temsirolimus (drug)]] 0.5 µM in 2 lines (HS-578T 0.0700×, HepG2/C3A 0.0976×); [[Triamcinolone (drug)]] 0.5 µM in 1 line (HCT15 0.0672×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.605×** | -10.2 | 1e-21 | 35/46 (A498, A-427, …) | top dose only | cell-cycle shift (explains ~1% here); position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.747×** | -4.0 | 0.016 | 13/46 (NCI-H23, LS 180, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | 0.786× | -3.3 | 0.16 | 15/45 (MIA PaCa-2, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Afatinib (drug)]] 0.5 µM |  | 0.860× | -3.0 | 0.35 | 6/48 (NCI-H2347, SW 1088, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.01 per unit of S-phase module lfc, +0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9183. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 8.89 | 4 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.70× (z +16.6) | [[Dinaciclib (drug)]] 0.05 µM 0.130× (z -11.6) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 7.14 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 4.23× (z +9.8) | [[Glycyrrhizic acid (drug)]] 0.05 µM 0.0879× (z -10.7) |
| [[NCI-H23 (line)]] | alt | 9.33 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 4.23× (z +11.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.330× (z -8.5) |
| [[SNU-423 (line)]] | alt | 11.8 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.97× (z +8.5) | [[Dinaciclib (drug)]] 5 µM 0.0896× (z -12.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A-427 (line)]] | wt | 15.4 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.213× (z -9.5) |
| [[A498 (line)]] | wt | 12.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.302× (z -12.4) |
| [[HCT15 (line)]] | alt | 12.7 | 0 | 1 | — | [[Triamcinolone (drug)]] 0.5 µM 0.0672× (z -11.0) |
| [[HepG2_C3A (line)]] | wt | 8.19 | 0 | 1 | — | [[Temsirolimus (drug)]] 0.5 µM 0.0976× (z -8.6) |
| [[Hs 766T (line)]] | wt | 9.50 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.79× (z +9.1) | — |
| [[HS-578T (line)]] | alt | 8.49 | 0 | 1 | — | [[Temsirolimus (drug)]] 0.5 µM 0.0700× (z -12.7) |
| [[hTERT-HPNE (line)]] | wt | 9.82 | 0 | 1 | — | [[Peretinoin (drug)]] 0.5 µM 0.0709× (z -10.6) |
| [[J82 (line)]] | alt | 11.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.48× (z +11.9) | — |
| [[KATO III (line)]] | alt | 12.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.72× (z +12.6) | — |
| [[LoVo (line)]] | wt | 11.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.91× (z +10.1) | — |
| [[NCI-H1573 (line)]] | alt | 11.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.64× (z +12.3) | — |
| [[NCI-H2030 (line)]] | alt | 21.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.209× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SW480 (line)]] | alt | 9.96 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.230× (z -10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A549 (line)]] | wt | 9.96 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 8.19 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 26.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 9.25 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 7.23 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 9.62 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 8.85 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 10.9 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 8.10 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 5.35 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 5.38 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 15.4 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 8.72 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 22.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 8.35 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 9.55 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 19.2 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 8.35 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 14.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 7.57 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 9.20 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 19.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 13.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9183), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*71 of its nearest partners move with it, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TBC1D17]] | +0.66 | +0.53 / +0.59 | both halves | 1e-05 |  |
| [[ABHD16A]] | +0.59 | +0.45 / +0.58 | both halves | 3e-05 |  |
| [[MOSPD2]] | +0.58 | +0.45 / +0.49 | both halves | 3e-05 |  |
| [[AMDHD2]] | +0.57 | +0.53 / +0.45 | both halves | 3e-05 |  |
| [[ROGDI]] | +0.57 | +0.40 / +0.43 | both halves | 5e-05 |  |
| [[CACFD1]] | +0.56 | +0.56 / +0.53 | both halves | 1e-05 |  |
| [[MBD6]] | +0.56 | +0.60 / +0.58 | both halves | 8e-06 |  |
| [[NUDT14]] | +0.56 | +0.46 / +0.46 | both halves | 2e-05 |  |
| [[ILVBL]] | +0.55 | +0.42 / +0.45 | both halves | 4e-05 |  |
| [[PNPLA2]] | +0.55 | +0.48 / +0.45 | both halves | 3e-05 | pathway: Phospholipid metabolism |
| [[LRCH4]] | +0.54 | +0.45 / +0.51 | both halves | 3e-05 |  |
| [[SNX15]] | +0.54 | +0.43 / +0.48 | both halves | 4e-05 |  |

## Genes that move opposite

*29 of its nearest partners move opposite, 6 of them with an alert (⚠; 6 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PHC2-AS1]] | -0.60 | -0.45 / -0.52 | both halves | 3e-05 |  |
| [[PDK1-AS1]] | -0.58 | -0.46 / -0.44 | both halves | 3e-05 |  |
| [[HSDL2-AS1]] | -0.52 | -0.11 / -0.43 | ⚠ not reproduced | 0.002 |  |
| [[POC1B-AS1]] | -0.50 | -0.23 / -0.38 | both halves | 5e-04 |  |
| [[YARS2]] | -0.50 | -0.25 / -0.36 | both halves | 4e-04 |  |
| [[DUS2]] | -0.49 | -0.25 / -0.38 | both halves | 4e-04 |  |
| [[DARS1-AS1]] | -0.49 | -0.28 / -0.30 | both halves | 3e-04 |  |
| [[KHDC1]] | -0.49 | -0.39 / -0.36 | both halves | 9e-05 |  |
| [[GNG12-AS1]] | -0.49 | -0.23 / -0.42 | both halves | 5e-04 |  |
| [[CCDC62]] | -0.49 | -0.21 / -0.40 | both halves | 6e-04 |  |
| [[NIPBL-DT]] | -0.48 | -0.15 / -0.39 | ⚠ not reproduced | 0.001 |  |
| [[MSANTD2]] | -0.48 | -0.21 / -0.40 | both halves | 7e-04 |  |
| [[MOSMO]] | -0.48 | -0.33 / -0.49 | both halves | 1e-04 |  |
| [[BEND3]] | -0.48 | -0.28 / -0.43 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises PIP4P1's level | compounds that target TOP2A: 2 of 5 lower it (Epirubicin, Idarubicin) | 40% of the class's compounds vs 0.6% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NECAP1]] | C | PIP4P1's natural level weakens NECAP1's drug response | PIP4P1's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.66, reverse -0.25; direction not clear | 0.039 | ⚠ tissue can mimic it; precision caveat; direction unclear |

## Where it sits

- **Module**: [[Module 017]] — Intraflagellar transport; 202 genes; this gene is in the **+** arm (projection on the module's main direction 0.410). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (0.9, -34.7); signed map (-7.0, 19.9). **Vector** length 80.9, 15.0% of its response variance represented; |z| ≥ 3 in 939 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~27% of this change | +3.8 | +3.5 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +3.1 | +8.5 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +2.9 | +4.7 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +2.8 | +11.4 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +2.6 | +5.8 |
|  | [[Entrectinib (drug)]] 5 µM |  | +2.4 | +1.9 |
|  | [[Bimiralisib (drug)]] 0.5 µM |  | +2.2 | +2.0 |
|  | [[Cepharanthine (drug)]] 5 µM |  | +2.2 | +5.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.2 | +4.9 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -7.1 | -10.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -5.9 | -3.3 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -5.4 | -4.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.2 | -1.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.7 | -1.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.5 | -1.9 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.4 | -0.7 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.7 | +0.8 |

## What is on record

|  |  |
|---|---|
| Name | phosphatidylinositol-4,5-bisphosphate 4-phosphatase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q11.2 — chr14:20,457,681-20,461,465 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MGC26684; previously C14orf9, TMEM55B |
| Gene groups (HGNC) | Phosphoinositide phosphatases |
| Reactome | 8 pathways, smallest: Synthesis of PIPs in the nucleus; PI5P Regulates TP53 Acetylation; Regulation of TP53 Activity through Acetylation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q86T03](https://www.uniprot.org/uniprotkb/Q86T03) (Type 1 phosphatidylinositol 4,5-bisphosphate 4-phosphatase):

> Catalyzes the hydrolysis of phosphatidylinositol-4,5-bisphosphate (PtdIns-4,5-P2) to phosphatidylinositol-4-phosphate (PtdIns-4-P). Does not hydrolyze phosphatidylinositol 3,4,5-trisphosphate, phosphatidylinositol 3,4-bisphosphate, inositol 3,5-bisphosphate, inositol 3,4-bisphosphate, phosphatidylinositol 5-monophosphate, phosphatidylinositol 4-monophosphate and phosphatidylinositol 3-monophosphate. Regulates lysosomal positioning by recruiting JIP4 to lysosomal membranes, thus inducing …

**Summary**, from NCBI Gene [90809](https://www.ncbi.nlm.nih.gov/gene/90809):

> TMEM55B catalyzes the degradation of phosphatidylinositol 4,5-bisphosphate (PtdIns-4,5-P2) by removing the 4-phosphate (Ungewickell et al., 2005 [PubMed 16365287]).[supplied by OMIM, Mar 2008]

**Accessions** — [HGNC:19299](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19299) · Entrez [90809](https://www.ncbi.nlm.nih.gov/gene/90809) · UniProt [Q86T03](https://www.uniprot.org/uniprotkb/Q86T03) · Ensembl [ENSG00000165782](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000165782)

## Data

Gene col 9183: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9183); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9183, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9183]; `tensor/DDL_lfc|DDL_z.npy` [9183]; `embed/gene_vectors.npy` [9183]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9183 or target_col == 9183). Every well: [[PIP4P1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PIP4P1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
