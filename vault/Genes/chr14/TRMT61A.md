---
symbol: "TRMT61A"
type: "gene"
col: 9250
ensembl_id: "ENSG00000166166"
name: "tRNA methyltransferase 61A"
location: "14q32.33"
module: 1
arm: "+"
pooled_cpm: 3.09
n_lines_expressing: 50
n_dd_up: 23
n_dd_down: 1
n_dd_up_clean: 12
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/001"]
generated_by: "tahoemap"
---

# TRMT61A

*tRNA methyltransferase 61A* — 14q32.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (11 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 3.49× (z +12.2, q 1e-31, up in 3 of 4 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 2.57× (z +9.6, q 2e-19, up in 23 of 35 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Tucidinostat (drug)]] 5 µM: 0.748× (z -4.3, q 0.011, down in 10 of 44 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, none with an alert; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Pimozide (drug)]] 0.05 µM in 1 line (A-427 0.0527×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (MIA PaCa-2 0.143×); [[Neratinib (drug)]] 5 µM in 1 line (NCI-H2030 0.0638×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RRP1]] (+0.78, fdr 7e-06), [[NIP7]] (+0.77, fdr 7e-06), [[DPH2]] (+0.76, fdr 7e-06); moves opposite to [[GNAS]] (-0.64, fdr 7e-06), [[NUCB2]] (-0.64, fdr 7e-06), [[ARL6IP5]] (-0.56, fdr 3e-05).
> It sits in the **+** arm of [[Module 001]] (rRNA processing).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[ADD3]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 11 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9250.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.49×** | +12.2 | 1e-31 | 3/4 (PANC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.58×** | +9.7 | 1e-19 | 10/16 (SW480, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.57×** | +9.6 | 2e-19 | 23/35 (A498, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.54×** | +8.8 | 3e-16 | 5/7 (MIA PaCa-2, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **2.03×** | +7.2 | 8e-11 | 27/44 (A498, PANC-1, …) | two highest doses | cell-cycle shift (explains ~5% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.59×** | +6.7 | 2e-09 | 17/36 (A-172, A498, …) | all doses, flat | cell-cycle shift (explains ~13% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.83×** | +6.1 | 8e-08 | 17/45 (NCI-H2347, NCI-H460, …) | inconsistent across doses | position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **1.84×** | +6.0 | 2e-07 | 21/40 (A498, NCI-H1792, …) | two highest doses | cell-cycle shift (explains ~12% here); composition shift; position effect removed |
| [[Belumosudil (drug)]] 5 µM |  | **1.84×** | +6.0 | 2e-07 | 19/41 (NCI-H1792, C32, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.84×** | +5.9 | 2e-07 | 5/18 (KATO III, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.79×** | +5.9 | 2e-07 | 15/41 (LOX-IMVI, A498, …) | all doses, flat |  |
| [[Auranofin (drug)]] 5 µM |  | **1.64×** | +5.0 | 3e-05 | 17/43 (MIA PaCa-2, NCI-H2030, …) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.65×** | +4.9 | 5e-05 | 9/26 (NCI-H1573, Panc 03.27, …) | top dose only | cell-cycle shift (explains ~18% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.57×** | +4.6 | 2e-04 | 8/21 (BT-474, SW1417, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~15% here); position effect removed |
| [[Pralsetinib (drug)]] 5 µM |  | **2.34×** | +4.5 | 2e-04 | 2/17 (PANC-1, NCI-H2347) | top dose only | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.47×** | +3.9 | 0.004 | 11/43 (J82, SK-MEL-2, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.45×** | +3.8 | 0.005 | 8/43 (RPMI-7951, PANC-1, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.37×** | +3.0 | 0.073 | 7/42 (SNU-423, HEC-1-A, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.50×** | +2.9 | 0.086 | 2/28 (PANC-1, SK-MEL-2) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 9250.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, none with an alert; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Pimozide (drug)]] 0.05 µM in 1 line (A-427 0.0527×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (MIA PaCa-2 0.143×); [[Neratinib (drug)]] 5 µM in 1 line (NCI-H2030 0.0638×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **0.748×** | -4.3 | 0.011 | 10/44 (HOP62, PANC-1, …) | all doses, stronger at high dose |  |
| [[Methotrexate (drug)]] 0.5 µM |  | 0.709× | -3.6 | 0.10 | 11/42 (HT-29, NCI-H1792, …) | inconsistent across doses |  |
| [[Gallic acid (hydrate) (drug)]] 5 µM |  | 0.800× | -3.3 | 0.18 | 6/44 (hTERT-HPNE, C-33 A, …) | top dose only | position effect removed |
| [[Tofacitinib (drug)]] 5 µM |  | 0.807× | -3.2 | 0.19 | 10/44 (SNU-1, NCI-H1792, …) | inconsistent across doses |  |
| [[Loperamide (hydrochloride) (drug)]] 5 µM |  | 0.739× | -3.1 | 0.19 | 6/44 (AsPC-1, AN3 CA, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.23 per unit of S-phase module lfc, +0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9250. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 5.72 | 0 | 1 | — | [[Pimozide (drug)]] 0.05 µM 0.0527× (z -11.7) |
| [[LoVo (line)]] | wt | 2.28 | 0 | 1 | — | [[Ferulic acid (drug)]] 5 µM 0.0610× (z -8.9) |
| [[MIA PaCa-2 (line)]] | alt | 6.14 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.143× (z -11.1) |
| [[NCI-H2030 (line)]] | alt | 4.58 | 0 | 1 | — | [[Neratinib (drug)]] 5 µM 0.0638× (z -10.0) |
| [[SK-MEL-2 (line)]] | alt | 5.74 | 0 | 1 | — | [[Tucatinib (drug)]] 0.05 µM 0.0719× (z -8.6) |
| [[A-172 (line)]] | wt | 1.61 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 3.90 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.79 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.37 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.25 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.05 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.13 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.85 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.44 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.42 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.22 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.28 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.31 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.55 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.25 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.59 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.22 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.54 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.92 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.80 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 4.99 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.27 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.63 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.88 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.36 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.50 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.14 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.13 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.25 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.73 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.88 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.39 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.51 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 4.07 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 4.08 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.45 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 5.68 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.38 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.87 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.98 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.07 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.75 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 5.09 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.83 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 3.53 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9250), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RRP1]] | +0.78 | +0.72 / +0.77 | both halves | 7e-06 | STRING 451 |
| [[NIP7]] | +0.77 | +0.75 / +0.80 | both halves | 7e-06 | STRING 587 |
| [[DPH2]] | +0.76 | +0.79 / +0.72 | both halves | 7e-06 | STRING 424 |
| [[IFRD2]] | +0.75 | +0.71 / +0.76 | both halves | 7e-06 | STRING 571 |
| [[CLUH]] | +0.74 | +0.80 / +0.69 | both halves | 7e-06 |  |
| [[PUS1]] | +0.74 | +0.78 / +0.68 | both halves | 7e-06 | pathway: tRNA modification in the nucleus and cytosol; STRING 709 |
| [[IMP4]] | +0.73 | +0.70 / +0.76 | both halves | 7e-06 | STRING 473 |
| [[RRP9]] | +0.71 | +0.78 / +0.63 | both halves | 7e-06 | STRING 657 |
| [[METTL1]] | +0.71 | +0.79 / +0.66 | both halves | 7e-06 | same gene group; pathway: tRNA modification in the nucleus and cytosol; STRING 964 |
| [[RRS1]] | +0.71 | +0.68 / +0.71 | both halves | 7e-06 | STRING 524 |
| [[NOC4L]] | +0.70 | +0.78 / +0.62 | both halves | 7e-06 |  |
| [[FAAP100]] | +0.70 | +0.70 / +0.69 | both halves | 7e-06 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GNAS]] | -0.64 | -0.60 / -0.68 | both halves | 7e-06 |  |
| [[NUCB2]] | -0.64 | -0.60 / -0.66 | both halves | 7e-06 |  |
| [[ARL6IP5]] | -0.56 | -0.60 / -0.45 | both halves | 3e-05 |  |
| [[GGH]] | -0.56 | -0.51 / -0.54 | both halves | 1e-05 |  |
| [[G3BP2]] | -0.55 | -0.51 / -0.55 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ADD3]] | B | ADD3 activity lowers TRMT61A's level | lines that do not express ADD3 (5) vs lines expressing it (45) | 1.46× higher at baseline in the lines without ADD3 | 0.083 | ⚠ within organs, on part of the lines; also absent: LINC02842, ADD3-AS1, WWC3 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 001]] — rRNA processing; 298 genes; this gene is in the **+** arm (projection on the module's main direction 0.681). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-16.4, -38.8); signed map (-2.6, -44.6). **Vector** length 49.3, 6.15% of its response variance represented; |z| ≥ 3 in 943 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *rRNA processing* (reactome, mean cos +0.52 to 28); *rRNA processing in the nucleus and cytosol* (reactome, mean cos +0.54 to 24); *Major pathway of rRNA processing in the nucleolus and cytosol* (reactome, mean cos +0.55 to 23).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +2.8 | +9.6 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +2.8 | +7.2 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.7 | +6.0 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +2.6 | +6.1 |
|  | [[Harringtonine (drug)]] 5 µM |  | +2.3 | +6.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.2 | +5.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.8 | +5.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.7 | +2.9 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.5 | +2.3 |
| fall | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -2.0 | -1.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.5 | -2.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.5 | -4.3 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.4 | -2.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -1.3 | -2.8 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.3 | +0.1 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.3 | -2.1 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -1.3 | -2.9 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.2 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | tRNA methyltransferase 61A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q32.33 — chr14:103,529,196-103,537,073 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ40452, GCD14, Gcd14p, hTRM61; previously C14orf172 |
| Gene groups (HGNC) | 7BS N1-adenosine RNA methyltransferases; DNA/RNA methyltransferases |
| Reactome | 3 pathways, smallest: tRNA modification in the nucleus and cytosol; tRNA processing; Metabolism of RNA |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96FX7](https://www.uniprot.org/uniprotkb/Q96FX7) (tRNA):

> Catalytic subunit of tRNA (adenine-N(1)-)-methyltransferase, which catalyzes the formation of N(1)-methyladenine at position 58 (m1A58) in initiator methionyl-tRNA. Catalytic subunit of mRNA N(1)-methyltransferase complex, which mediates methylation of adenosine residues at the N(1) position of a small subset of mRNAs: N(1) methylation takes place in tRNA T-loop-like structures of mRNAs and is only present at low stoichiometries.

**Summary**, from NCBI Gene [115708](https://www.ncbi.nlm.nih.gov/gene/115708):

> Enables mRNA (adenine-N1-)-methyltransferase activity. Involved in mRNA processing. Predicted to be located in nucleoplasm. Predicted to be part of tRNA (m1A) methyltransferase complex. Predicted to be active in nucleus. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:23790](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23790) · Entrez [115708](https://www.ncbi.nlm.nih.gov/gene/115708) · UniProt [Q96FX7](https://www.uniprot.org/uniprotkb/Q96FX7) · Ensembl [ENSG00000166166](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000166166)

## Data

Gene col 9250: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9250); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9250, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9250]; `tensor/DDL_lfc|DDL_z.npy` [9250]; `embed/gene_vectors.npy` [9250]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9250 or target_col == 9250). Every well: [[TRMT61A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TRMT61A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
