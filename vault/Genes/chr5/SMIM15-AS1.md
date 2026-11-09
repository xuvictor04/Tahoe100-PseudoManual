---
symbol: "SMIM15-AS1"
type: "gene"
col: 14751
ensembl_id: "ENSG00000251279"
name: "SMIM15 antisense RNA 1"
location: "5q12.1"
module: 83
arm: "+"
pooled_cpm: 7.44
n_lines_expressing: 50
n_dd_up: 16
n_dd_down: 12
n_dd_up_clean: 12
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 4
direction_downstream: 1
tags: ["gene", "module/083"]
generated_by: "tahoemap"
---

# SMIM15-AS1

*SMIM15 antisense RNA 1* — 5q12.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.08× (z +18.1, q 0e+00, up in 41 of 42 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (8 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.498× (z -8.0, q 1e-12, down in 27 of 43 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change. The strongest without an alert is [[Belinostat (drug)]] 0.5 µM: 0.699× (z -4.1, q 0.003, down in 20 of 42 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PCBP1-AS1]] (+0.87, fdr 7e-06), [[CCT6B]] (+0.86, fdr 7e-06), [[MSH4]] (+0.85, fdr 7e-06); moves opposite to [[PAFAH1B3]] (-0.72, fdr 6e-05).
> It sits in the **+** arm of [[Module 083]].
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 1 goes from it, the strongest it → [[PCBD2]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 5 with an alert ⚠. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14751.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.08×** | +18.1 | 0e+00 | 41/42 (PANC-1, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.19×** | +12.6 | 6e-34 | 30/43 (LoVo, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.16×** | +8.8 | 4e-16 | 25/41 (LoVo, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.58×** | +7.3 | 3e-11 | 27/47 (HOP62, A-172, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.78×** | +6.3 | 3e-08 | 19/37 (CFPAC-1, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.76×** | +6.2 | 5e-08 | 19/41 (A498, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.65×** | +5.7 | 1e-06 | 19/45 (HOP62, NCI-H23, …) | top dose only |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.15× | +5.6 | 2e-06 | 8/48 (LoVo, J82, …) | inconsistent across doses |  |
| [[Filgotinib (drug)]] 5 µM |  | **1.59×** | +5.3 | 8e-06 | 18/48 (NCI-H460, A498, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.57×** | +5.0 | 4e-05 | 7/15 (HEC-1-A, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.41×** | +3.9 | 0.005 | 8/30 (NCI-H2347, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~99% of this change | **1.27×** | +3.9 | 0.006 | 15/47 (NCI-H2347, PANC-1, …) | rises with dose | low cells (technical?) |
| [[Ponatinib (drug)]] 5 µM |  | **1.35×** | +3.4 | 0.030 | 11/47 (A-172, LoVo, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.35×** | +3.3 | 0.041 | 11/43 (SW480, A498, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.33×** | +3.2 | 0.051 | 2/44 (A498, HS-578T) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.33×** | +3.1 | 0.068 | 12/46 (A-427, SNU-1, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.31×** | +3.0 | 0.078 | 10/45 (NCI-H460, LOX-IMVI, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 8 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14751.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **0.498×** | -8.0 | 1e-12 | 27/43 (PANC-1, HT-29, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **0.573×** | -6.3 | 6e-08 | 21/47 (PANC-1, NCI-H23, …) | all doses, stronger at high dose | composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.633×** | -5.2 | 3e-05 | 19/47 (SW1417, PANC-1, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **0.666×** | -4.6 | 5e-04 | 17/45 (PANC-1, NCI-H23, …) | rises with dose |  |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.484×** | -4.3 | 0.002 | 15/38 (PANC-1, RPMI-7951, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~46% of this change | **0.678×** | -4.3 | 0.002 | 17/36 (LOX-IMVI, PANC-1, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **0.689×** | -4.2 | 0.002 | 18/45 (Panc 03.27, PANC-1, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.699×** | -4.1 | 0.003 | 20/42 (SW1417, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.573×** | -3.3 | 0.057 | 13/45 (PANC-1, HEC-1-A, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[HI-TOPK-032 (drug)]] 0.05 µM |  | **0.739×** | -3.3 | 0.061 | 13/44 (A-427, SNU-423, …) | inconsistent across doses | low cells (technical?) |
| [[Radotinib (drug)]] 5 µM |  | **0.819×** | -3.2 | 0.062 | 12/47 (SW 1271, SW1417, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.762×** | -3.1 | 0.091 | 14/46 (PANC-1, SW480, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.15 per unit of S-phase module lfc, -0.44 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14751. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 11.9 | 1 | 2 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.18× (z +8.7) | [[Simotinib (drug)]] 5 µM 0.148× (z -9.8) ⚠ toxic · without an alert: [[Bosentan (hydrate) (drug)]] 5 µM 0.169× (z -9.2) |
| [[PANC-1 (line)]] | alt | 11.4 | 1 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.19× (z +10.4) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.138× (z -12.6) ⚠ cell-cycle shift, explains ~49% of this change |
| [[NCI-H1792 (line)]] | alt | 6.80 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.65× (z +8.8) | [[Pyridoxine (drug)]] 0.5 µM 0.117× (z -8.8) |
| [[NCI-H460 (line)]] | wt | 7.44 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.34× (z +9.7) | — |
| [[C-33 A (line)]] | alt | 13.3 | 0 | 1 | — | [[Arbutin (drug)]] 5 µM 0.0605× (z -10.4) |
| [[CFPAC-1 (line)]] | alt | 5.66 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.07× (z +8.5) | — |
| [[COLO 205 (line)]] | alt | 8.48 | 0 | 1 | — | [[Sacubitril_Valsartan (drug)]] 0.05 µM 0.0638× (z -8.9) |
| [[HCT15 (line)]] | alt | 6.81 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.9× (z +9.4) | — |
| [[HOP62 (line)]] | alt | 7.75 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.121× (z -10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change |
| [[HS-578T (line)]] | alt | 7.07 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.44× (z +8.8) | — |
| [[HT-29 (line)]] | alt | 6.63 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0685× (z -10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change |
| [[J82 (line)]] | alt | 6.39 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0947× (z -10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change |
| [[LoVo (line)]] | wt | 9.62 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.01× (z +13.3) | — |
| [[LOX-IMVI (line)]] | wt | 8.07 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.57× (z +12.3) | — |
| [[NCI-H2030 (line)]] | alt | 9.18 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.74× (z +11.8) | — |
| [[NCI-H23 (line)]] | alt | 8.08 | 0 | 1 | — | [[Orlistat (drug)]] 0.05 µM 0.103× (z -9.1) |
| [[Panc 03.27 (line)]] | alt | 4.40 | 0 | 1 | — | [[Glycyrrhizic acid (drug)]] 5 µM 0.0671× (z -8.9) |
| [[RKO (line)]] | wt | 10.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.10× (z +8.8) | — |
| [[SK-MEL-2 (line)]] | alt | 8.72 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.03× (z +10.7) | — |
| [[SW 900 (line)]] | alt | 6.67 | 0 | 1 | — | [[Pitavastatin (Calcium) (drug)]] 0.05 µM 0.0883× (z -8.5) |
| [[A-172 (line)]] | wt | 6.22 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 9.67 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 9.15 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 5.98 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 7.38 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.02 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 6.26 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.73 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 6.30 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.19 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 5.57 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.23 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 5.78 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 5.41 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 7.60 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 8.39 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.16 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.88 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.31 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.60 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 8.22 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.81 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 5.69 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 5.88 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 8.87 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 4.49 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 7.56 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 6.56 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14751), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PCBP1-AS1]] | +0.87 | +0.85 / +0.66 | both halves | 7e-06 | same gene group |
| [[CCT6B]] | +0.86 | +0.84 / +0.69 | both halves | 7e-06 |  |
| [[MSH4]] | +0.85 | +0.83 / +0.63 | both halves | 7e-06 |  |
| [[BAAT]] | +0.83 | +0.82 / +0.62 | both halves | 7e-06 |  |
| [[MIRLET7IHG]] | +0.80 | +0.81 / +0.63 | both halves | 7e-06 |  |
| [[UBE2D3-AS1]] | +0.80 | +0.78 / +0.56 | both halves | 1e-05 | same gene group |
| [[PPP1R3F]] | +0.80 | +0.79 / +0.55 | both halves | 1e-05 |  |
| [[GLIPR1-AS1]] | +0.80 | +0.70 / +0.63 | both halves | 7e-06 | same gene group |
| [[CPEB2-DT]] | +0.80 | +0.79 / +0.50 | both halves | 1e-05 |  |
| [[ANKDD1B]] | +0.79 | +0.77 / +0.65 | both halves | 7e-06 |  |
| [[LINC01191]] | +0.79 | +0.74 / +0.59 | both halves | 7e-06 |  |
| [[EFCAB8]] | +0.78 | +0.72 / +0.75 | both halves | 7e-06 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PAFAH1B3]] | -0.72 | -0.56 / -0.39 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 3, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers SMIM15-AS1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.6% of all compounds | 0.017 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[SLC26A4]] | B | SLC26A4 activity raises SMIM15-AS1's level | lines that do not express SLC26A4 (7) vs lines expressing it (43) | 1.26× lower at baseline in the lines without SLC26A4 | 0.030 | ⚠ within organs, on part of the lines; also absent: HES4; maybe low, not absent |
| [[CDK6-AS1]] | B | CDK6-AS1 activity raises SMIM15-AS1's level | lines that do not express CDK6-AS1 (6) vs lines expressing it (44) | 1.20× lower at baseline in the lines without CDK6-AS1 | 0.083 | ⚠ within organs, on part of the lines; also absent: PLS3, CDK6, UACA; maybe low, not absent |
| [[LINC01829]] | C | LINC01829 activity raises SMIM15-AS1's level | lines that do not express LINC01829 (3) vs lines expressing it (47) | 1.46× lower at baseline in the lines without LINC01829 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: PARP11, GNG12-AS1, LINC02763; maybe low, not absent; its own permutation p |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PCBD2]] | C | SMIM15-AS1's natural level strengthens PCBD2's drug response | SMIM15-AS1's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.66, reverse +0.13; direction not clear | 0.034 | ⚠ tissue can mimic it; precision caveat; direction unclear |

## Where it sits

- **Module**: [[Module 083]]; 53 genes; this gene is in the **+** arm (projection on the module's main direction 0.900). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.40).
- **Nodal map** (x, y) = (29.5, -12.4); signed map (17.1, 2.9). **Vector** length 83.6, 15.7% of its response variance represented; |z| ≥ 3 in 1,090 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +8.5 | +18.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +6.6 | +8.8 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +6.3 | +12.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +5.8 | +2.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.4 | +5.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.2 | +7.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.2 | +3.0 |
|  | [[Filgotinib (drug)]] 5 µM |  | +3.0 | +5.3 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.7 | +3.1 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | -5.6 | -5.2 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.7 | -1.5 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -4.6 | -2.7 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -4.5 | -4.1 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -4.0 | -2.5 |
|  | [[Brivudine (drug)]] 5 µM |  | -3.8 | -1.5 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.4 | -3.2 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | -2.0 | -3.3 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | -1.9 | -2.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.8 | -0.8 |

## What is on record

|  |  |
|---|---|
| Name | SMIM15 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 5q12.1 — chr5:61,162,070-61,232,040 (+) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:41293](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:41293) · Entrez [101928630](https://www.ncbi.nlm.nih.gov/gene/101928630) · Ensembl [ENSG00000251279](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000251279)

## Data

Gene col 14751: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14751); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14751, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14751]; `tensor/DDL_lfc|DDL_z.npy` [14751]; `embed/gene_vectors.npy` [14751]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14751 or target_col == 14751). Every well: [[SMIM15-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SMIM15-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
