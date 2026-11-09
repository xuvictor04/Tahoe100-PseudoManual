---
symbol: "YIPF2"
type: "gene"
col: 5111
ensembl_id: "ENSG00000130733"
name: "Yip1 domain family member 2"
location: "19p13.2"
module: 40
arm: "+"
pooled_cpm: 20.28
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 23
n_dd_up_clean: 3
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 5
direction_downstream: 2
tags: ["gene", "module/040"]
generated_by: "tahoemap"
---

# YIPF2

*Yip1 domain family member 2* — 19p13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (2 with an alert ⚠); the strongest is [[Docetaxel (drug)]] 0.05 µM: 1.45× (z +4.8, q 7e-04, up in 24 of 44 measured lines) ⚠ transcription drop. The strongest without an alert is [[Vinblastine (sulfate) (drug)]] 5 µM: 1.23× (z +3.7, q 0.041, up in 15 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 23 drug-doses (10 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.448× (z -14.5, q 4e-45, down in 41 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GPR107]] (+0.84, fdr 7e-06), [[COG6]] (+0.82, fdr 7e-06), [[TMEM39A]] (+0.80, fdr 7e-06); moves opposite to [[UTP20]] (-0.65, fdr 7e-06).
> It sits in the **+** arm of [[Module 040]] (Asparagine N-linked glycosylation).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[SNHG18]] → it (grade B ⚠); 2 go from it, the strongest it → [[EIF2AK3]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 2 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5111.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.45×** | +4.8 | 7e-04 | 24/44 (A-427, LOX-IMVI, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~21% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.23×** | +3.7 | 0.041 | 15/48 (C32, PANC-1, …) | rises with dose |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.49×** | +3.7 | 0.041 | 12/44 (A498, MIA PaCa-2, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.47×** | +3.6 | 0.045 | 7/45 (NCI-H2347, RPMI-7951, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.31×** | +3.5 | 0.045 | 15/37 (SW480, HEC-1-A, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[XRK3F2 (drug)]] 0.5 µM |  | 1.41× | +3.2 | 0.12 | 9/43 (NCI-H2347, NCI-H1573, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 10 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 23 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5111.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.448×** | -14.5 | 4e-45 | 41/47 (AsPC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.402×** | -11.4 | 1e-27 | 40/47 (NCI-H2347, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.484×** | -9.4 | 7e-19 | 35/46 (A498, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.486×** | -9.4 | 1e-18 | 41/47 (NCI-H2347, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.620×** | -6.2 | 6e-08 | 29/48 (AsPC-1, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.610×** | -6.2 | 6e-08 | 28/46 (H4, RPMI-7951, …) | top dose only |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.636×** | -5.6 | 2e-06 | 25/47 (NCI-H2347, HS-578T, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.656×** | -5.5 | 3e-06 | 28/48 (NCI-H2347, A498, …) | all doses, stronger at high dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.751×** | -5.2 | 1e-05 | 23/48 (HS-578T, A498, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **0.674×** | -5.1 | 2e-05 | 25/48 (A498, HS-578T, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~63% of this change | **0.681×** | -5.0 | 3e-05 | 24/48 (A498, HS-578T, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **0.779×** | -4.5 | 3e-04 | 25/48 (NCI-H2347, HS-578T, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.710×** | -4.4 | 4e-04 | 23/47 (H4, HOP62, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.706×** | -4.2 | 0.001 | 22/45 (A-172, NCI-H460, …) | all doses, stronger at high dose | low cells (technical?); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.729×** | -4.1 | 0.002 | 22/48 (H4, HOP62, …) | two highest doses | cell-cycle shift (explains ~5% here); position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.760×** | -3.6 | 0.010 | 17/48 (BT-474, KATO III, …) | two highest doses |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 0.849× | -3.0 | 0.069 | 11/48 (A498, AsPC-1, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.44 per unit of S-phase module lfc, +0.32 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5111. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[AsPC-1 (line)]] | alt | 23.7 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.136× (z -18.8) |
| [[H4 (line)]] | wt | 30.0 | 0 | 5 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0992× (z -11.9) |
| [[NCI-H2347 (line)]] | alt | 43.3 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.283× (z -16.6) |
| [[A498 (line)]] | wt | 46.7 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.160× (z -17.7) |
| [[HS-578T (line)]] | alt | 45.6 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.304× (z -14.5) |
| [[hTERT-HPNE (line)]] | wt | 19.1 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.122× (z -10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.173× (z -8.9) |
| [[RPMI-7951 (line)]] | alt | 30.5 | 0 | 3 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0775× (z -16.1) |
| [[HOP62 (line)]] | alt | 17.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.158× (z -18.7) |
| [[BT-474 (line)]] | alt | 22.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.320× (z -9.4) |
| [[CFPAC-1 (line)]] | alt | 20.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.192× (z -16.2) |
| [[HEC-1-A (line)]] | alt | 19.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.87× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | — |
| [[J82 (line)]] | alt | 17.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.242× (z -12.7) |
| [[KATO III (line)]] | alt | 22.7 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.173× (z -11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~16% of this change |
| [[LoVo (line)]] | wt | 20.1 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.191× (z -9.9) |
| [[LOX-IMVI (line)]] | wt | 6.24 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.194× (z -9.1) |
| [[NCI-H2030 (line)]] | alt | 24.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.308× (z -10.7) |
| [[Panc 03.27 (line)]] | alt | 21.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.222× (z -13.5) |
| [[SK-MEL-2 (line)]] | alt | 15.2 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.131× (z -9.7) |
| [[SW 900 (line)]] | alt | 21.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.154× (z -10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SW1417 (line)]] | alt | 26.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.358× (z -10.7) |
| [[A-172 (line)]] | wt | 19.6 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 11.9 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 11.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 7.86 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 10.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 14.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 27.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 55.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 11.5 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 18.8 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 21.2 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 9.67 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 9.47 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 11.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 18.7 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 26.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 21.7 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 16.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5111), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GPR107]] | +0.84 | +0.85 / +0.80 | both halves | 7e-06 |  |
| [[COG6]] | +0.82 | +0.87 / +0.73 | both halves | 7e-06 |  |
| [[TMEM39A]] | +0.80 | +0.86 / +0.72 | both halves | 7e-06 |  |
| [[NPRL2]] | +0.80 | +0.83 / +0.72 | both halves | 7e-06 |  |
| [[SRP54]] | +0.79 | +0.81 / +0.75 | both halves | 7e-06 |  |
| [[ACBD3]] | +0.79 | +0.85 / +0.71 | both halves | 7e-06 |  |
| [[PRRC1]] | +0.78 | +0.82 / +0.69 | both halves | 7e-06 |  |
| [[BET1L]] | +0.78 | +0.79 / +0.73 | both halves | 7e-06 |  |
| [[EIF2AK3]] | +0.78 | +0.78 / +0.72 | both halves | 7e-06 |  |
| [[ERLEC1]] | +0.78 | +0.81 / +0.70 | both halves | 7e-06 |  |
| [[ZFPL1]] | +0.77 | +0.79 / +0.79 | both halves | 7e-06 |  |
| [[CYB561D2]] | +0.77 | +0.76 / +0.71 | both halves | 7e-06 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UTP20]] | -0.65 | -0.66 / -0.60 | both halves | 7e-06 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 2, C 3.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SNHG18]] | B | SNHG18 activity raises YIPF2's level | lines that do not express SNHG18 (29) vs lines expressing it (21) | 1.58× lower at baseline in the lines without SNHG18 | 0.020 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: SEMA5A, AMPH, LINC02930 |
| [[GALNT3]] | B | GALNT3 activity raises YIPF2's level | lines that do not express GALNT3 (30) vs lines expressing it (20) | 1.39× lower at baseline in the lines without GALNT3 | 0.091 | ⚠ within organs, on part of the lines; also absent: TMEM125, GRHL2, SKAP1 |
| [[CYB561D2]] | C | CYB561D2's natural level strengthens YIPF2's drug response | CYB561D2's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.72, reverse -0.01; direction clear | 0.006 | ⚠ tissue can mimic it; precision caveat |
| [[TMEM39A]] | C | TMEM39A's natural level strengthens YIPF2's drug response | TMEM39A's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.67, reverse +0.57; direction not clear | 0.033 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[NPRL2]] | C | NPRL2's natural level strengthens YIPF2's drug response | NPRL2's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.65, reverse +0.04; direction clear | 0.043 | ⚠ tissue can mimic it; precision caveat |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 0, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EIF2AK3]] | C | YIPF2's natural level strengthens EIF2AK3's drug response | YIPF2's natural level across 49 lines (lineage-adjusted; a glimpse) | r +0.62, reverse +0.38; direction not clear | 0.072 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| cells under [[Belzutifan (drug)]] 5 µM | C | YIPF2's natural level lowers the cells' numbers under Belzutifan 5 µM (makes them more sensitive) | YIPF2's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.59 | 0.479 over the table, 0.080 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

## Where it sits

- **Module**: [[Module 040]] — Asparagine N-linked glycosylation; 111 genes; this gene is in the **+** arm (projection on the module's main direction 0.867). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.26).
- **Nodal map** (x, y) = (11.1, -32.8); signed map (-49.0, 9.7). **Vector** length 104, 26.3% of its response variance represented; |z| ≥ 3 in 886 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +4.6 | +0.2 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~68% of this change | +3.5 | -4.0 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~63% of this change | +3.4 | -5.0 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | +3.1 | -5.1 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | +2.9 | +4.8 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +2.8 | +2.8 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.6 | +3.7 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.3 | +3.7 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +2.3 | +3.6 |
|  | [[Methylprednisolone succinate (drug)]] 0.5 µM |  | +2.0 | +2.6 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -6.4 | -9.4 |
|  | [[Harringtonine (drug)]] 5 µM |  | -5.4 | -11.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.5 | -5.5 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -3.7 | -4.1 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -3.3 | -5.6 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.8 | -4.2 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.8 | -1.1 |
|  | [[Busulfan (drug)]] 0.05 µM |  | -2.7 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | Yip1 domain family member 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.2 — chr19:10,922,185-10,928,681 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MGC3262, FinGER2, Yip5C, YIPFbeta3B |
| Gene groups (HGNC) | Yip1 domain containing |
| Matched by | ensembl_id |

UniProt [Q9BWQ6](https://www.uniprot.org/uniprotkb/Q9BWQ6) carries no function annotation.

**Summary**, from NCBI Gene [78992](https://www.ncbi.nlm.nih.gov/gene/78992):

> Predicted to enable small GTPase binding activity. Predicted to be involved in vesicle-mediated transport. Located in Golgi apparatus and transport vesicle. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:28476](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28476) · Entrez [78992](https://www.ncbi.nlm.nih.gov/gene/78992) · UniProt [Q9BWQ6](https://www.uniprot.org/uniprotkb/Q9BWQ6) · Ensembl [ENSG00000130733](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000130733)

## Data

Gene col 5111: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5111); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5111, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5111]; `tensor/DDL_lfc|DDL_z.npy` [5111]; `embed/gene_vectors.npy` [5111]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5111 or target_col == 5111). Every well: [[YIPF2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/YIPF2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
