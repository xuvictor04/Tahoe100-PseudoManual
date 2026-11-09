---
symbol: "PEX5"
type: "gene"
col: 6278
ensembl_id: "ENSG00000139197"
name: "peroxisomal biogenesis factor 5"
location: "12p13.31"
module: 2
arm: "+"
pooled_cpm: 16.33
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 2
n_dd_up_clean: 11
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/002"]
generated_by: "tahoemap"
---

# PEX5

*peroxisomal biogenesis factor 5* — 12p13.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (2 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 1.91× (z +10.8, q 1e-24, up in 38 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Epirubicin (hydrochloride) (drug)]] 5 µM: 0.719× (z -5.3, q 6e-05, down in 23 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 10 here, 6 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (RKO 0.214×; ⚠ cell-cycle shift, explains ~0% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (RKO 0.263×; ⚠ cell-cycle shift, would explain all of this change); [[Dinaciclib (drug)]] 0.5 µM in 1 line (RKO 0.219×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~2% of this change); [[Procainamide (hydrochloride) (drug)]] 0.05 µM in 1 line (HepG2/C3A 0.0931×); [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 1 line (SW48 0.114×); [[Hydroxyurea (drug)]] 0.05 µM in 1 line (COLO 205 0.109×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[POLRMT]] (+0.64, fdr 2e-05), [[ACTR5]] (+0.63, fdr 1e-05), [[ST6GALNAC6]] (+0.63, fdr 2e-05); moves opposite to [[MED13]] (-0.60, fdr 8e-05), [[DLEU2]] (-0.59, fdr 1e-05), [[BAZ2B]] (-0.55, fdr 1e-04).
> It sits in the **+** arm of [[Module 002]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 2 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6278.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **1.91×** | +10.8 | 1e-24 | 38/48 (SW480, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.88×** | +10.6 | 1e-23 | 39/47 (SW480, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **1.72×** | +9.0 | 4e-17 | 38/47 (SW480, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.64×** | +8.3 | 2e-14 | 31/47 (SW480, Hs 766T, …) | all doses, flat |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.84×** | +5.3 | 1e-05 | 20/44 (Panc 03.27, A-427, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.29×** | +4.2 | 0.003 | 14/48 (NCI-H2347, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **1.27×** | +4.0 | 0.006 | 13/46 (Panc 03.27, SW480, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.28×** | +3.8 | 0.009 | 18/47 (HEC-1-A, SW48, …) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.26×** | +3.7 | 0.012 | 16/46 (NCI-H23, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dihydroartemisinin (drug)]] 5 µM |  | **1.23×** | +3.4 | 0.034 | 6/47 (hTERT-HPNE, HOP62, …) | top dose only |  |
| [[Erlotinib (drug)]] 0.05 µM |  | **1.23×** | +3.2 | 0.063 | 4/47 (SK-MEL-2, NCI-H23, …) | inconsistent across doses | position effect removed |
| [[Glycyrrhizic acid (drug)]] 0.5 µM |  | **1.21×** | +3.1 | 0.090 | 6/47 (NCI-H1573, SW480, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.20×** | +3.1 | 0.090 | 11/47 (NCI-H460, NCI-H23, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 1 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 6278.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 10 here, 6 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (RKO 0.214×; ⚠ cell-cycle shift, explains ~0% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (RKO 0.263×; ⚠ cell-cycle shift, would explain all of this change); [[Dinaciclib (drug)]] 0.5 µM in 1 line (RKO 0.219×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~2% of this change); [[Procainamide (hydrochloride) (drug)]] 0.05 µM in 1 line (HepG2/C3A 0.0931×); [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 1 line (SW48 0.114×); [[Hydroxyurea (drug)]] 0.05 µM in 1 line (COLO 205 0.109×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.719×** | -5.3 | 6e-05 | 23/48 (NCI-H23, RKO, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.799×** | -3.6 | 0.079 | 17/46 (SW48, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Thymol (drug)]] 5 µM |  | 0.863× | -3.5 | 0.079 | 11/48 (NCI-H2347, J82, …) | top dose only | position effect removed |
| [[Entrectinib (drug)]] 5 µM |  | 0.819× | -3.4 | 0.11 | 10/47 (HS-578T, Panc 03.27, …) | top dose only | position effect removed |
| [[Bimiralisib (drug)]] 0.5 µM |  | 0.760× | -3.3 | 0.11 | 14/44 (NCI-H1792, SK-MEL-2, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Larotrectinib (drug)]] 0.05 µM |  | 0.830× | -3.1 | 0.14 | 7/48 (MIA PaCa-2, NCI-H2347, …) | inconsistent across doses | position effect removed |
| [[Palmatine (chloride) (drug)]] 0.5 µM |  | 0.833× | -3.1 | 0.14 | 12/46 (CHP-212, SHP-77, …) | inconsistent across doses |  |
| [[Binimetinib (drug)]] 0.5 µM |  | 0.860× | -3.1 | 0.14 | 6/48 (RKO, CHP-212, …) | rises with dose | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | 0.828× | -3.1 | 0.14 | 11/47 (PANC-1, LOX-IMVI, …) | top dose only | composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.08 per unit of S-phase module lfc, -0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6278. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[RKO (line)]] | wt | 61.1 | 0 | 4 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.214× (z -15.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW480 (line)]] | alt | 25.0 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 2.71× (z +9.7) | — |
| [[HepG2_C3A (line)]] | wt | 14.0 | 0 | 2 (1 ⚠) | — | [[Procainamide (hydrochloride) (drug)]] 0.05 µM 0.0931× (z -10.0) |
| [[COLO 205 (line)]] | alt | 10.9 | 0 | 1 | — | [[Hydroxyurea (drug)]] 0.05 µM 0.109× (z -8.7) |
| [[H4 (line)]] | wt | 32.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.158× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H1792 (line)]] | alt | 12.8 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.42× (z +11.1) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[NCI-H23 (line)]] | alt | 32.5 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.325× (z -8.6) |
| [[SW48 (line)]] | wt | 15.8 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.114× (z -8.9) |
| [[A-172 (line)]] | wt | 8.75 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 27.8 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 13.0 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 11.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 27.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 6.55 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 15.6 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 6.21 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 16.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 13.9 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 9.80 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 15.1 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 13.9 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 22.2 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 11.1 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 27.3 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 19.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 12.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 9.31 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 22.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 15.2 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 19.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 20.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 17.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6278), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[POLRMT]] | +0.64 | +0.61 / +0.47 | both halves | 2e-05 |  |
| [[ACTR5]] | +0.63 | +0.52 / +0.55 | both halves | 1e-05 |  |
| [[ST6GALNAC6]] | +0.63 | +0.58 / +0.47 | both halves | 2e-05 |  |
| [[NOMO3]] | +0.62 | +0.48 / +0.52 | both halves | 2e-05 | pathway: Protein localization |
| [[CPSF1]] | +0.61 | +0.48 / +0.52 | both halves | 2e-05 |  |
| [[TATDN2]] | +0.61 | +0.56 / +0.56 | both halves | 1e-05 |  |
| [[NLE1]] | +0.61 | +0.59 / +0.47 | both halves | 2e-05 |  |
| [[NOC2L]] | +0.61 | +0.52 / +0.53 | both halves | 1e-05 |  |
| [[ABHD17A]] | +0.60 | +0.49 / +0.54 | both halves | 1e-05 |  |
| [[KLHL17]] | +0.60 | +0.58 / +0.48 | both halves | 2e-05 |  |
| [[WDR3]] | +0.60 | +0.56 / +0.53 | both halves | 1e-05 |  |
| [[GTPBP3]] | +0.60 | +0.54 / +0.42 | both halves | 4e-05 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MED13]] | -0.60 | -0.54 / -0.37 | both halves | 8e-05 |  |
| [[DLEU2]] | -0.59 | -0.53 / -0.50 | both halves | 1e-05 |  |
| [[BAZ2B]] | -0.55 | -0.48 / -0.33 | both halves | 1e-04 |  |
| [[ANKHD1-EIF4EBP3]] | -0.55 | -0.55 / -0.35 | both halves | 1e-04 |  |
| [[KANSL1L]] | -0.53 | -0.45 / -0.36 | both halves | 1e-04 |  |
| [[C11orf58]] | -0.53 | -0.48 / -0.32 | both halves | 2e-04 |  |
| [[ASH1L]] | -0.53 | -0.49 / -0.33 | both halves | 1e-04 |  |
| [[SMIM14]] | -0.53 | -0.53 / -0.48 | both halves | 2e-05 |  |
| [[ATOSA]] | -0.51 | -0.48 / -0.42 | both halves | 4e-05 |  |
| [[GTF2IRD2B]] | -0.51 | -0.47 / -0.29 | both halves | 2e-04 |  |
| [[LINC02307]] | -0.51 | -0.42 / -0.39 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises PEX5's level | compounds that target TOP2A: 2 of 5 lower it (Doxorubicin, Epirubicin) | 40% of the class's compounds vs 0.6% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[HGF]] | B | HGF activity raises PEX5's level | lines that do not express HGF (38) vs lines expressing it (12) | 1.41× lower at baseline in the lines without HGF | 0.078 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: SYT4, RIT2, CALCA |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 002]]; 248 genes; this gene is in the **+** arm (projection on the module's main direction 0.534). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.21).
- **Nodal map** (x, y) = (-7.6, -25.1); signed map (-43.3, -12.9). **Vector** length 69.8, 11.1% of its response variance represented; |z| ≥ 3 in 918 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +4.0 | -0.4 |
|  | [[Panobinostat (drug)]] 5 µM |  | +4.0 | +10.8 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +3.8 | +8.3 |
|  | [[Belinostat (drug)]] 5 µM |  | +3.7 | +9.0 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +3.5 | +10.6 |
|  | [[EX229 (drug)]] 5 µM |  | +2.5 | +2.9 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +1.9 | +2.9 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +1.9 | +2.4 |
|  | [[Belzutifan (drug)]] 5 µM |  | +1.6 | +1.8 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | +1.5 | +2.8 |
| fall | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -3.0 | -3.6 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | -2.8 | -3.1 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -2.7 | -5.3 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -1.9 | -1.8 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift | -1.8 | +0.1 |
|  | [[Binimetinib (drug)]] 5 µM |  | -1.7 | -2.8 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -1.7 | -3.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -1.5 | -1.5 |
|  | [[Binimetinib (drug)]] 0.05 µM |  | -1.5 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | peroxisomal biogenesis factor 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12p13.31 — chr12:7,188,685-7,218,574 (+) |
| Ensembl biotype | protein_coding |
| Also known as | PTS1R; previously PXR1 |
| Gene groups (HGNC) | Tetratricopeptide repeat domain containing; Peroxins |
| Hallmark sets | PEROXISOME |
| Reactome | 8 pathways, smallest: Pexophagy; E3 ubiquitin ligases ubiquitinate target proteins; Peroxisomal protein import |
| Matched by | ensembl_id |

**Function**, from UniProt [P50542](https://www.uniprot.org/uniprotkb/P50542) (Peroxisomal targeting signal 1 receptor):

> Receptor that mediates peroxisomal import of proteins containing a C-terminal PTS1-type tripeptide peroxisomal targeting signal (SKL-type). Binds to cargo proteins containing a PTS1 peroxisomal targeting signal in the cytosol, and translocates them into the peroxisome matrix by passing through the PEX13-PEX14 docking complex along with cargo proteins. PEX5 receptor is then retrotranslocated into the cytosol, leading to release of bound cargo in the peroxisome matrix, and reset for a subsequent …

**Summary**, from NCBI Gene [5830](https://www.ncbi.nlm.nih.gov/gene/5830):

> The product of this gene binds to the C-terminal PTS1-type tripeptide peroxisomal targeting signal (SKL-type) and plays an essential role in peroxisomal protein import. Peroxins (PEXs) are proteins that are essential for the assembly of functional peroxisomes. The peroxisome biogenesis disorders (PBDs) are a group of genetically heterogeneous autosomal recessive, lethal diseases characterized by multiple defects in peroxisome function. The peroxisomal biogenesis disorders are a heterogeneous …

**Accessions** — [HGNC:9719](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9719) · Entrez [5830](https://www.ncbi.nlm.nih.gov/gene/5830) · UniProt [P50542](https://www.uniprot.org/uniprotkb/P50542) · Ensembl [ENSG00000139197](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000139197)

## Data

Gene col 6278: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6278); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6278, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6278]; `tensor/DDL_lfc|DDL_z.npy` [6278]; `embed/gene_vectors.npy` [6278]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6278 or target_col == 6278). Every well: [[PEX5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PEX5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
