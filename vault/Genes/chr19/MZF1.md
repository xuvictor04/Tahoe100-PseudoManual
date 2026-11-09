---
symbol: "MZF1"
type: "gene"
col: 1793
ensembl_id: "ENSG00000099326"
name: "myeloid zinc finger 1"
location: "19q13.43"
module: 17
arm: "-"
pooled_cpm: 21.39
n_lines_expressing: 50
n_dd_up: 1
n_dd_down: 31
n_dd_up_clean: 1
n_dd_down_clean: 21
in_vector_space: true
direction_upstream: 0
direction_downstream: 1
tags: ["gene", "module/017"]
generated_by: "tahoemap"
---

# MZF1

*myeloid zinc finger 1* — 19q13.43

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 1 drug-dose (none with an alert); the strongest is [[GSK1059615 (drug)]] 5 µM: 1.52× (z +3.9, q 0.057, up in 8 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 31 drug-doses (10 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.475× (z -18.5, q 0e+00, down in 43 of 47 measured lines).
> Its strongest partners by |cos| (91 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 10 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EOLA2-DT]] (+0.67, fdr 7e-06), [[KAT8]] (+0.65, fdr 7e-06), [[ZNF586]] (+0.61, fdr 1e-05); moves opposite to [[RAB11A]] (-0.53, fdr 5e-05), [[CYB5A]] (-0.52, fdr 5e-05), [[SUCLG1]] (-0.52, fdr 3e-05).
> It sits in the **-** arm of [[Module 017]] (Intraflagellar transport).
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 1 goes from it, the strongest it → [[TMEM91]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 1 of them raises it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1793.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[GSK1059615 (drug)]] 5 µM |  | **1.52×** | +3.9 | 0.057 | 8/46 (SW480, A-172, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 0.5 µM |  | 1.29× | +3.2 | 0.42 | 8/46 (CFPAC-1, SNU-423, …) | rises with dose | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 35 in all, 12 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 31 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1793.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.475×** | -18.5 | 0e+00 | 43/47 (PANC-1, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **0.363×** | -17.9 | 0e+00 | 43/48 (HEC-1-A, PANC-1, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.407×** | -15.8 | 0e+00 | 46/48 (HEC-1-A, HCT15, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **0.411×** | -15.7 | 0e+00 | 44/48 (HCT15, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.460×** | -13.7 | 2e-40 | 38/46 (MIA PaCa-2, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.499×** | -12.2 | 2e-32 | 39/48 (PANC-1, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **0.539×** | -10.5 | 1e-23 | 34/47 (PANC-1, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **0.575×** | -9.7 | 2e-20 | 41/45 (SNU-423, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Selinexor (drug)]] 5 µM |  | **0.713×** | -8.4 | 3e-15 | 27/48 (SNU-423, PANC-1, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.724×** | -8.0 | 7e-14 | 29/47 (HEC-1-A, HCT15, …) | top dose only | cell-cycle shift (explains ~17% here); position effect removed |
| [[Brivudine (drug)]] 5 µM |  | **0.429×** | -7.8 | 3e-13 | 31/48 (SNU-1, NCI-H460, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.699×** | -6.3 | 1e-08 | 24/47 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.699×** | -6.0 | 6e-08 | 24/47 (RPMI-7951, HEC-1-A, …) | top dose only | position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~38% of this change | **0.714×** | -5.7 | 5e-07 | 23/45 (PANC-1, H4, …) | rises with dose | position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **0.817×** | -5.0 | 2e-05 | 22/48 (J82, PANC-1, …) | rises with dose |  |
| [[EX229 (drug)]] 5 µM |  | **0.610×** | -4.5 | 2e-04 | 21/45 (SNU-1, RPMI-7951, …) | rises with dose | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.790×** | -3.9 | 0.003 | 17/47 (HT-29, SNU-423, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.27 per unit of S-phase module lfc, -0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1793. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 29.1 | 0 | 9 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.226× (z -20.3) |
| [[HEC-1-A (line)]] | alt | 37.8 | 0 | 7 | — | [[Panobinostat (drug)]] 5 µM 0.280× (z -12.3) |
| [[RPMI-7951 (line)]] | alt | 42.1 | 0 | 6 (2 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.175× (z -12.6) ⚠ transcription drop; cell-cycle shift, explains ~58% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.220× (z -10.9) |
| [[HCT15 (line)]] | alt | 84.8 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.154× (z -12.5) |
| [[MIA PaCa-2 (line)]] | alt | 31.0 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0751× (z -20.1) |
| [[NCI-H1792 (line)]] | alt | 20.7 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.307× (z -10.6) |
| [[LOX-IMVI (line)]] | wt | 14.6 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0901× (z -13.9) |
| [[NCI-H1573 (line)]] | alt | 19.3 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.295× (z -9.0) |
| [[NCI-H23 (line)]] | alt | 19.2 | 0 | 3 | — | [[Belinostat (drug)]] 5 µM 0.243× (z -9.4) |
| [[NCI-H460 (line)]] | wt | 19.7 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.144× (z -16.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.328× (z -14.0) |
| [[A-172 (line)]] | wt | 28.8 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.349× (z -11.3) |
| [[C-33 A (line)]] | alt | 37.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.139× (z -12.8) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[HT-29 (line)]] | alt | 56.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.340× (z -13.2) |
| [[hTERT-HPNE (line)]] | wt | 20.0 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.235× (z -9.9) |
| [[SNU-423 (line)]] | alt | 14.0 | 0 | 2 | — | [[Selinexor (drug)]] 5 µM 0.150× (z -15.5) |
| [[A498 (line)]] | wt | 12.3 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.236× (z -9.2) |
| [[CFPAC-1 (line)]] | alt | 17.0 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.278× (z -8.8) |
| [[COLO 205 (line)]] | alt | 22.2 | 0 | 1 (1 ⚠) | — | [[NG25 (drug)]] 5 µM 0.0647× (z -8.9) ⚠ cell-cycle shift, explains ~60% of this change |
| [[HOP62 (line)]] | alt | 12.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.272× (z -11.9) |
| [[HS-578T (line)]] | alt | 16.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.192× (z -13.0) |
| [[J82 (line)]] | alt | 13.3 | 0 | 1 | — | [[Selinexor (drug)]] 5 µM 0.351× (z -9.6) |
| [[KATO III (line)]] | alt | 32.2 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.166× (z -13.2) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[Panc 03.27 (line)]] | alt | 14.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.131× (z -15.1) |
| [[SW480 (line)]] | alt | 24.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.468× (z -10.7) |
| [[A-427 (line)]] | wt | 16.8 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 24.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 7.68 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 10.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 27.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 33.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 10.8 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 12.3 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 17.2 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 22.2 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 9.86 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 25.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 5.93 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 21.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 8.54 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 19.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 28.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 23.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 21.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 12.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1793), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*65 of its nearest partners move with it, 7 of them with an alert (⚠; 7 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EOLA2-DT]] | +0.67 | +0.62 / +0.67 | both halves | 7e-06 |  |
| [[KAT8]] | +0.65 | +0.60 / +0.58 | both halves | 7e-06 |  |
| [[ZNF586]] | +0.61 | +0.49 / +0.58 | both halves | 1e-05 | same gene group |
| [[SLC25A53]] | +0.59 | +0.55 / +0.50 | both halves | 1e-05 |  |
| [[LMF1]] | +0.58 | +0.47 / +0.59 | both halves | 2e-05 |  |
| [[ITFG2]] | +0.58 | +0.42 / +0.58 | both halves | 4e-05 |  |
| [[SYMPK]] | +0.57 | +0.66 / +0.42 | both halves | 4e-05 |  |
| [[MIATNB]] | +0.54 | +0.48 / +0.49 | both halves | 2e-05 |  |
| [[APTX]] | +0.54 | +0.45 / +0.45 | both halves | 3e-05 | same gene group |
| [[WDR81]] | +0.53 | +0.32 / +0.54 | both halves | 2e-04 |  |
| [[FBXL19-AS1]] | +0.53 | +0.30 / +0.49 | both halves | 2e-04 |  |
| [[PROSER3]] | +0.53 | +0.45 / +0.53 | both halves | 3e-05 |  |

## Genes that move opposite

*35 of its nearest partners move opposite, 3 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RAB11A]] | -0.53 | -0.55 / -0.39 | both halves | 5e-05 |  |
| [[CYB5A]] | -0.52 | -0.39 / -0.58 | both halves | 5e-05 |  |
| [[SUCLG1]] | -0.52 | -0.52 / -0.44 | both halves | 3e-05 |  |
| [[NDFIP1]] | -0.52 | -0.30 / -0.49 | both halves | 2e-04 |  |
| [[RNF2]] | -0.48 | -0.41 / -0.33 | both halves | 1e-04 |  |
| [[FAM221A]] | -0.48 | -0.45 / -0.34 | both halves | 1e-04 |  |
| [[KIF3A]] | -0.47 | -0.43 / -0.34 | both halves | 1e-04 |  |
| [[THYN1]] | -0.47 | -0.28 / -0.42 | both halves | 3e-04 |  |
| [[PAPSS1]] | -0.47 | -0.32 / -0.42 | both halves | 2e-04 |  |
| [[HERC1]] | -0.47 | -0.37 / -0.42 | both halves | 8e-05 |  |
| [[COMMD8]] | -0.47 | -0.56 / -0.38 | both halves | 6e-05 |  |
| [[CAPN5]] | -0.47 | -0.30 / -0.36 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TMEM91]] | C | MZF1's natural level strengthens TMEM91's drug response | MZF1's natural level across 47 lines (lineage-adjusted; a glimpse) | r +0.71, reverse +0.48; direction not clear | 0.013 | ⚠ tissue can mimic it; precision caveat; direction unclear |

## Where it sits

- **Module**: [[Module 017]] — Intraflagellar transport; 202 genes; this gene is in the **-** arm (projection on the module's main direction -0.471). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-10.3, 26.0); signed map (1.5, -4.4). **Vector** length 77.3, 15.4% of its response variance represented; |z| ≥ 3 in 1,171 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +5.8 | +2.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.5 | +2.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +4.4 | +0.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | +4.0 | -1.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.9 | +1.8 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +2.9 | +2.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.7 | -0.8 |
|  | [[Triamcinolone (drug)]] 5 µM |  | +1.4 | +1.9 |
| fall | [[Selinexor (drug)]] 5 µM |  | -3.6 | -8.4 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -3.3 | -9.7 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -3.3 | -18.5 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -3.1 | -12.2 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.8 | -7.8 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.6 | -3.8 |
|  | [[EX229 (drug)]] 5 µM |  | -1.5 | -4.5 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.5 | -1.8 |
|  | [[L-Thyroxine (sodium salt pentahydrate) (drug)]] 0.05 µM |  | -1.5 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | myeloid zinc finger 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.43 — chr19:58,561,931-58,573,575 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ZSCAN6, MZF1B, MZF-1, Zfp98; previously ZNF42 |
| Gene groups (HGNC) | Zinc fingers C2H2-type; SCAN domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [P28698](https://www.uniprot.org/uniprotkb/P28698) (Myeloid zinc finger 1):

> Binds to target promoter DNA and functions as a transcription regulator. Regulates transcription from the PADI1 and CDH2 promoter. May be one regulator of transcriptional events during hemopoietic development.

**Summary**, from NCBI Gene [7593](https://www.ncbi.nlm.nih.gov/gene/7593):

> Enables DNA-binding transcription factor activity, RNA polymerase II-specific; RNA polymerase II cis-regulatory region sequence-specific DNA binding activity; and protein homodimerization activity. Involved in negative regulation of transcription by RNA polymerase II and positive regulation of transcription by RNA polymerase II. Located in nucleoplasm. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:13108](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13108) · Entrez [7593](https://www.ncbi.nlm.nih.gov/gene/7593) · UniProt [P28698](https://www.uniprot.org/uniprotkb/P28698) · Ensembl [ENSG00000099326](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000099326)

## Data

Gene col 1793: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1793); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1793, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1793]; `tensor/DDL_lfc|DDL_z.npy` [1793]; `embed/gene_vectors.npy` [1793]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1793 or target_col == 1793). Every well: [[MZF1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MZF1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
