---
symbol: "ABCB8"
type: "gene"
col: 12355
ensembl_id: "ENSG00000197150"
name: "ATP binding cassette subfamily B member 8"
location: "7q36.1"
module: 72
arm: "+"
pooled_cpm: 10.21
n_lines_expressing: 50
n_dd_up: 26
n_dd_down: 3
n_dd_up_clean: 13
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/072"]
generated_by: "tahoemap"
---

# ABCB8

*ATP binding cassette subfamily B member 8* — 7q36.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 26 drug-doses (13 with an alert ⚠); the strongest is [[Bortezomib (drug)]] 0.05 µM: 2.44× (z +13.9, q 2e-41, up in 38 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (1 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 0.587× (z -12.6, q 2e-33, down in 34 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Selinexor (drug)]] 5 µM in 3 lines (A498 0.342×, PANC-1 0.416×, HS-578T 0.356×); [[Homoharringtonine (drug)]] 5 µM in 1 line (A-427 0.129×; ⚠ cell-cycle shift, would explain all of this change); [[Sunitinib (drug)]] 5 µM in 1 line (SW 900 0.0744×; ⚠ toxic).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PSMB3]] (+0.67, fdr 7e-06), [[USP5]] (+0.67, fdr 7e-06), [[PSMC4]] (+0.63, fdr 7e-06); moves opposite to [[ZNF330]] (-0.57, fdr 2e-05), [[SNX2]] (-0.53, fdr 2e-05), [[RCHY1]] (-0.52, fdr 6e-05).
> It is in [[Module 072]], a single-armed module (Degradation of DVL).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[ASPH]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 14 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 26 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12355.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Bortezomib (drug)]] 0.05 µM |  | **2.44×** | +13.9 | 2e-41 | 38/46 (PANC-1, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **2.27×** | +13.6 | 1e-39 | 34/47 (PANC-1, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **2.14×** | +12.6 | 4e-34 | 36/48 (SW480, MIA PaCa-2, …) | all doses, stronger at high dose | position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **2.07×** | +12.0 | 4e-31 | 35/47 (PANC-1, HOP62, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **2.11×** | +11.9 | 2e-30 | 16/19 (LS 180, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.98×** | +11.3 | 2e-27 | 33/47 (SW480, MIA PaCa-2, …) | all doses, stronger at high dose | position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **1.85×** | +10.1 | 3e-22 | 23/32 (C32, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.49×** | +9.3 | 1e-18 | 29/46 (SW480, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~25% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **1.59×** | +7.1 | 9e-11 | 14/26 (C32, LS 180, …) | all doses, stronger at high dose | composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **1.44×** | +6.0 | 1e-07 | 23/47 (SW480, MIA PaCa-2, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.29×** | +6.0 | 1e-07 | 16/48 (MIA PaCa-2, SNU-423, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **1.40×** | +5.3 | 5e-06 | 20/45 (A-172, NCI-H460, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.38×** | +5.3 | 6e-06 | 17/47 (SNU-423, CFPAC-1, …) | top dose only |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.34×** | +4.8 | 6e-05 | 8/47 (SW1417, MIA PaCa-2, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~23% of this change | **1.31×** | +4.4 | 3e-04 | 10/48 (SW480, HT-29, …) | all doses, stronger at high dose | position effect removed |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.25×** | +3.6 | 0.008 | 7/47 (HOP62, J82, …) | two highest doses | low cells (technical?) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.36×** | +3.6 | 0.008 | 5/48 (MIA PaCa-2, C32, …) | all doses, flat | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **1.25×** | +3.5 | 0.010 | 9/46 (LS 180, NCI-H23, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.50×** | +3.5 | 0.012 | 5/43 (A-172, LOX-IMVI, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Cobimetinib (drug)]] 5 µM |  | **1.24×** | +3.4 | 0.015 | 4/45 (NCI-H460, SK-MEL-2, …) | rises with dose |  |
| [[DT-061 (drug)]] 5 µM |  | **1.46×** | +3.3 | 0.025 | 3/41 (A498, A-427, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12355.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Selinexor (drug)]] 5 µM in 3 lines (A498 0.342×, PANC-1 0.416×, HS-578T 0.356×); [[Homoharringtonine (drug)]] 5 µM in 1 line (A-427 0.129×; ⚠ cell-cycle shift, would explain all of this change); [[Sunitinib (drug)]] 5 µM in 1 line (SW 900 0.0744×; ⚠ toxic).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM |  | **0.587×** | -12.6 | 2e-33 | 34/48 (A498, PANC-1, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~0% here); position effect removed |
| [[Selinexor (drug)]] 0.5 µM |  | **0.700×** | -6.0 | 7e-07 | 20/47 (LS 180, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); position effect removed |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~10% of this change | **0.800×** | -3.7 | 0.034 | 7/48 (HepG2/C3A, NCI-H460, …) | all doses, stronger at high dose | position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | 0.688× | -3.3 | 0.15 | 10/47 (SW 900, RKO, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.41 per unit of S-phase module lfc, -0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12355. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 17.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.129× (z -13.6) ⚠ cell-cycle shift, would explain all of this change |
| [[A498 (line)]] | wt | 13.9 | 0 | 1 | — | [[Selinexor (drug)]] 5 µM 0.342× (z -10.9) |
| [[HS-578T (line)]] | alt | 17.4 | 0 | 1 | — | [[Selinexor (drug)]] 5 µM 0.356× (z -9.2) |
| [[LS 180 (line)]] | wt | 17.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.93× (z +9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[NCI-H1792 (line)]] | alt | 6.13 | 0 | 1 (1 ⚠) | — | [[Neratinib (maleate) (drug)]] 0.5 µM 0.0749× (z -9.8) ⚠ cell-cycle shift, explains ~79% of this change |
| [[PANC-1 (line)]] | alt | 10.3 | 0 | 1 | — | [[Selinexor (drug)]] 5 µM 0.416× (z -10.1) |
| [[SW 900 (line)]] | alt | 6.03 | 0 | 1 (1 ⚠) | — | [[Sunitinib (drug)]] 5 µM 0.0744× (z -9.9) ⚠ toxic |
| [[A-172 (line)]] | wt | 9.93 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 9.92 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 6.51 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 11.8 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 4.73 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 7.32 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 8.30 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 9.98 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 8.44 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.63 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 5.54 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 7.41 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 7.27 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 7.50 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 15.0 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 6.45 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 5.07 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 9.58 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 20.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 9.65 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 9.07 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.53 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 6.93 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 9.38 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 8.08 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 9.43 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 6.87 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 5.12 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 11.4 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 9.27 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12355), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PSMB3]] | +0.67 | +0.68 / +0.60 | both halves | 7e-06 | pathway: ABC-family protein mediated transport |
| [[USP5]] | +0.67 | +0.66 / +0.59 | both halves | 7e-06 |  |
| [[PSMC4]] | +0.63 | +0.59 / +0.66 | both halves | 7e-06 | pathway: ABC-family protein mediated transport |
| [[ACTR1A]] | +0.63 | +0.57 / +0.64 | both halves | 1e-05 |  |
| [[NPLOC4]] | +0.62 | +0.65 / +0.58 | both halves | 7e-06 |  |
| [[TALDO1]] | +0.61 | +0.62 / +0.54 | both halves | 1e-05 | pathway: HALLMARK_ADIPOGENESIS |
| [[NECAB3]] | +0.59 | +0.60 / +0.52 | both halves | 1e-05 |  |
| [[PSMD1]] | +0.59 | +0.60 / +0.56 | both halves | 1e-05 | pathway: ABC-family protein mediated transport |
| [[UFD1]] | +0.58 | +0.59 / +0.51 | both halves | 1e-05 |  |
| [[FAM227A]] | +0.57 | +0.52 / +0.58 | both halves | 1e-05 |  |
| [[UBR4]] | +0.57 | +0.58 / +0.48 | both halves | 2e-05 |  |
| [[VCP]] | +0.56 | +0.55 / +0.54 | both halves | 1e-05 | pathway: ABC-family protein mediated transport |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF330]] | -0.57 | -0.46 / -0.58 | both halves | 2e-05 |  |
| [[SNX2]] | -0.53 | -0.52 / -0.47 | both halves | 2e-05 |  |
| [[RCHY1]] | -0.52 | -0.38 / -0.59 | both halves | 6e-05 |  |
| [[DMAC1]] | -0.52 | -0.47 / -0.49 | both halves | 2e-05 |  |
| [[EBAG9]] | -0.49 | -0.45 / -0.43 | both halves | 3e-05 |  |
| [[PPP4R2]] | -0.47 | -0.41 / -0.42 | both halves | 4e-05 |  |
| [[ZNF14]] | -0.47 | -0.44 / -0.37 | both halves | 9e-05 |  |
| [[RRAGD]] | -0.46 | -0.39 / -0.50 | both halves | 5e-05 |  |
| [[METTL14]] | -0.45 | -0.40 / -0.45 | both halves | 5e-05 |  |
| [[PPP1R3B]] | -0.44 | -0.45 / -0.38 | both halves | 7e-05 |  |
| [[ZNF585A]] | -0.44 | -0.42 / -0.40 | both halves | 4e-05 |  |
| [[POLR1H]] | -0.44 | -0.39 / -0.41 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ASPH]] | B | ASPH activity lowers ABCB8's level | lines that do not express ASPH (5) vs lines expressing it (45) | 1.52× higher at baseline in the lines without ASPH | 0.024 | ⚠ within organs, on part of the lines; also absent: HIPK2, EPS8, SCML1; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers ABCB8's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.0% of all compounds | 0.032 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 072]] — Degradation of DVL; 69 genes; every member is in the + arm (projection on the module's main direction 0.564). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-21.7, -12.9); signed map (-29.5, -30.0). **Vector** length 77.8, 13.6% of its response variance represented; |z| ≥ 3 in 1,050 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 0.5 µM |  | +7.1 | +12.0 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +6.8 | +13.9 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +6.5 | +13.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | +5.5 | +10.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | +5.4 | +11.9 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +2.8 | +3.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.2 | +6.0 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +1.7 | +3.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.7 | +5.3 |
| fall | [[Selinexor (drug)]] 5 µM |  | -7.4 | -12.6 |
|  | [[Selinexor (drug)]] 0.5 µM |  | -5.2 | -6.0 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -3.5 | -1.0 |
|  | [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~10% of this change | -3.0 | -3.7 |
|  | [[TAK-901 (drug)]] 5 µM |  | -2.2 | -3.3 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | -2.1 | -1.8 |
|  | [[EX229 (drug)]] 5 µM |  | -1.9 | -2.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.2 | -0.9 |
|  | [[Budesonide (drug)]] 0.05 µM |  | -1.0 | -1.5 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -1.0 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | ATP binding cassette subfamily B member 8 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q36.1 — chr7:151,028,422-151,047,782 (+) |
| Ensembl biotype | protein_coding |
| Also known as | EST328128, M-ABC1, MABC1, MITOSUR |
| Gene groups (HGNC) | ATP binding cassette subfamily B |
| Hallmark sets | ADIPOGENESIS |
| Reactome | 3 pathways, smallest: Mitochondrial ABC transporters; ABC-family protein mediated transport; Transport of small molecules |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NUT2](https://www.uniprot.org/uniprotkb/Q9NUT2) (Mitochondrial potassium channel ATP-binding subunit):

> ATP-binding subunit of the mitochondrial ATP-gated potassium channel (mitoK(ATP)). Together with pore-forming subunit CCDC51/MITOK of the mitoK(ATP) channel, mediates ATP-dependent potassium currents across the mitochondrial inner membrane. An increase in ATP intracellular levels closes the channel, inhibiting K(+) transport, whereas a decrease in ATP levels enhances K(+) uptake in the mitochondrial matrix. Plays a role in mitochondrial iron transport. Required for maintenance of normal cardiac …

**Summary**, from NCBI Gene [11194](https://www.ncbi.nlm.nih.gov/gene/11194):

> This nuclear gene encodes a multi-pass membrane protein that is targeted to the mitochondrial inner membrane. The encoded protein is an ATP-dependent transporter that may mediate the passage of organic and inorganic molecules out of the mitochondria. Loss of function of the related gene in mouse results in a disruption of iron homeostasis between the mitochondria and cytosol. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Aug 2013]

**Accessions** — [HGNC:49](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:49) · Entrez [11194](https://www.ncbi.nlm.nih.gov/gene/11194) · UniProt [Q9NUT2](https://www.uniprot.org/uniprotkb/Q9NUT2) · Ensembl [ENSG00000197150](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000197150)

## Data

Gene col 12355: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12355); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12355, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12355]; `tensor/DDL_lfc|DDL_z.npy` [12355]; `embed/gene_vectors.npy` [12355]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12355 or target_col == 12355). Every well: [[ABCB8 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ABCB8.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
