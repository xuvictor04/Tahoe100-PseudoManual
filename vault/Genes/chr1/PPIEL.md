---
symbol: "PPIEL"
type: "gene"
col: 14383
ensembl_id: "ENSG00000243970"
name: "peptidylprolyl isomerase E like (pseudogene)"
location: "1p34.3"
module: 38
arm: "+"
pooled_cpm: 10.02
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 3
n_dd_up_clean: 8
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 5
direction_downstream: 0
tags: ["gene", "module/038"]
generated_by: "tahoemap"
---

# PPIEL

*peptidylprolyl isomerase E like (pseudogene)* — 1p34.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.69× (z +13.5, q 8e-39, up in 37 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (2 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.616× (z -4.7, q 0.001, down in 23 of 42 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Digitoxin (drug)]] 0.5 µM: 0.685× (z -3.7, q 0.045, down in 17 of 45 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 10 here, 3 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 3 lines (HT-29 0.0906×, LOX-IMVI 0.122×, HEC-1-A 0.205×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Digitoxin (drug)]] 5 µM in 2 lines (BT-474 0.0587×, NCI-H1573 0.148×; ⚠ toxic; transcription drop); [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM in 2 lines (AsPC-1 0.0622×, HepG2/C3A 0.0748×); [[Ouabain (Octahydrate) (drug)]] 0.5 µM in 2 lines (PANC-1 0.188×, LOX-IMVI 0.148×); [[Bosentan (hydrate) (drug)]] 5 µM in 1 line (HOP62 0.0630×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PPIEL-1]] (+0.93, fdr 7e-06, ⚠ same locus), [[IDI2-AS1]] (+0.88, fdr 7e-06), [[PYGM]] (+0.81, fdr 7e-06), [[TRIM72]] (+0.81, fdr 7e-06); moves opposite to [[FBXO3]] (-0.64, fdr 1e-05).
> It is in [[Module 038]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 1 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14383.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.69×** | +13.5 | 8e-39 | 37/44 (C32, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.65×** | +6.8 | 3e-09 | 30/43 (NCI-H460, SNU-423, …) | top dose only | cell-cycle shift (explains ~14% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.79×** | +5.6 | 3e-06 | 29/43 (NCI-H460, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Filgotinib (drug)]] 5 µM |  | **1.79×** | +5.6 | 3e-06 | 24/48 (LoVo, NCI-H460, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **1.62×** | +4.6 | 4e-04 | 22/45 (C32, NCI-H460, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.58×** | +4.2 | 0.002 | 8/21 (SW480, C32, …) | top dose only | cell-cycle shift (explains ~8% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.57×** | +4.2 | 0.002 | 20/44 (NCI-H460, RKO, …) | top dose only | cell-cycle shift (explains ~22% here) |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.50×** | +3.7 | 0.016 | 10/46 (Panc 03.27, A-172, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.29×** | +3.5 | 0.031 | 10/47 (RKO, NCI-H460, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 3 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14383.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 10 here, 3 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 3 lines (HT-29 0.0906×, LOX-IMVI 0.122×, HEC-1-A 0.205×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Digitoxin (drug)]] 5 µM in 2 lines (BT-474 0.0587×, NCI-H1573 0.148×; ⚠ toxic; transcription drop); [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM in 2 lines (AsPC-1 0.0622×, HepG2/C3A 0.0748×); [[Ouabain (Octahydrate) (drug)]] 0.5 µM in 2 lines (PANC-1 0.188×, LOX-IMVI 0.148×); [[Bosentan (hydrate) (drug)]] 5 µM in 1 line (HOP62 0.0630×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.616×** | -4.7 | 0.001 | 23/42 (BT-474, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~31% of this change | **0.659×** | -4.0 | 0.014 | 19/38 (PANC-1, SW 900, …) | inconsistent across doses | low cells (technical?) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.685×** | -3.7 | 0.045 | 17/45 (PANC-1, J82, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | 0.701× | -3.3 | 0.13 | 18/44 (SW480, SW48, …) | rises with dose |  |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | 0.532× | -3.2 | 0.15 | 8/39 (C32, RKO, …) | top dose only | noisy plate (z scaled) |
| [[Erlotinib (drug)]] 5 µM |  | 0.713× | -3.2 | 0.15 | 15/45 (H4, C-33 A, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | 0.728× | -3.1 | 0.17 | 20/45 (PANC-1, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~15% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.27 per unit of S-phase module lfc, -0.37 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14383. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 11.0 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.158× (z -10.4) |
| [[A-172 (line)]] | wt | 5.23 | 0 | 2 | — | [[Estrone sulfate (potassium) (drug)]] 0.05 µM 0.0877× (z -8.6) |
| [[HOP62 (line)]] | alt | 11.4 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 4.74× (z +9.9) | [[Bosentan (hydrate) (drug)]] 5 µM 0.0630× (z -12.0) |
| [[LOX-IMVI (line)]] | wt | 8.43 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.122× (z -9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.148× (z -8.8) |
| [[AsPC-1 (line)]] | alt | 7.27 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM 0.0622× (z -11.1) |
| [[BT-474 (line)]] | alt | 15.8 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0587× (z -14.0) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 10.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.30× (z +10.9) | — |
| [[CFPAC-1 (line)]] | alt | 6.84 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.05× (z +9.5) | — |
| [[HEC-1-A (line)]] | alt | 21.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.205× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HepG2_C3A (line)]] | wt | 11.9 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM 0.0748× (z -8.8) |
| [[HT-29 (line)]] | alt | 14.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0906× (z -12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H1573 (line)]] | alt | 11.0 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.148× (z -10.8) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 5.21 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.85× (z +9.9) | — |
| [[Panc 03.27 (line)]] | alt | 7.78 | 0 | 1 | — | [[Rosiglitazone (drug)]] 0.05 µM 0.0686× (z -9.4) |
| [[SK-MEL-2 (line)]] | alt | 9.55 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.51× (z +10.3) | — |
| [[SW480 (line)]] | alt | 11.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.49× (z +9.8) | — |
| [[A-427 (line)]] | wt | 8.37 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 8.59 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 10.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 9.64 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 6.79 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.28 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 11.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 6.09 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 5.87 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 9.26 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 9.30 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 18.2 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 12.7 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 9.25 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.00 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 9.74 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.64 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 11.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.10 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 9.60 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 5.89 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.42 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 9.12 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 6.62 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 17.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14383), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PPIEL-1]] | +0.93 | +0.95 / +0.87 | both halves | 7e-06 | ⚠ same locus (0.0 kb, same strand: neighbours can correlate without regulation) |
| [[IDI2-AS1]] | +0.88 | +0.88 / +0.84 | both halves | 7e-06 |  |
| [[PYGM]] | +0.81 | +0.83 / +0.76 | both halves | 7e-06 | **novel candidate** |
| [[TRIM72]] | +0.81 | +0.83 / +0.72 | both halves | 7e-06 |  |
| [[FNDC7]] | +0.79 | +0.81 / +0.69 | both halves | 7e-06 |  |
| [[PILRA]] | +0.78 | +0.83 / +0.68 | both halves | 7e-06 |  |
| [[ARL9]] | +0.78 | +0.80 / +0.68 | both halves | 7e-06 |  |
| [[PITRM1-AS1]] | +0.77 | +0.77 / +0.71 | both halves | 7e-06 |  |
| [[VWCE]] | +0.75 | +0.74 / +0.73 | both halves | 7e-06 |  |
| [[MYOCOS]] | +0.74 | +0.79 / +0.61 | both halves | 7e-06 |  |
| [[FGF18]] | +0.73 | +0.76 / +0.66 | both halves | 7e-06 |  |
| [[LINC02236]] | +0.73 | +0.75 / +0.67 | both halves | 7e-06 |  |
| [[GARIN1A]] | +0.73 | +0.77 / +0.62 | both halves | 7e-06 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FBXO3]] | -0.64 | -0.66 / -0.54 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 3, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers PPIEL's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Idarubicin, Mitoxantrone) | 60% of the class's compounds vs 2.2% of all compounds | 0.059 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[KCNQ4]] | B | KCNQ4 activity raises PPIEL's level | lines that do not express KCNQ4 (7) vs lines expressing it (43) | 1.62× lower at baseline in the lines without KCNQ4 | 0.089 | ⚠ within organs, on part of the lines; also absent: ENSG00000248993; maybe low, not absent; its own permutation p |
| [[IMPA1P1]] | B | IMPA1P1 activity raises PPIEL's level | lines that do not express IMPA1P1 (6) vs lines expressing it (44) | 1.49× lower at baseline in the lines without IMPA1P1 | 0.095 | ⚠ within organs, on part of the lines; also absent: ENSG00000229195; maybe low, not absent |
| [[NABP1]] | C | NABP1 activity raises PPIEL's level | lines that do not express NABP1 (4) vs lines expressing it (46) | 1.66× lower at baseline in the lines without NABP1 | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: PHF11, LACC1, NMI; maybe low, not absent; its own permutation p |
| [[TRIM72]] | C | TRIM72 activity raises PPIEL's level | lines that do not express TRIM72 (4) vs lines expressing it (46) | 1.77× lower at baseline in the lines without TRIM72 | 0.096 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: LINC02133, LYG1, LINC01762; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 038]]; 122 genes; every member is in the + arm (projection on the module's main direction 0.800). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.28; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (34.3, -16.1); signed map (15.9, 10.2). **Vector** length 91.8, 18.6% of its response variance represented; |z| ≥ 3 in 1,083 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +5.2 | +13.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +3.7 | +5.6 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +3.7 | +2.5 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +3.6 | +3.7 |
|  | [[Filgotinib (drug)]] 5 µM |  | +3.4 | +5.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.1 | +4.6 |
|  | [[EX229 (drug)]] 5 µM |  | +2.7 | +2.2 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.6 | +1.2 |
| fall | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -5.1 | -4.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -3.9 | -3.1 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | -3.4 | -3.2 |
|  | [[Brivudine (drug)]] 5 µM |  | -3.4 | -1.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.3 | -0.7 |
|  | [[Radotinib (drug)]] 5 µM |  | -3.3 | -2.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | -3.2 | -1.6 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | -2.9 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | peptidylprolyl isomerase E like (pseudogene) |
| Locus type | pseudogene |
| Location | 1p34.3 — chr1:39,531,838-39,558,707 (-) |
| Ensembl biotype | transcribed_unprocessed_pseudogene |
| Also known as | PPIEP1 |
| Matched by | ensembl_id |

**Summary**, from NCBI Gene [728448](https://www.ncbi.nlm.nih.gov/gene/728448):

> This transcribed pseudogene is related to PPIE (Gene ID: 10450). Expression of this pseudogene may be downregulated in non-small cell lung cancer (NSCLC). Differential DNA methylation of this locus may be associated with intellectual disability and bipolar disorder in human patients. [provided by RefSeq, Sep 2016]

**Accessions** — [HGNC:33195](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:33195) · Entrez [728448](https://www.ncbi.nlm.nih.gov/gene/728448) · Ensembl [ENSG00000243970](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000243970)

## Data

Gene col 14383: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14383); `tables/drug_effects.parquet` (16 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14383, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14383]; `tensor/DDL_lfc|DDL_z.npy` [14383]; `embed/gene_vectors.npy` [14383]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14383 or target_col == 14383). Every well: [[PPIEL — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PPIEL.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
