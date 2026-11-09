---
symbol: "EMC4"
type: "gene"
col: 4883
ensembl_id: "ENSG00000128463"
name: "ER membrane protein complex subunit 4"
location: "15q14"
module: 72
arm: "+"
pooled_cpm: 34.46
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 1
n_dd_up_clean: 3
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/072"]
generated_by: "tahoemap"
---

# EMC4

*ER membrane protein complex subunit 4* — 15q14

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.12× (z +10.7, q 9e-24, up in 44 of 46 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 1.74× (z +5.2, q 4e-05, up in 42 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.734× (z -4.1, q 0.024, down in 32 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Topotecan (hydrochloride) (drug)]] 5 µM in 1 line (RKO 0.189×; ⚠ toxic); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (SNU-1 0.0992×; ⚠ cell-cycle shift, explains ~0% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PDZD11]] (+0.67, fdr 7e-06), [[PSMB4]] (+0.65, fdr 7e-06), [[ACTR6]] (+0.61, fdr 1e-05); moves opposite to [[CPT1B]] (-0.54, fdr 1e-04), [[HNRNPH1]] (-0.53, fdr 1e-04), [[ARGLU1]] (-0.52, fdr 2e-05).
> It is in [[Module 072]], a single-armed module (Degradation of DVL).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[SYCP2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 8 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4883.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **3.12×** | +10.7 | 9e-24 | 44/46 (NCI-H1792, A549, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **2.71×** | +9.0 | 7e-17 | 33/37 (NCI-H460, SNU-423, …) | all doses, stronger at high dose | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.74×** | +5.2 | 4e-05 | 42/47 (LOX-IMVI, SW480, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | **1.74×** | +4.8 | 2e-04 | 30/39 (A-172, A498, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.59×** | +4.2 | 0.003 | 32/46 (SK-MEL-2, HT-29, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.55×** | +4.1 | 0.004 | 34/48 (NCI-H1573, HOP62, …) | two highest doses | position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **1.51×** | +3.9 | 0.008 | 33/48 (NCI-H2030, A549, …) | two highest doses | position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.44×** | +3.5 | 0.039 | 28/47 (NCI-H1573, PANC-1, …) | two highest doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.29×** | +3.3 | 0.053 | 24/48 (NCI-H2347, NCI-H1792, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~65% of this change | **1.42×** | +3.3 | 0.058 | 26/46 (AsPC-1, PANC-1, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~78% of this change | **1.41×** | +3.3 | 0.058 | 28/48 (A549, LoVo, …) | two highest doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 4883.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Topotecan (hydrochloride) (drug)]] 5 µM in 1 line (RKO 0.189×; ⚠ toxic); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (SNU-1 0.0992×; ⚠ cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.734×** | -4.1 | 0.024 | 32/47 (H4, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Budesonide (drug)]] 5 µM |  | 0.721× | -3.1 | 0.51 | 23/48 (SW 1088, HEC-1-A, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.33 per unit of S-phase module lfc, +0.36 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4883. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 32.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.76× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[A498 (line)]] | wt | 50.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.53× (z +9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[A549 (line)]] | wt | 37.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.39× (z +11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[NCI-H1792 (line)]] | alt | 33.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.74× (z +11.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[PANC-1 (line)]] | alt | 34.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.49× (z +9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[SW480 (line)]] | alt | 30.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.75× (z +9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[CFPAC-1 (line)]] | alt | 54.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.13× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[HOP62 (line)]] | alt | 25.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.05× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[HT-29 (line)]] | alt | 36.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.80× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[KATO III (line)]] | alt | 33.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.91× (z +9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[LoVo (line)]] | wt | 42.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.60× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[LOX-IMVI (line)]] | wt | 26.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.27× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[LS 180 (line)]] | wt | 35.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.74× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[NCI-H460 (line)]] | wt | 28.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.46× (z +12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[RKO (line)]] | wt | 41.2 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.189× (z -10.6) ⚠ toxic |
| [[SK-MEL-2 (line)]] | alt | 36.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.87× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[SNU-1 (line)]] | wt | 30.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0992× (z -10.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SNU-423 (line)]] | alt | 23.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.48× (z +9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[A-427 (line)]] | wt | 27.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 33.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 25.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 23.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 27.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 21.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 31.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 31.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 36.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 43.0 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 34.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 23.7 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 33.1 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 24.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 32.9 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 33.8 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 24.4 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 41.7 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 56.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 34.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 32.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 33.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 29.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 36.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 37.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 51.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 36.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 23.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 29.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 36.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 39.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 17.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4883), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PDZD11]] | +0.67 | +0.61 / +0.63 | both halves | 7e-06 |  |
| [[PSMB4]] | +0.65 | +0.63 / +0.67 | both halves | 7e-06 |  |
| [[ACTR6]] | +0.61 | +0.55 / +0.54 | both halves | 1e-05 |  |
| [[HSBP1]] | +0.60 | +0.51 / +0.68 | both halves | 1e-05 |  |
| [[EMC3]] | +0.59 | +0.51 / +0.60 | both halves | 1e-05 | same gene group; pathway: Cotranslational targeting of proteins to the endoplasmic reticulum; STRING 999 |
| [[PFDN6]] | +0.58 | +0.51 / +0.53 | both halves | 1e-05 |  |
| [[PSENEN]] | +0.57 | +0.42 / +0.60 | both halves | 4e-05 |  |
| [[PSMB6]] | +0.57 | +0.50 / +0.68 | both halves | 1e-05 |  |
| [[BABAM1]] | +0.57 | +0.51 / +0.61 | both halves | 1e-05 |  |
| [[INVS]] | +0.56 | +0.50 / +0.48 | both halves | 2e-05 |  |
| [[PSMB3]] | +0.56 | +0.57 / +0.50 | both halves | 1e-05 |  |
| [[PRR13]] | +0.56 | +0.53 / +0.57 | both halves | 1e-05 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CPT1B]] | -0.54 | -0.51 / -0.35 | both halves | 1e-04 |  |
| [[HNRNPH1]] | -0.53 | -0.46 / -0.35 | both halves | 1e-04 |  |
| [[ARGLU1]] | -0.52 | -0.46 / -0.49 | both halves | 2e-05 |  |
| [[TRIM28]] | -0.52 | -0.41 / -0.48 | both halves | 4e-05 |  |
| [[ZNF385C]] | -0.52 | -0.49 / -0.44 | both halves | 3e-05 |  |
| [[BCL3]] | -0.49 | -0.47 / -0.37 | both halves | 8e-05 |  |
| [[CTBP1]] | -0.49 | -0.37 / -0.39 | both halves | 7e-05 |  |
| [[AGER]] | -0.49 | -0.43 / -0.30 | both halves | 2e-04 |  |
| [[HNRNPD]] | -0.48 | -0.30 / -0.44 | both halves | 2e-04 |  |
| [[DDX39A]] | -0.46 | -0.38 / -0.41 | both halves | 7e-05 |  |
| [[SF1]] | -0.46 | -0.24 / -0.55 | both halves | 4e-04 |  |
| [[LINC02026]] | -0.46 | -0.46 / -0.21 | both halves | 7e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SYCP2]] | B | SYCP2 activity raises EMC4's level | lines that do not express SYCP2 (15) vs lines expressing it (35) | 1.22× lower at baseline in the lines without SYCP2 | 0.096 | ⚠ within organs, on part of the lines; also absent: AMOT, LINC00937, DMBX1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 072]] — Degradation of DVL; 69 genes; every member is in the + arm (projection on the module's main direction 0.593). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-21.8, -47.5); signed map (-24.0, -25.4). **Vector** length 54.3, 12.3% of its response variance represented; |z| ≥ 3 in 566 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 0.5 µM |  | +4.1 | +4.1 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +4.0 | +2.8 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +3.9 | +3.5 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +3.3 | +2.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.4 | +2.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.2 | +5.2 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +1.3 | +0.6 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +1.2 | +2.2 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -3.1 | -2.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.7 | -2.4 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -2.4 | -4.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -1.5 | +0.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | -1.5 | +4.8 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -1.2 | -1.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | -1.2 | -1.5 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | -1.1 | -0.5 |

