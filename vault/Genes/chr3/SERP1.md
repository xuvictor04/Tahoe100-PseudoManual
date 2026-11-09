---
symbol: "SERP1"
type: "gene"
col: 4218
ensembl_id: "ENSG00000120742"
name: "stress associated endoplasmic reticulum protein 1"
location: "3q25.1"
module: 49
arm: "+"
pooled_cpm: 99.36
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 0
n_dd_up_clean: 7
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 2
direction_downstream: 1
tags: ["gene", "module/049"]
generated_by: "tahoemap"
---

# SERP1

*stress associated endoplasmic reticulum protein 1* — 3q25.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (3 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 1.80× (z +9.0, q 2e-16, up in 46 of 48 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 4 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (NCI-H2347 0.417×, A498 0.468×; ⚠ cell-cycle shift, explains ~0% of this change); [[Radotinib (drug)]] 0.5 µM in 1 line (SW 1271 0.0709×); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (NCI-H2347 0.419×; ⚠ cell-cycle shift, explains ~25% of this change); [[Digitoxin (drug)]] 0.5 µM in 1 line (KATO III 0.372×); [[Tadalafil (drug)]] 5 µM in 1 line (SW 1088 0.0824×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PGM3]] (+0.78, fdr 7e-06), [[DNAJC25]] (+0.78, fdr 7e-06), [[SLC33A1]] (+0.74, fdr 7e-06).
> It is in [[Module 049]], a single-armed module (XBP1(S) activates chaperone genes).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[GALNT3]] → it (grade B ⚠); 1 goes from it, the strongest it → [[MINAR1]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 3 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4218.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **1.80×** | +9.0 | 2e-16 | 46/48 (LOX-IMVI, Panc 03.27, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.39×** | +7.1 | 4e-10 | 33/49 (J82, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.54×** | +6.6 | 8e-09 | 39/49 (C-33 A, SK-MEL-2, …) | two highest doses | cell-cycle shift (explains ~5% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.46×** | +5.6 | 3e-06 | 27/43 (LOX-IMVI, NCI-H460, …) | two highest doses | cell-cycle shift (explains ~5% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.28×** | +3.8 | 0.018 | 28/48 (PANC-1, CFPAC-1, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~12% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.28×** | +3.7 | 0.020 | 26/50 (LOX-IMVI, A-172, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.24×** | +3.4 | 0.062 | 25/48 (NCI-H1573, Panc 03.27, …) | all doses, flat |  |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.23×** | +3.2 | 0.079 | 21/47 (A498, HS-578T, …) | inconsistent across doses | low cells (technical?) |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.34×** | +3.2 | 0.079 | 25/48 (LOX-IMVI, LoVo, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Methylprednisolone succinate (drug)]] 0.5 µM |  | **1.34×** | +3.2 | 0.079 | 21/48 (LoVo, LS 180, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[Fluvoxamine (maleate) (drug)]] 5 µM |  | 1.16× | +3.2 | 0.079 | 11/48 (Panc 03.27, SW1417, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 4218.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 4 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (NCI-H2347 0.417×, A498 0.468×; ⚠ cell-cycle shift, explains ~0% of this change); [[Radotinib (drug)]] 0.5 µM in 1 line (SW 1271 0.0709×); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (NCI-H2347 0.419×; ⚠ cell-cycle shift, explains ~25% of this change); [[Digitoxin (drug)]] 0.5 µM in 1 line (KATO III 0.372×); [[Tadalafil (drug)]] 5 µM in 1 line (SW 1088 0.0824×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[PH-797804 (drug)]] 5 µM |  | 0.661× | -3.2 | 0.28 | 24/48 (NCI-H2347, A-172, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 0.05 µM |  | 0.801× | -3.2 | 0.28 | 23/47 (NCI-H2347, hTERT-HPNE, …) | inconsistent across doses |  |
| [[Lidocaine (hydrochloride) (drug)]] 5 µM |  | 0.866× | -3.1 | 0.28 | 18/48 (C-33 A, NCI-H1573, …) | rises with dose | position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | 0.817× | -3.1 | 0.28 | 21/48 (KATO III, H4, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 0.05 µM |  | 0.809× | -3.0 | 0.28 | 23/48 (CFPAC-1, HOP62, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.01 per unit of S-phase module lfc, +0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4218. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[KATO III (line)]] | alt | 232 | 0 | 3 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.366× (z -10.0) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.372× (z -9.8) |
| [[LOX-IMVI (line)]] | wt | 66.1 | 2 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 2.68× (z +9.9) | — |
| [[NCI-H1573 (line)]] | alt | 136 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.26× (z +10.4) ⚠ cell-cycle shift, explains ~25% of this change | — |
| [[NCI-H2347 (line)]] | alt | 116 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.417× (z -14.3) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H460 (line)]] | wt | 55.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.56× (z +9.4) ⚠ toxic; transcription drop | — |
| [[Panc 03.27 (line)]] | alt | 121 | 2 | 0 | [[Auranofin (drug)]] 5 µM 2.25× (z +9.8) | — |
| [[A-172 (line)]] | wt | 68.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.23× (z +9.0) ⚠ toxic; transcription drop | — |
| [[A498 (line)]] | wt | 113 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.468× (z -12.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A549 (line)]] | wt | 63.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.52× (z +8.7) ⚠ toxic; transcription drop | — |
| [[BT-474 (line)]] | alt | 100 | 1 | 0 | [[Auranofin (drug)]] 5 µM 2.38× (z +9.5) | — |
| [[C-33 A (line)]] | alt | 57.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.12× (z +9.0) ⚠ toxic; transcription drop | — |
| [[HEC-1-A (line)]] | alt | 109 | 1 | 0 | [[Auranofin (drug)]] 5 µM 2.26× (z +9.7) | — |
| [[J82 (line)]] | alt | 123 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.08× (z +11.8) | — |
| [[MIA PaCa-2 (line)]] | alt | 91.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.44× (z +10.5) | — |
| [[RKO (line)]] | wt | 98.0 | 1 | 0 | [[Auranofin (drug)]] 5 µM 2.54× (z +8.6) | — |
| [[SK-MEL-2 (line)]] | alt | 92.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.41× (z +8.9) ⚠ toxic; transcription drop | — |
| [[SNU-423 (line)]] | alt | 50.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.08× (z +8.6) | — |
| [[SW 1088 (line)]] | alt | 92.8 | 0 | 1 | — | [[Tadalafil (drug)]] 5 µM 0.0824× (z -9.4) |
| [[SW 1271 (line)]] | alt | 79.0 | 0 | 1 | — | [[Radotinib (drug)]] 0.5 µM 0.0709× (z -11.4) |
| [[SW480 (line)]] | alt | 93.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.70× (z +8.7) | — |
| [[A-427 (line)]] | wt | 114 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 60.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 101 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 43.5 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 99.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 63.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 146 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 116 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 99.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 60.1 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 79.2 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 76.9 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 144 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 157 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 85.7 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 159 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 154 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 64.8 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 56.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 80.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 82.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 95.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 61.5 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 82.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 132 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 60.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 67.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 94.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 127 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 102 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4218), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PGM3]] | +0.78 | +0.71 / +0.81 | both halves | 7e-06 | **novel candidate** |
| [[DNAJC25]] | +0.78 | +0.77 / +0.75 | both halves | 7e-06 |  |
| [[SLC33A1]] | +0.74 | +0.75 / +0.71 | both halves | 7e-06 |  |
| [[GMPPA]] | +0.74 | +0.70 / +0.76 | both halves | 7e-06 |  |
| [[DNAJB9]] | +0.74 | +0.80 / +0.69 | both halves | 7e-06 | pathway: HALLMARK_UNFOLDED_PROTEIN_RESPONSE; STRING 509 |
| [[UFM1]] | +0.74 | +0.73 / +0.67 | both halves | 7e-06 | pathway: HALLMARK_MTORC1_SIGNALING |
| [[MYDGF]] | +0.74 | +0.67 / +0.76 | both halves | 7e-06 | pathway: IRE1alpha activates chaperones |
| [[SEC24D]] | +0.74 | +0.65 / +0.76 | both halves | 7e-06 |  |
| [[SLC15A2]] | +0.73 | +0.66 / +0.71 | both halves | 7e-06 |  |
| [[PLPP5]] | +0.73 | +0.75 / +0.72 | both halves | 7e-06 |  |
| [[SEC61B]] | +0.73 | +0.71 / +0.76 | both halves | 7e-06 | same gene group; pathway: Cotranslational targeting of proteins to the endoplasmic reticulum; STRING 746 |
| [[SRP54]] | +0.73 | +0.68 / +0.76 | both halves | 7e-06 | pathway: Cotranslational targeting of proteins to the endoplasmic reticulum |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GALNT3]] | B | GALNT3 activity raises SERP1's level | lines that do not express GALNT3 (30) vs lines expressing it (20) | 1.52× lower at baseline in the lines without GALNT3 | 0.031 | ⚠ within organs, on part of the lines; also absent: TMEM125, GRHL2, SKAP1 |
| [[AGR2]] | B | AGR2 activity raises SERP1's level | lines that do not express AGR2 (32) vs lines expressing it (18) | 1.34× lower at baseline in the lines without AGR2 | 0.098 | ⚠ within organs, on part of the lines; also absent: FXYD3, SERPINB5, PRKCH-AS1 |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MINAR1]] | C | SERP1's natural level strengthens MINAR1's drug response | SERP1's natural level across 44 lines (lineage-adjusted; a glimpse) | r +0.70, reverse -0.30; direction not clear | 0.031 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others; direction unclear |

## Where it sits

- **Module**: [[Module 049]] — XBP1(S) activates chaperone genes; 93 genes; every member is in the + arm (projection on the module's main direction 0.773). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.12; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (12.9, -35.6); signed map (-51.0, 12.4). **Vector** length 122, 40.0% of its response variance represented; |z| ≥ 3 in 753 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +8.4 | +9.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.3 | +7.1 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +3.1 | +3.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.1 | +1.5 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +3.1 | +1.4 |
|  | [[Terfenadine (drug)]] 5 µM |  | +2.9 | +2.3 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.8 | +2.7 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +2.6 | +1.7 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +2.6 | +3.4 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -3.7 | -3.1 |
|  | [[Berbamine (drug)]] 0.05 µM |  | -3.4 | -1.7 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -3.2 | -1.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -3.2 | -1.4 |
|  | [[Megestrol (drug)]] 0.05 µM | ⚠ cell-cycle shift | -3.0 | -1.5 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -2.9 | -2.7 |
|  | [[Busulfan (drug)]] 0.05 µM |  | -2.9 | -1.7 |
|  | [[(R)-Verapamil (hydrochloride) (drug)]] 0.05 µM |  | -2.9 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | stress associated endoplasmic reticulum protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q25.1 — chr3:150,541,998-150,603,228 (-) |
| Ensembl biotype | protein_coding |
| Also known as | RAMP4, FLJ43424 |
| Gene groups (HGNC) | Sec61 complex subunits |
| Hallmark sets | UNFOLDED_PROTEIN_RESPONSE, MTORC1_SIGNALING |
| Reactome | 8 pathways, smallest: Insertion of tail-anchored proteins into the endoplasmic reticulum membrane; XBP1(S) activates chaperone genes; IRE1alpha activates chaperones |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y6X1](https://www.uniprot.org/uniprotkb/Q9Y6X1) (Stress-associated endoplasmic reticulum protein 1):

> Interacts with target proteins during their translocation into the lumen of the endoplasmic reticulum. Protects unfolded target proteins against degradation during ER stress. May facilitate glycosylation of target proteins after termination of ER stress. May modulate the use of N-glycosylation sites on target proteins.

**Summary**, from NCBI Gene [27230](https://www.ncbi.nlm.nih.gov/gene/27230):

> Predicted to be involved in endoplasmic reticulum unfolded protein response. Predicted to act upstream of or within several processes, including positive regulation of organ growth; positive regulation of peptide hormone secretion; and positive regulation of translation. Located in cytoplasmic microtubule. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:10759](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10759) · Entrez [27230](https://www.ncbi.nlm.nih.gov/gene/27230) · UniProt [Q9Y6X1](https://www.uniprot.org/uniprotkb/Q9Y6X1) · Ensembl [ENSG00000120742](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000120742)

## Data

Gene col 4218: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4218); `tables/drug_effects.parquet` (16 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4218, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4218]; `tensor/DDL_lfc|DDL_z.npy` [4218]; `embed/gene_vectors.npy` [4218]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4218 or target_col == 4218). Every well: [[SERP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SERP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
