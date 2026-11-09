---
symbol: "EYS"
type: "gene"
col: 11976
ensembl_id: "ENSG00000188107"
name: "EGF-like photoreceptor maintenance factor"
location: "6q12"
module: 75
arm: "+"
pooled_cpm: 8.3
n_lines_expressing: 50
n_dd_up: 18
n_dd_down: 1
n_dd_up_clean: 11
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/075"]
generated_by: "tahoemap"
---

# EYS

*EGF-like photoreceptor maintenance factor* — 6q12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (7 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.59× (z +23.6, q 0e+00, up in 42 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Digitoxin (drug)]] 0.05 µM: 0.744× (z -3.9, q 0.064, down in 12 of 46 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 1 line (COLO 205 0.134×; ⚠ toxic; transcription drop); [[Belinostat (drug)]] 0.5 µM in 1 line (HS-578T 0.153×).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RBMS3-AS3]] (+0.78, fdr 7e-06), [[LRRC4C]] (+0.76, fdr 7e-06), [[CNTN5]] (+0.76, fdr 7e-06).
> It is in [[Module 075]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[LINC00504]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 7 with an alert ⚠; shown: the 15 strongest. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11976.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.59×** | +23.6 | 0e+00 | 42/44 (NCI-H1792, PANC-1, …) | rises with dose | cell-cycle shift (explains ~1% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.43×** | +16.4 | 0e+00 | 36/44 (A-172, SNU-423, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **2.55×** | +12.2 | 6e-32 | 39/47 (NCI-H1792, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.48×** | +11.9 | 3e-30 | 25/33 (LoVo, SW480, …) | all doses, flat | cell-cycle shift (explains ~3% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.31×** | +10.5 | 7e-24 | 12/15 (PANC-1, LOX-IMVI, …) | all doses, flat | cell-cycle shift (explains ~3% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.30×** | +10.0 | 1e-21 | 18/26 (HOP62, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~3% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.93×** | +8.6 | 8e-16 | 29/42 (A-172, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.92×** | +8.2 | 2e-14 | 30/44 (NCI-H2030, HOP62, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.91×** | +8.1 | 3e-14 | 28/42 (LOX-IMVI, NCI-H460, …) | top dose only | cell-cycle shift (explains ~2% here); position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.49×** | +7.3 | 1e-11 | 27/48 (A-172, NCI-H2030, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.36×** | +5.7 | 7e-07 | 19/48 (A-172, SNU-423, …) | rises with dose | position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **1.46×** | +4.8 | 8e-05 | 20/46 (A-172, hTERT-HPNE, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.40×** | +4.4 | 4e-04 | 13/40 (A498, HOP62, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~2% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.38×** | +4.2 | 0.001 | 10/46 (SW480, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Verteporfin (drug)]] 5 µM |  | **1.36×** | +3.8 | 0.005 | 6/44 (C-33 A, A498, …) | all doses, stronger at high dose | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 1 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 11976.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 1 line (COLO 205 0.134×; ⚠ toxic; transcription drop); [[Belinostat (drug)]] 0.5 µM in 1 line (HS-578T 0.153×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.05 µM |  | **0.744×** | -3.9 | 0.064 | 12/46 (A549, NCI-H2030, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.936× | -3.1 | 0.47 | 6/48 (SNU-423, SW48, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.04 per unit of S-phase module lfc, -0.00 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11976. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 16.1 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 62.1× (z +28.8) | — |
| [[HS-578T (line)]] | alt | 8.49 | 4 | 1 | [[Homoharringtonine (drug)]] 5 µM 16.7× (z +18.2) | [[Belinostat (drug)]] 0.5 µM 0.153× (z -8.6) |
| [[A498 (line)]] | wt | 5.71 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 18.6× (z +20.7) | — |
| [[HEC-1-A (line)]] | alt | 6.98 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.89× (z +13.5) | — |
| [[hTERT-HPNE (line)]] | wt | 17.9 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 166× (z +23.0) | — |
| [[LoVo (line)]] | wt | 7.64 | 3 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.85× (z +13.5) | — |
| [[LOX-IMVI (line)]] | wt | 7.45 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.78× (z +12.6) | — |
| [[PANC-1 (line)]] | alt | 4.66 | 3 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.21× (z +13.9) | — |
| [[HOP62 (line)]] | alt | 7.16 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.83× (z +12.3) | — |
| [[NCI-H1792 (line)]] | alt | 8.18 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 11.8× (z +15.2) | — |
| [[NCI-H2030 (line)]] | alt | 10.9 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.68× (z +11.0) | — |
| [[NCI-H2347 (line)]] | alt | 6.18 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.9× (z +16.6) | — |
| [[SNU-423 (line)]] | alt | 14.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 38.0× (z +25.1) | — |
| [[SW480 (line)]] | alt | 5.57 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.05× (z +10.3) | — |
| [[C32 (line)]] | wt | 8.93 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.88× (z +8.6) | — |
| [[COLO 205 (line)]] | alt | 14.1 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.134× (z -8.9) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 8.80 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.50× (z +10.6) | — |
| [[J82 (line)]] | alt | 5.27 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.60× (z +8.6) | — |
| [[KATO III (line)]] | alt | 6.48 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.60× (z +9.3) | — |
| [[LS 180 (line)]] | wt | 7.09 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.91× (z +11.0) | — |
| [[NCI-H460 (line)]] | wt | 7.14 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.58× (z +10.6) | — |
| [[RKO (line)]] | wt | 7.36 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.88× (z +12.1) | — |
| [[A-427 (line)]] | wt | 5.75 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 6.29 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 6.96 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 6.09 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 6.60 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 6.87 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 8.04 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 10.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 6.05 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 24.4 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 6.24 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 7.98 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.89 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.65 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 5.37 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 6.66 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 9.46 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 8.29 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 8.00 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 8.20 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 5.15 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 6.55 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11976), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RBMS3-AS3]] | +0.78 | +0.82 / +0.62 | both halves | 7e-06 |  |
| [[LRRC4C]] | +0.76 | +0.70 / +0.68 | both halves | 7e-06 |  |
| [[CNTN5]] | +0.76 | +0.73 / +0.78 | both halves | 7e-06 |  |
| [[LINC01090]] | +0.75 | +0.74 / +0.56 | both halves | 1e-05 |  |
| [[LINC02755]] | +0.75 | +0.75 / +0.73 | both halves | 7e-06 |  |
| [[TPTE2P6]] | +0.75 | +0.64 / +0.63 | both halves | 7e-06 |  |
| [[GALNTL6]] | +0.75 | +0.68 / +0.69 | both halves | 7e-06 |  |
| [[GRM8]] | +0.75 | +0.74 / +0.58 | both halves | 7e-06 |  |
| [[MIR4300HG]] | +0.75 | +0.76 / +0.67 | both halves | 7e-06 |  |
| [[THSD7B]] | +0.75 | +0.71 / +0.63 | both halves | 7e-06 |  |
| [[ZNF341-AS1]] | +0.74 | +0.71 / +0.44 | both halves | 3e-05 |  |
| [[PPP1R9A-AS1]] | +0.74 | +0.68 / +0.60 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC00504]] | B | LINC00504 activity raises EYS's level | lines that do not express LINC00504 (31) vs lines expressing it (19) | 1.40× lower at baseline in the lines without LINC00504 | 0.012 | ⚠ within organs, on part of the lines; also absent: ENSG00000287598, LINC02930, ENSG00000287474 |
| [[LINC02398]] | B | LINC02398 activity raises EYS's level | lines that do not express LINC02398 (13) vs lines expressing it (37) | 1.39× lower at baseline in the lines without LINC02398 | 0.015 | ⚠ within organs, on part of the lines; also absent: ANKRD7, KCNMB2, IGSF11; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers EYS's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.6% of all compounds | 0.017 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[LY96]] | B | LY96 activity raises EYS's level | lines that do not express LY96 (18) vs lines expressing it (32) | 1.34× lower at baseline in the lines without LY96 | 0.037 | ⚠ within organs, on part of the lines; also absent: SOX5, ENSG00000287100, ENSG00000287622; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 075]]; 60 genes; every member is in the + arm (projection on the module's main direction 0.816). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (19.8, 26.8); signed map (33.8, 11.9). **Vector** length 78.9, 14.1% of its response variance represented; |z| ≥ 3 in 973 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +11.5 | +23.6 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +9.0 | +16.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +8.8 | +11.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +8.0 | +10.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +7.7 | +10.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +5.7 | +7.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.8 | +5.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.2 | +2.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.2 | +2.5 |
|  | [[Verteporfin (drug)]] 5 µM |  | +2.1 | +3.8 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -4.4 | -2.4 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -3.8 | -2.9 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.6 | -0.7 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -3.0 | -1.5 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -2.4 | -3.1 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.0 | -0.6 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.7 | -2.4 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -1.5 | -1.9 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.4 | -1.3 |
|  | [[Asciminib (drug)]] 0.05 µM |  | -1.3 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | EGF-like photoreceptor maintenance factor |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q12 — chr6:63,719,980-65,707,226 (-) |
| Ensembl biotype | protein_coding |
| Also known as | dJ1018A4.2, bA166P24.2, SPAM, bA307F22.3, dJ303F19.1, bA74E24.1; previously C6orf180, EGFL11, RP25, EGFL10, C6orf178 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q5T1H1](https://www.uniprot.org/uniprotkb/Q5T1H1) (Protein eyes shut homolog):

> Required to maintain the integrity of photoreceptor cells. Specifically required for normal morphology of the photoreceptor ciliary pocket, and might thus facilitate protein trafficking between the photoreceptor inner and outer segments via the transition zone (By similarity).

**Summary**, from NCBI Gene [346007](https://www.ncbi.nlm.nih.gov/gene/346007):

> The product of this gene contains multiple epidermal growth factor (EGF)-like and LamG domains. The protein is expressed in the photoreceptor layer of the retina, and the gene is mutated in autosomal recessive retinitis pigmentosa. Multiple transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Dec 2008]

**Accessions** — [HGNC:21555](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21555) · Entrez [346007](https://www.ncbi.nlm.nih.gov/gene/346007) · UniProt [Q5T1H1](https://www.uniprot.org/uniprotkb/Q5T1H1) · Ensembl [ENSG00000188107](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000188107)

## Data

Gene col 11976: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11976); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11976, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11976]; `tensor/DDL_lfc|DDL_z.npy` [11976]; `embed/gene_vectors.npy` [11976]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11976 or target_col == 11976). Every well: [[EYS — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EYS.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