## What is on record

|  |  |
|---|---|
| Name | ER membrane protein complex subunit 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q14 — chr15:34,225,013-34,230,156 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ90746, MGC24415, PIG17; previously TMEM85 |
| Gene groups (HGNC) | ER membrane protein complex subunits |
| Reactome | 5 pathways, smallest: Dengue Virus Attachment and Entry; Cotranslational targeting of proteins to the endoplasmic reticulum; Protein localization |
| Matched by | ensembl_id |

**Function**, from UniProt [Q5J8M3](https://www.uniprot.org/uniprotkb/Q5J8M3) (ER membrane protein complex subunit 4):

> Part of the endoplasmic reticulum membrane protein complex (EMC) that enables the energy-independent insertion into endoplasmic reticulum membranes of newly synthesized membrane proteins. Preferentially accommodates proteins with transmembrane domains that are weakly hydrophobic or contain destabilizing features such as charged and aromatic residues. Involved in the cotranslational insertion of multi-pass membrane proteins in which stop-transfer membrane-anchor sequences become ER membrane …

**Summary**, from NCBI Gene [51234](https://www.ncbi.nlm.nih.gov/gene/51234):

> Contributes to membrane insertase activity. Involved in protein insertion into ER membrane by stop-transfer membrane-anchor sequence and tail-anchored membrane protein insertion into ER membrane. Located in endoplasmic reticulum membrane. Part of EMC complex. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:28032](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28032) · Entrez [51234](https://www.ncbi.nlm.nih.gov/gene/51234) · UniProt [Q5J8M3](https://www.uniprot.org/uniprotkb/Q5J8M3) · Ensembl [ENSG00000128463](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000128463)

## Data

Gene col 4883: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4883); `tables/drug_effects.parquet` (13 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4883, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4883]; `tensor/DDL_lfc|DDL_z.npy` [4883]; `embed/gene_vectors.npy` [4883]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4883 or target_col == 4883). Every well: [[EMC4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EMC4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
