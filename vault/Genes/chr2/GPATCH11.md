---
symbol: "GPATCH11"
type: "gene"
col: 7595
ensembl_id: "ENSG00000152133"
name: "G-patch domain containing 11"
location: "2p22.2"
module: 17
arm: "+"
pooled_cpm: 23.67
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 3
n_dd_up_clean: 8
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/017"]
generated_by: "tahoemap"
---

# GPATCH11

*G-patch domain containing 11* — 2p22.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (7 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 4.17× (z +20.2, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (none with an alert); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.784× (z -4.8, q 8e-04, down in 25 of 48 measured lines).
> Its strongest partners by |cos| (96 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 7 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ISCA2]] (+0.76, fdr 9e-06), [[INIP]] (+0.75, fdr 9e-06), [[RFC1]] (+0.73, fdr 1e-05); moves opposite to [[CCNT2-AS1]] (-0.70, fdr 4e-05), [[EPM2A]] (-0.70, fdr 2e-05), [[STARD4-AS1]] (-0.68, fdr 1e-04).
> It sits in the **+** arm of [[Module 017]] (Intraflagellar transport).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[ZNF420]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 7 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7595.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **4.17×** | +20.2 | 0e+00 | 48/48 (LoVo, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **4.11×** | +20.0 | 0e+00 | 48/48 (A498, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **4.00×** | +19.6 | 0e+00 | 48/48 (A498, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.19×** | +11.1 | 2e-26 | 41/48 (A498, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **1.56×** | +8.9 | 6e-17 | 31/47 (LS 180, A-427, …) | all doses, stronger at high dose | composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **1.87×** | +8.9 | 6e-17 | 39/47 (A498, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **1.79×** | +7.9 | 2e-13 | 33/48 (SW480, LS 180, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.70×** | +7.2 | 3e-11 | 33/46 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Brivudine (drug)]] 5 µM |  | **2.35×** | +6.3 | 2e-08 | 39/48 (AsPC-1, A498, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.41×** | +4.9 | 7e-05 | 23/47 (LS 180, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~64% of this change | **1.34×** | +4.1 | 0.002 | 24/45 (SW 900, AsPC-1, …) | inconsistent across doses | low cells (technical?) |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.72×** | +4.0 | 0.003 | 21/46 (RKO, NCI-H2347, …) | inconsistent across doses | noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.67×** | +3.8 | 0.006 | 17/48 (LS 180, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.31×** | +3.7 | 0.010 | 20/48 (SW480, A-427, …) | all doses, stronger at high dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.28×** | +3.5 | 0.015 | 16/48 (NCI-H23, SW1417, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | 1.17× | +3.2 | 0.049 | 14/48 (LOX-IMVI, A498, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 7595.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.784×** | -4.8 | 8e-04 | 25/48 (A498, Hs 766T, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.759×** | -3.9 | 0.030 | 20/48 (A-172, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.763×** | -3.7 | 0.049 | 18/47 (HEC-1-A, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | 0.785× | -3.1 | 0.20 | 16/38 (A-427, A498, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Ivermectin (drug)]] 5 µM |  | 0.799× | -3.1 | 0.20 | 7/48 (A498, HS-578T, …) | rises with dose | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.36 per unit of S-phase module lfc, +0.27 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7595. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 32.4 | 4 (1 ⚠) | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 4.54× (z +11.3) | [[Dinaciclib (drug)]] 0.05 µM 0.207× (z -10.9) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 39.1 | 4 | 1 | [[Panobinostat (drug)]] 0.5 µM 3.64× (z +13.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.382× (z -14.2) |
| [[A549 (line)]] | wt | 20.6 | 4 (1 ⚠) | 1 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 6.91× (z +11.4) | [[Dinaciclib (drug)]] 5 µM 0.204× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SW480 (line)]] | alt | 35.0 | 5 (2 ⚠) | 0 | [[Belinostat (drug)]] 5 µM 3.35× (z +12.1) | — |
| [[A-172 (line)]] | wt | 24.1 | 3 | 1 | [[Belinostat (drug)]] 5 µM 4.75× (z +11.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.404× (z -9.2) |
| [[KATO III (line)]] | alt | 22.4 | 4 (1 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 4.83× (z +9.7) | — |
| [[LS 180 (line)]] | wt | 17.4 | 4 (1 ⚠) | 0 | [[Belinostat (drug)]] 5 µM 7.01× (z +12.6) | — |
| [[NCI-H460 (line)]] | wt | 28.4 | 3 | 1 | [[Panobinostat (drug)]] 0.5 µM 4.09× (z +12.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.436× (z -10.0) |
| [[PANC-1 (line)]] | alt | 26.2 | 4 (1 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 4.07× (z +13.4) | — |
| [[AsPC-1 (line)]] | alt | 16.2 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 6.65× (z +11.6) | — |
| [[CFPAC-1 (line)]] | alt | 17.8 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 5.23× (z +12.0) | — |
| [[HEC-1-A (line)]] | alt | 22.6 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 4.54× (z +11.6) | — |
| [[HOP62 (line)]] | alt | 21.8 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 5.12× (z +12.2) | — |
| [[HS-578T (line)]] | alt | 24.7 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.80× (z +9.8) | — |
| [[J82 (line)]] | alt | 19.0 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 4.12× (z +9.4) | — |
| [[LoVo (line)]] | wt | 10.6 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 10.1× (z +13.5) | — |
| [[LOX-IMVI (line)]] | wt | 18.7 | 3 | 0 | [[Belinostat (drug)]] 5 µM 5.58× (z +10.8) | — |
| [[MIA PaCa-2 (line)]] | alt | 14.9 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 8.00× (z +11.1) | — |
| [[NCI-H1573 (line)]] | alt | 13.2 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 6.57× (z +10.7) | — |
| [[NCI-H2030 (line)]] | alt | 26.7 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 4.48× (z +11.6) | — |
| [[NCI-H23 (line)]] | alt | 30.9 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 5.84× (z +12.3) | — |
| [[NCI-H2347 (line)]] | alt | 22.2 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 4.21× (z +12.8) | — |
| [[Panc 03.27 (line)]] | alt | 17.7 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 5.57× (z +10.5) | — |
| [[SNU-423 (line)]] | alt | 16.7 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 4.89× (z +9.5) | — |
| [[SW1417 (line)]] | alt | 30.3 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.54× (z +10.1) | — |
| [[RKO (line)]] | wt | 32.7 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.66× (z +9.2) | — |
| [[HCT15 (line)]] | alt | 31.0 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 4.84× (z +8.9) | — |
| [[Hs 766T (line)]] | wt | 24.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.303× (z -10.7) |
| [[NCI-H1792 (line)]] | alt | 23.0 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 4.14× (z +9.1) | — |
| [[SK-MEL-2 (line)]] | alt | 19.0 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.325× (z -8.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW 1271 (line)]] | alt | 45.4 | 0 | 1 | — | [[Auranofin (drug)]] 0.05 µM 0.0503× (z -9.7) |
| [[AN3 CA (line)]] | alt | 28.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 22.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 26.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 12.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 15.7 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 19.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 21.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 23.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 35.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 32.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 30.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 21.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 32.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 35.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 15.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7595), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*70 of its nearest partners move with it, 4 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ISCA2]] | +0.76 | +0.57 / +0.64 | both halves | 9e-06 |  |
| [[INIP]] | +0.75 | +0.57 / +0.73 | both halves | 9e-06 |  |
| [[RFC1]] | +0.73 | +0.64 / +0.54 | both halves | 1e-05 |  |
| [[PARP2]] | +0.72 | +0.67 / +0.61 | both halves | 7e-06 |  |
| [[HPF1]] | +0.72 | +0.53 / +0.72 | both halves | 1e-05 |  |
| [[ASB8]] | +0.70 | +0.72 / +0.68 | both halves | 7e-06 |  |
| [[KBTBD6]] | +0.70 | +0.57 / +0.71 | both halves | 9e-06 |  |
| [[MPHOSPH10]] | +0.70 | +0.60 / +0.68 | both halves | 7e-06 |  |
| [[COMMD2]] | +0.70 | +0.49 / +0.57 | both halves | 1e-05 |  |
| [[CINP]] | +0.69 | +0.71 / +0.55 | both halves | 1e-05 |  |
| [[RP9]] | +0.68 | +0.62 / +0.73 | both halves | 7e-06 |  |
| [[RBMX2]] | +0.68 | +0.66 / +0.67 | both halves | 7e-06 |  |

## Genes that move opposite

*30 of its nearest partners move opposite, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CCNT2-AS1]] | -0.70 | -0.41 / -0.50 | both halves | 4e-05 |  |
| [[EPM2A]] | -0.70 | -0.48 / -0.47 | both halves | 2e-05 |  |
| [[STARD4-AS1]] | -0.68 | -0.36 / -0.50 | both halves | 1e-04 |  |
| [[C2orf88]] | -0.67 | -0.27 / -0.38 | both halves | 3e-04 |  |
| [[ATP11C]] | -0.67 | -0.54 / -0.59 | both halves | 1e-05 |  |
| [[BHLHE40-AS1]] | -0.66 | -0.33 / -0.58 | both halves | 1e-04 |  |
| [[SECISBP2]] | -0.64 | -0.42 / -0.47 | both halves | 4e-05 |  |
| [[CCDC200]] | -0.64 | -0.40 / -0.55 | both halves | 5e-05 |  |
| [[CRPPA]] | -0.64 | -0.33 / -0.47 | both halves | 1e-04 |  |
| [[RCC2]] | -0.64 | -0.51 / -0.45 | both halves | 3e-05 |  |
| [[PRRC2B]] | -0.63 | -0.43 / -0.47 | both halves | 3e-05 |  |
| [[SIAH2-AS1]] | -0.63 | -0.32 / -0.39 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF420]] | B | ZNF420 activity raises GPATCH11's level | lines that do not express ZNF420 (7) vs lines expressing it (43) | 1.39× lower at baseline in the lines without ZNF420 | 0.047 | ⚠ within organs, on part of the lines; also absent: ZNF571, ZNF850, ZNF540 |
| [[RASSF4]] | B | RASSF4 activity weakens GPATCH11's drug response | lines that do not express RASSF4 (11) vs lines expressing it (37) | the lines without RASSF4 respond 1.19× as strongly (z diff -0.95); strongest at Homoharringtonine 5 µM: 2.18x vs 1.33x (z diff -3.6) | 0.093 | ⚠ within organs, on part of the lines; also absent: CTSS, SLC15A3, MX2; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[ZNF567]] | B | ZNF567 activity raises GPATCH11's level | lines that do not express ZNF567 (5) vs lines expressing it (45) | 1.37× lower at baseline in the lines without ZNF567 | 0.099 | ⚠ within organs, on part of the lines; also absent: ZNF571, ZNF529, ZFP14 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 017]] — Intraflagellar transport; 202 genes; this gene is in the **+** arm (projection on the module's main direction 0.731). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-28.3, -1.8); signed map (-19.9, -10.6). **Vector** length 103, 26.6% of its response variance represented; |z| ≥ 3 in 888 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Assembly of the 9+0 primary cilium* (reactome, mean cos +0.50 to 11); *Intraflagellar transport* (reactome, mean cos +0.53 to 6); *Cilium Assembly* (reactome, mean cos +0.50 to 11).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM |  | +4.7 | +19.6 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +4.1 | +20.0 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +4.1 | +8.9 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +3.7 | +11.1 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.2 | +6.3 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.5 | +2.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.1 | +2.7 |
|  | [[Ponatinib (drug)]] 0.05 µM |  | +1.7 | +1.5 |
|  | [[Belinostat (drug)]] 0.05 µM |  | +1.7 | +2.4 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -11.4 | -4.8 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -7.8 | -3.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -7.8 | -3.1 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -7.2 | -2.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | -7.1 | -0.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -5.6 | -1.1 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.8 | -0.8 |
|  | [[Demeclocycline (drug)]] 5 µM |  | -1.6 | -2.6 |
|  | [[Cepharanthine (drug)]] 5 µM |  | -1.5 | -0.6 |
|  | [[Thymol (drug)]] 0.5 µM |  | -1.5 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | G-patch domain containing 11 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p22.2 — chr2:37,084,518-37,099,244 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ38348, CENPY, CENP-Y; previously CCDC75 |
| Gene groups (HGNC) | G-patch domain containing |
| Matched by | ensembl_id |

UniProt [Q8N954](https://www.uniprot.org/uniprotkb/Q8N954) carries no function annotation.

**Summary**, from NCBI Gene [253635](https://www.ncbi.nlm.nih.gov/gene/253635):

> Predicted to enable nucleic acid binding activity. Located in kinetochore and nucleoplasm. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:26768](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26768) · Entrez [253635](https://www.ncbi.nlm.nih.gov/gene/253635) · UniProt [Q8N954](https://www.uniprot.org/uniprotkb/Q8N954) · Ensembl [ENSG00000152133](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000152133)

## Data

Gene col 7595: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7595); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7595, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7595]; `tensor/DDL_lfc|DDL_z.npy` [7595]; `embed/gene_vectors.npy` [7595]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7595 or target_col == 7595). Every well: [[GPATCH11 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GPATCH11.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
