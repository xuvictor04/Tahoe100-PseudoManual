---
symbol: "NOL6"
type: "gene"
col: 9097
ensembl_id: "ENSG00000165271"
name: "nucleolar protein 6"
location: "9p13.3"
module: 1
arm: "+"
pooled_cpm: 10.07
n_lines_expressing: 50
n_dd_up: 28
n_dd_down: 1
n_dd_up_clean: 12
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 1
tags: ["gene", "module/001"]
generated_by: "tahoemap"
---

# NOL6

*nucleolar protein 6* — 9p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 28 drug-doses (16 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.66× (z +16.0, q 0e+00, up in 37 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[Pitavastatin (Calcium) (drug)]] 5 µM: 0.713× (z -3.8, q 0.091, down in 11 of 46 measured lines) ⚠ cell-cycle shift, explains ~27% of this change.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Imiquimod (maleate) (drug)]] 5 µM in 1 line (KATO III 0.111×); [[Topotecan (hydrochloride) (drug)]] 0.05 µM in 1 line (LS 180 0.102×); [[Cobimetinib (drug)]] 5 µM in 1 line (AsPC-1 0.0965×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[METTL1]] (+0.78, fdr 7e-06), [[WDR46]] (+0.76, fdr 7e-06), [[PNO1]] (+0.75, fdr 7e-06); moves opposite to [[HINT1]] (-0.61, fdr 7e-06), [[NPC2]] (-0.58, fdr 1e-05), [[CERT1]] (-0.57, fdr 1e-05).
> It sits in the **+** arm of [[Module 001]] (rRNA processing).
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 1 goes from it, the strongest it → [[GAR1]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 16 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 28 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 16 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9097.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.66×** | +16.0 | 0e+00 | 37/44 (A-172, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **3.55×** | +14.6 | 1e-45 | 39/43 (PANC-1, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **2.89×** | +12.0 | 6e-31 | 39/48 (SW480, A-172, …) | rises with dose | position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **4.62×** | +9.2 | 4e-18 | 40/47 (HOP62, PANC-1, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~6% here); composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **2.16×** | +8.9 | 8e-17 | 35/47 (SW480, BT-474, …) | rises with dose | position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **2.22×** | +8.8 | 9e-17 | 33/45 (NCI-H460, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~4% here); composition shift; position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **2.18×** | +8.8 | 1e-16 | 31/47 (SW480, LoVo, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **4.13×** | +8.5 | 9e-16 | 34/43 (PANC-1, RKO, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.84×** | +7.0 | 1e-10 | 33/46 (NCI-H460, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~5% here); position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.95×** | +6.5 | 5e-09 | 28/47 (NCI-H460, Hs 766T, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~73% of this change | **1.59×** | +5.1 | 2e-05 | 6/15 (NCI-H2347, LOX-IMVI, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~40% of this change | **1.58×** | +5.1 | 2e-05 | 19/36 (A-172, NCI-H1573, …) | rises with dose | position effect removed |
| [[Belumosudil (drug)]] 5 µM |  | **1.47×** | +4.3 | 9e-04 | 20/46 (NCI-H1792, MIA PaCa-2, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **1.43×** | +4.0 | 0.003 | 19/46 (LOX-IMVI, NCI-H460, …) | top dose only | position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.40×** | +3.9 | 0.004 | 15/46 (PANC-1, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.77×** | +3.4 | 0.015 | 7/44 (MIA PaCa-2, SW 900, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.33×** | +3.1 | 0.043 | 8/46 (HOP62, Hs 766T, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.30×** | +2.9 | 0.084 | 13/46 (LOX-IMVI, HEC-1-A, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 1 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9097.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Imiquimod (maleate) (drug)]] 5 µM in 1 line (KATO III 0.111×); [[Topotecan (hydrochloride) (drug)]] 0.05 µM in 1 line (LS 180 0.102×); [[Cobimetinib (drug)]] 5 µM in 1 line (AsPC-1 0.0965×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.713×** | -3.8 | 0.091 | 11/46 (RKO, CHP-212, …) | top dose only |  |
| [[Ponatinib (drug)]] 5 µM |  | 0.767× | -3.0 | 0.35 | 13/48 (KATO III, RKO, …) | rises with dose | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.56 per unit of S-phase module lfc, -0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9097. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 9.04 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.45× (z +10.4) | [[Dinaciclib (drug)]] 0.5 µM 0.124× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[H4 (line)]] | wt | 16.4 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 5.44× (z +9.0) | [[Clotrimazole (drug)]] 0.5 µM 0.0931× (z -9.0) |
| [[KATO III (line)]] | alt | 11.0 | 0 | 2 (1 ⚠) | — | [[Imiquimod (maleate) (drug)]] 5 µM 0.111× (z -10.7) |
| [[PANC-1 (line)]] | alt | 19.8 | 2 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 4.57× (z +10.6) | — |
| [[SNU-423 (line)]] | alt | 3.82 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 12.2× (z +11.3) | [[Acetazolamide (drug)]] 0.05 µM 0.0645× (z -8.6) |
| [[A-172 (line)]] | wt | 5.29 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.95× (z +11.7) | — |
| [[AN3 CA (line)]] | alt | 14.3 | 0 | 1 | — | [[Ponatinib (drug)]] 0.05 µM 0.0562× (z -8.7) |
| [[AsPC-1 (line)]] | alt | 8.84 | 0 | 1 | — | [[Cobimetinib (drug)]] 5 µM 0.0965× (z -9.7) |
| [[HOP62 (line)]] | alt | 5.63 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.06× (z +9.8) | — |
| [[J82 (line)]] | alt | 14.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.47× (z +9.5) | — |
| [[LOX-IMVI (line)]] | wt | 7.58 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 10.4× (z +9.7) | — |
| [[LS 180 (line)]] | wt | 8.33 | 0 | 1 | — | [[Topotecan (hydrochloride) (drug)]] 0.05 µM 0.102× (z -9.9) |
| [[NCI-H2347 (line)]] | alt | 5.27 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.128× (z -9.6) ⚠ transcription drop |
| [[NCI-H460 (line)]] | wt | 6.96 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.26× (z +8.6) | — |
| [[Panc 03.27 (line)]] | alt | 7.85 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.89× (z +9.7) | — |
| [[SK-MEL-2 (line)]] | alt | 17.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.22× (z +8.5) | — |
| [[A-427 (line)]] | wt | 8.15 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 32.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.68 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.16 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 9.71 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 5.37 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 5.57 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.69 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 7.17 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 6.82 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 7.95 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 10.1 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.72 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 4.61 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 4.87 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.88 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 8.47 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 16.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 9.60 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 11.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.92 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 8.21 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 10.5 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 8.36 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9097), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[METTL1]] | +0.78 | +0.82 / +0.73 | both halves | 7e-06 |  |
| [[WDR46]] | +0.76 | +0.79 / +0.67 | both halves | 7e-06 | same gene group; pathway: Major pathway of rRNA processing in the nucleolus and cytosol; STRING 999 |
| [[PNO1]] | +0.75 | +0.77 / +0.73 | both halves | 7e-06 | pathway: Major pathway of rRNA processing in the nucleolus and cytosol; STRING 980 |
| [[DPH2]] | +0.75 | +0.76 / +0.67 | both halves | 7e-06 | **novel candidate** |
| [[MYBBP1A]] | +0.74 | +0.71 / +0.74 | both halves | 7e-06 | STRING 970 |
| [[IMP4]] | +0.73 | +0.78 / +0.65 | both halves | 7e-06 | pathway: Major pathway of rRNA processing in the nucleolus and cytosol; STRING 998 |
| [[GRWD1]] | +0.72 | +0.69 / +0.77 | both halves | 7e-06 | STRING 789 |
| [[PES1]] | +0.72 | +0.76 / +0.62 | both halves | 7e-06 | pathway: Major pathway of rRNA processing in the nucleolus and cytosol; STRING 860 |
| [[TBL3]] | +0.71 | +0.70 / +0.69 | both halves | 7e-06 | pathway: Major pathway of rRNA processing in the nucleolus and cytosol; STRING 999 |
| [[NOLC1]] | +0.70 | +0.72 / +0.67 | both halves | 7e-06 | STRING 815 |
| [[PRMT5]] | +0.69 | +0.68 / +0.65 | both halves | 7e-06 |  |
| [[IPO4]] | +0.68 | +0.70 / +0.66 | both halves | 7e-06 | STRING 723 |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HINT1]] | -0.61 | -0.60 / -0.61 | both halves | 7e-06 |  |
| [[NPC2]] | -0.58 | -0.54 / -0.54 | both halves | 1e-05 | same gene group |
| [[CERT1]] | -0.57 | -0.56 / -0.56 | both halves | 1e-05 |  |
| [[NENF]] | -0.57 | -0.61 / -0.55 | both halves | 1e-05 |  |
| [[ELF2]] | -0.56 | -0.60 / -0.50 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GAR1]] | C | NOL6's natural level strengthens GAR1's drug response | NOL6's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.66, reverse -0.17; direction not clear | 0.034 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others; direction unclear |

## Where it sits

- **Module**: [[Module 001]] — rRNA processing; 298 genes; this gene is in the **+** arm (projection on the module's main direction 0.621). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-16.8, -34.0); signed map (-3.9, -44.2). **Vector** length 77.5, 14.8% of its response variance represented; |z| ≥ 3 in 1,141 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *MYC targets v2* (hallmark, mean cos +0.57 to 10).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.7 | +14.6 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +3.7 | +6.5 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +3.3 | +7.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.9 | +8.5 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.8 | +4.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.6 | +3.9 |
|  | [[Pralsetinib (drug)]] 5 µM |  | +1.8 | +2.5 |
|  | [[Budesonide (drug)]] 5 µM |  | +1.7 | +2.7 |
| fall | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change | -2.9 | +3.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.3 | -3.0 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -2.2 | -2.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.2 | +2.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.1 | +0.5 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -2.0 | -2.9 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.7 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | nucleolar protein 6 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9p13.3 — chr9:33,461,353-33,473,930 (-) |
| Ensembl biotype | protein_coding |
| Also known as | bA311H10.1, Nrap, FLJ21959, MGC14896, MGC14921, MGC20838, UTP22 |
| Gene groups (HGNC) | UTPc subcomplex; MicroRNA protein coding host genes |
| Reactome | 5 pathways, smallest: rRNA modification in the nucleus and cytosol; Major pathway of rRNA processing in the nucleolus and cytosol; rRNA processing in the nucleus and cytosol |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H6R4](https://www.uniprot.org/uniprotkb/Q9H6R4) (Nucleolar protein 6):

> Part of the small subunit (SSU) processome, first precursor of the small eukaryotic ribosomal subunit. During the assembly of the SSU processome in the nucleolus, many ribosome biogenesis factors, an RNA chaperone and ribosomal proteins associate with the nascent pre-rRNA and work in concert to generate RNA folding, modifications, rearrangements and cleavage as well as targeted degradation of pre-ribosomal RNA by the RNA exosome.

**Summary**, from NCBI Gene [65083](https://www.ncbi.nlm.nih.gov/gene/65083):

> The nucleolus is a dense subnuclear membraneless organelle that assembles around clusters of rRNA genes and functions in ribosome biogenesis. This gene encodes a nucleolar RNA-associated protein that is highly conserved between species. RNase treatment of permeabilized cells indicates that the nucleolar localization is RNA dependent. Further studies suggest that the protein is associated with ribosome biogenesis through an interaction with pre-rRNA primary transcripts. Alternative splicing has …

**Accessions** — [HGNC:19910](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19910) · Entrez [65083](https://www.ncbi.nlm.nih.gov/gene/65083) · UniProt [Q9H6R4](https://www.uniprot.org/uniprotkb/Q9H6R4) · Ensembl [ENSG00000165271](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000165271)

## Data

Gene col 9097: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9097); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9097, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9097]; `tensor/DDL_lfc|DDL_z.npy` [9097]; `embed/gene_vectors.npy` [9097]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9097 or target_col == 9097). Every well: [[NOL6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NOL6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
