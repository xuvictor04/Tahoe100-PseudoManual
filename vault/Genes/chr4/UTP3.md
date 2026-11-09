---
symbol: "UTP3"
type: "gene"
col: 5324
ensembl_id: "ENSG00000132467"
name: "UTP3 small subunit processome component"
location: "4q13.3"
module: 11
arm: "+"
pooled_cpm: 19.41
n_lines_expressing: 50
n_dd_up: 22
n_dd_down: 1
n_dd_up_clean: 11
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/011"]
generated_by: "tahoemap"
---

# UTP3

*UTP3 small subunit processome component* — 4q13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (11 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.36× (z +20.0, q 0e+00, up in 46 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[Anethole trithione (drug)]] 5 µM: 0.768× (z -4.4, q 0.008, down in 25 of 48 measured lines) ⚠ cell-cycle shift, explains ~21% of this change.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 1 line (LoVo 0.217×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Lidocaine (hydrochloride) (drug)]] 0.05 µM in 1 line (H4 0.103×); [[venetoclax (drug)]] 5 µM in 1 line (A-427 0.0671×); [[Glycyrrhizic acid (drug)]] 0.5 µM in 1 line (HepG2/C3A 0.0950×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF830]] (+0.81, fdr 7e-06), [[MRM2]] (+0.80, fdr 7e-06), [[SURF6]] (+0.79, fdr 7e-06); moves opposite to [[RPA1]] (-0.68, fdr 7e-06), [[RTN3]] (-0.67, fdr 1e-05), [[GET1]] (-0.66, fdr 7e-06).
> It sits in the **+** arm of [[Module 011]] (Mitochondrial translation elongation).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 11 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5324.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **3.36×** | +20.0 | 0e+00 | 46/47 (PANC-1, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift; position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **5.42×** | +19.9 | 0e+00 | 47/47 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **3.97×** | +16.9 | 0e+00 | 47/47 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **3.97×** | +16.9 | 0e+00 | 47/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.90×** | +10.5 | 8e-24 | 45/48 (NCI-H1573, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~11% here); position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **4.64×** | +9.8 | 1e-20 | 43/48 (SW480, A-427, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~11% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **2.15×** | +9.4 | 5e-19 | 37/48 (NCI-H460, MIA PaCa-2, …) | all doses, stronger at high dose | position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.63×** | +7.7 | 1e-12 | 36/48 (CFPAC-1, HOP62, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **3.21×** | +7.5 | 6e-12 | 34/45 (SW480, KATO III, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.80×** | +6.9 | 2e-10 | 37/44 (NCI-H460, A498, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.66×** | +6.2 | 4e-08 | 36/47 (HEC-1-A, SW480, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~64% of this change | **1.44×** | +4.4 | 5e-04 | 26/47 (NCI-H2347, AsPC-1, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~58% of this change | **1.43×** | +4.4 | 5e-04 | 22/48 (NCI-H1792, PANC-1, …) | two highest doses |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~62% of this change | **1.46×** | +4.2 | 1e-03 | 19/35 (HOP62, SK-MEL-2, …) | inconsistent across doses | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~51% of this change | **1.38×** | +3.9 | 0.003 | 23/45 (CFPAC-1, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Selinexor (drug)]] 5 µM |  | **1.23×** | +3.3 | 0.026 | 15/48 (NCI-H1573, SNU-423, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5324.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 1 line (LoVo 0.217×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Lidocaine (hydrochloride) (drug)]] 0.05 µM in 1 line (H4 0.103×); [[venetoclax (drug)]] 5 µM in 1 line (A-427 0.0671×); [[Glycyrrhizic acid (drug)]] 0.5 µM in 1 line (HepG2/C3A 0.0950×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **0.768×** | -4.4 | 0.008 | 25/48 (SW1417, A498, …) | all doses, stronger at high dose |  |
| [[Folic acid (drug)]] 5 µM |  | 0.811× | -3.5 | 0.15 | 17/48 (CHP-212, PANC-1, …) | top dose only |  |
| [[Verteporfin (drug)]] 5 µM |  | 0.755× | -3.3 | 0.16 | 18/47 (PANC-1, NCI-H460, …) | top dose only |  |
| [[Anethole trithione (drug)]] 0.5 µM |  | 0.777× | -3.1 | 0.26 | 12/48 (Hs 766T, COLO 205, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.33 per unit of S-phase module lfc, +0.24 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5324. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 16.9 | 6 | 0 | [[Harringtonine (drug)]] 5 µM 6.79× (z +12.8) | — |
| [[HEC-1-A (line)]] | alt | 24.7 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.98× (z +13.8) | — |
| [[LoVo (line)]] | wt | 21.8 | 4 | 1 (1 ⚠) | [[Harringtonine (drug)]] 5 µM 4.65× (z +10.5) | [[Dinaciclib (drug)]] 5 µM 0.217× (z -10.4) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[MIA PaCa-2 (line)]] | alt | 14.7 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.89× (z +12.1) | — |
| [[NCI-H1573 (line)]] | alt | 26.6 | 5 | 0 | [[Harringtonine (drug)]] 5 µM 7.00× (z +13.7) | — |
| [[PANC-1 (line)]] | alt | 17.7 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.61× (z +14.4) | — |
| [[A-172 (line)]] | wt | 10.9 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.37× (z +11.3) | — |
| [[A498 (line)]] | wt | 24.3 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.56× (z +13.8) | — |
| [[A549 (line)]] | wt | 16.6 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.81× (z +13.9) | — |
| [[AsPC-1 (line)]] | alt | 11.9 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.99× (z +12.3) | — |
| [[CFPAC-1 (line)]] | alt | 16.3 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.63× (z +11.6) | — |
| [[LS 180 (line)]] | wt | 20.2 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.11× (z +13.5) | — |
| [[NCI-H1792 (line)]] | alt | 12.5 | 4 | 0 | [[Harringtonine (drug)]] 5 µM 9.75× (z +11.5) | — |
| [[NCI-H2347 (line)]] | alt | 18.8 | 4 | 0 | [[Harringtonine (drug)]] 5 µM 4.76× (z +10.5) | — |
| [[SK-MEL-2 (line)]] | alt | 28.4 | 4 | 0 | [[Harringtonine (drug)]] 5 µM 7.29× (z +11.6) | — |
| [[SW 900 (line)]] | alt | 17.3 | 4 | 0 | [[Harringtonine (drug)]] 5 µM 7.77× (z +11.5) | — |
| [[A-427 (line)]] | wt | 25.9 | 2 | 1 | [[Harringtonine (drug)]] 5 µM 4.07× (z +9.5) | [[venetoclax (drug)]] 5 µM 0.0671× (z -10.0) |
| [[HOP62 (line)]] | alt | 13.8 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.27× (z +12.7) | — |
| [[HS-578T (line)]] | alt | 12.3 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.01× (z +10.7) | — |
| [[HT-29 (line)]] | alt | 22.9 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.78× (z +11.9) | — |
| [[KATO III (line)]] | alt | 22.2 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.98× (z +9.8) | — |
| [[LOX-IMVI (line)]] | wt | 12.9 | 3 | 0 | [[Harringtonine (drug)]] 0.5 µM 6.30× (z +9.6) | — |
| [[SNU-423 (line)]] | alt | 16.6 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.69× (z +12.4) | — |
| [[SW480 (line)]] | alt | 21.6 | 3 | 0 | [[Harringtonine (drug)]] 0.5 µM 4.60× (z +12.3) | — |
| [[HCT15 (line)]] | alt | 24.8 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.74× (z +9.5) | — |
| [[NCI-H2030 (line)]] | alt | 18.6 | 1 | 1 (1 ⚠) | [[Harringtonine (drug)]] 5 µM 5.56× (z +10.5) | [[Dinaciclib (drug)]] 0.5 µM 0.242× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[NCI-H23 (line)]] | alt | 26.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.79× (z +11.7) | — |
| [[RPMI-7951 (line)]] | alt | 24.3 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.34× (z +9.2) | — |
| [[C32 (line)]] | wt | 13.0 | 1 | 0 | [[Harringtonine (drug)]] 0.5 µM 6.33× (z +8.8) | — |
| [[COLO 205 (line)]] | alt | 18.8 | 1 | 0 | [[Harringtonine (drug)]] 5 µM 5.97× (z +8.8) | — |
| [[H4 (line)]] | wt | 23.2 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.103× (z -10.3) |
| [[HepG2_C3A (line)]] | wt | 11.4 | 0 | 1 | — | [[Glycyrrhizic acid (drug)]] 0.5 µM 0.0950× (z -8.9) |
| [[Hs 766T (line)]] | wt | 13.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.83× (z +8.8) | — |
| [[hTERT-HPNE (line)]] | wt | 18.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.31× (z +8.6) | — |
| [[J82 (line)]] | alt | 19.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.68× (z +8.7) | — |
| [[RKO (line)]] | wt | 34.7 | 1 | 0 | [[Harringtonine (drug)]] 0.5 µM 4.10× (z +9.0) | — |
| [[SW1417 (line)]] | alt | 21.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.46× (z +8.8) | — |
| [[SW48 (line)]] | wt | 19.4 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.116× (z -8.5) ⚠ cell-cycle shift, explains ~44% of this change |
| [[AN3 CA (line)]] | alt | 19.9 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 21.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 25.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 28.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 22.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 25.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5324), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF830]] | +0.81 | +0.86 / +0.68 | both halves | 7e-06 |  |
| [[MRM2]] | +0.80 | +0.84 / +0.76 | both halves | 7e-06 | pathway: rRNA processing; STRING 435 |
| [[SURF6]] | +0.79 | +0.84 / +0.83 | both halves | 7e-06 | STRING 874 |
| [[FAM200A]] | +0.79 | +0.82 / +0.68 | both halves | 7e-06 |  |
| [[ZNF75A]] | +0.79 | +0.80 / +0.76 | both halves | 7e-06 |  |
| [[EID2]] | +0.77 | +0.82 / +0.77 | both halves | 7e-06 |  |
| [[RPP38]] | +0.76 | +0.80 / +0.66 | both halves | 7e-06 | pathway: Major pathway of rRNA processing in the nucleolus and cytosol; STRING 853 |
| [[RPL7L1]] | +0.76 | +0.82 / +0.69 | both halves | 7e-06 | STRING 443 |
| [[NAIF1]] | +0.76 | +0.77 / +0.68 | both halves | 7e-06 |  |
| [[FBXO38]] | +0.75 | +0.78 / +0.62 | both halves | 7e-06 |  |
| [[THUMPD3]] | +0.75 | +0.76 / +0.71 | both halves | 7e-06 |  |
| [[ZNF629]] | +0.75 | +0.74 / +0.71 | both halves | 7e-06 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RPA1]] | -0.68 | -0.67 / -0.63 | both halves | 7e-06 |  |
| [[RTN3]] | -0.67 | -0.63 / -0.57 | both halves | 1e-05 |  |
| [[GET1]] | -0.66 | -0.66 / -0.59 | both halves | 7e-06 |  |
| [[NAP1L4]] | -0.65 | -0.72 / -0.63 | both halves | 7e-06 |  |
| [[STRN]] | -0.64 | -0.79 / -0.39 | both halves | 6e-05 |  |
| [[RCN2]] | -0.64 | -0.54 / -0.60 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers UTP3's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.8% of all compounds | 0.028 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[MAGEA4]] | B | MAGEA4 activity raises UTP3's level | lines that do not express MAGEA4 (41) vs lines expressing it (9) | 1.22× lower at baseline in the lines without MAGEA4 | 0.054 | ⚠ within organs, on part of the lines; co-absent genes; co-occurs with TP53; also absent: CGA, CALCA, GCG |
| [[FJX1]] | B | FJX1 activity raises UTP3's level | lines that do not express FJX1 (11) vs lines expressing it (39) | 1.15× lower at baseline in the lines without FJX1 | 0.079 | ⚠ within organs, on part of the lines; also absent: DYNC2H1, GIHCG, HDGFL3 |
| [[ZC3H12C]] | B | ZC3H12C activity raises UTP3's level | lines that do not express ZC3H12C (7) vs lines expressing it (43) | 1.14× lower at baseline in the lines without ZC3H12C | 0.080 | ⚠ within organs, on part of the lines; also absent: TMOD2, KLF12, DPF1 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 011]] — Mitochondrial translation elongation; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.851). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-37.1, 6.2); signed map (-0.2, -20.8). **Vector** length 102, 27.0% of its response variance represented; |z| ≥ 3 in 897 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +9.5 | +16.9 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +9.1 | +16.9 |
|  | [[Harringtonine (drug)]] 5 µM |  | +7.6 | +19.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +7.1 | +9.4 |
|  | [[TAK-901 (drug)]] 5 µM |  | +6.6 | +9.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +5.1 | +7.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | +5.0 | +7.5 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +4.2 | +2.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.4 | +6.2 |
| fall | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -4.7 | +2.7 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -4.4 | -0.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | -4.2 | +0.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | -4.1 | +1.8 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~64% of this change | -4.1 | +4.4 |
|  | [[Flumatinib (mesylate) (drug)]] 5 µM |  | -1.8 | -0.8 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.7 | -1.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -1.7 | -1.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | -1.5 | -1.6 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.5 | +0.7 |

## What is on record

|  |  |
|---|---|
| Name | UTP3 small subunit processome component |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q13.3 — chr4:70,688,532-70,690,551 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ23256, DKFZp761F222, SAS10, CRLZ1 |
| Gene groups (HGNC) | SSU processome |
| Reactome | 5 pathways, smallest: rRNA modification in the nucleus and cytosol; Major pathway of rRNA processing in the nucleolus and cytosol; rRNA processing in the nucleus and cytosol |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NQZ2](https://www.uniprot.org/uniprotkb/Q9NQZ2) (Something about silencing protein 10):

> Essential for gene silencing: has a role in the structure of silenced chromatin. Plays a role in the developing brain (By similarity). Part of the small subunit (SSU) processome, first precursor of the small eukaryotic ribosomal subunit. During the assembly of the SSU processome in the nucleolus, many ribosome biogenesis factors, an RNA chaperone and ribosomal proteins associate with the nascent pre-rRNA and work in concert to generate RNA folding, modifications, rearrangements and cleavage as …

**Summary**, from NCBI Gene [57050](https://www.ncbi.nlm.nih.gov/gene/57050):

> Enables RNA binding activity. Involved in ribosomal small subunit biogenesis. Located in nucleolus. Part of small-subunit processome. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:24477](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24477) · Entrez [57050](https://www.ncbi.nlm.nih.gov/gene/57050) · UniProt [Q9NQZ2](https://www.uniprot.org/uniprotkb/Q9NQZ2) · Ensembl [ENSG00000132467](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000132467)

## Data

Gene col 5324: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5324); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5324, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5324]; `tensor/DDL_lfc|DDL_z.npy` [5324]; `embed/gene_vectors.npy` [5324]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5324 or target_col == 5324). Every well: [[UTP3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/UTP3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
