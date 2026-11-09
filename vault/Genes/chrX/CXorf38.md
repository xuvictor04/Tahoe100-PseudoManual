---
symbol: "CXorf38"
type: "gene"
col: 11727
ensembl_id: "ENSG00000185753"
name: "chromosome X open reading frame 38"
location: "Xp11.4"
module: 20
arm: "-"
pooled_cpm: 35.46
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 0
n_dd_up_clean: 7
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/020"]
generated_by: "tahoemap"
---

# CXorf38

*chromosome X open reading frame 38* — Xp11.4

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (5 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 1.70× (z +11.1, q 4e-26, up in 38 of 48 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 6 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Niclosamide (olamine) (drug)]] 5 µM in 2 lines (C-33 A 0.0959×, HepG2/C3A 0.119×; ⚠ toxic; cell-cycle shift, explains ~38% of this change); [[Homoharringtonine (drug)]] 5 µM in 2 lines (COLO 205 0.286×, NCI-H1792 0.332×; ⚠ cell-cycle shift, explains ~61% of this change); [[Ouabain (Octahydrate) (drug)]] 5 µM in 2 lines (SW480 0.435×, NCI-H1573 0.423×; ⚠ cell-cycle shift, explains ~0% of this change); [[Capivasertib (drug)]] 5 µM in 1 line (SHP-77 0.0718×); [[Medroxyprogesterone acetate (drug)]] 0.05 µM in 1 line (Hs 766T 0.409×).
> Its strongest partners by |cos| (94 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 10 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ELOF1]] (+0.58, fdr 4e-05), [[PDGFB]] (+0.57, fdr 3e-05), [[AFTPH]] (+0.57, fdr 2e-05); moves opposite to [[HCFC1]] (-0.58, fdr 3e-05), [[RCN1]] (-0.52, fdr 2e-04), [[CRPPA]] (-0.51, fdr 2e-04).
> It sits in the **-** arm of [[Module 020]] (Cap-dependent Translation Initiation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[PDGFB]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 6 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11727.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **1.70×** | +11.1 | 4e-26 | 38/48 (NCI-H460, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.68×** | +10.9 | 2e-25 | 40/48 (NCI-H460, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.52×** | +8.8 | 2e-16 | 32/48 (SNU-423, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.39×** | +7.0 | 5e-10 | 29/48 (NCI-H2347, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.38×** | +6.8 | 1e-09 | 29/48 (PANC-1, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.36×** | +6.2 | 6e-08 | 24/48 (LoVo, NCI-H460, …) | rises with dose | composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~61% of this change | **1.22×** | +5.9 | 3e-07 | 24/47 (HEC-1-A, A498, …) | rises with dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.25×** | +4.6 | 3e-04 | 19/45 (HEC-1-A, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **1.50×** | +4.5 | 5e-04 | 20/49 (RPMI-7951, PANC-1, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~19% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **1.21×** | +4.1 | 0.002 | 20/48 (PANC-1, KATO III, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.14× | +3.8 | 0.006 | 12/48 (HEC-1-A, MIA PaCa-2, …) | top dose only | low cells (technical?) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~38% of this change | **1.20×** | +3.7 | 0.008 | 17/47 (KATO III, NCI-H460, …) | top dose only |  |
| [[Rosiglitazone (drug)]] 5 µM |  | 1.19× | +3.6 | 0.015 | 17/47 (SW480, PANC-1, …) | top dose only |  |
| [[Mebendazole (drug)]] 5 µM |  | 1.17× | +3.3 | 0.046 | 7/48 (NCI-H1792, SW480, …) | top dose only |  |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.24×** | +3.2 | 0.046 | 7/47 (SW480, HS-578T, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 11727.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 6 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Niclosamide (olamine) (drug)]] 5 µM in 2 lines (C-33 A 0.0959×, HepG2/C3A 0.119×; ⚠ toxic; cell-cycle shift, explains ~38% of this change); [[Homoharringtonine (drug)]] 5 µM in 2 lines (COLO 205 0.286×, NCI-H1792 0.332×; ⚠ cell-cycle shift, explains ~61% of this change); [[Ouabain (Octahydrate) (drug)]] 5 µM in 2 lines (SW480 0.435×, NCI-H1573 0.423×; ⚠ cell-cycle shift, explains ~0% of this change); [[Capivasertib (drug)]] 5 µM in 1 line (SHP-77 0.0718×); [[Medroxyprogesterone acetate (drug)]] 0.05 µM in 1 line (Hs 766T 0.409×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Hydroxyurea (drug)]] 5 µM |  | 0.831× | -3.7 | 0.10 | 9/48 (BT-474, SNU-423, …) | top dose only |  |
| [[Belumosudil (drug)]] 5 µM |  | 0.846× | -3.4 | 0.16 | 13/48 (C-33 A, RKO, …) | top dose only |  |
| [[Budesonide (drug)]] 5 µM |  | 0.853× | -3.3 | 0.16 | 5/48 (Panc 03.27, HS-578T, …) | top dose only |  |
| [[Quinestrol (drug)]] 5 µM |  | 0.904× | -3.0 | 0.37 | 3/49 (NCI-H1792, CHP-212, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.08 per unit of S-phase module lfc, +0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11727. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C-33 A (line)]] | alt | 55.3 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0959× (z -19.1) ⚠ toxic; cell-cycle shift, explains ~38% of this change |
| [[MIA PaCa-2 (line)]] | alt | 30.0 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.65× (z +10.4) ⚠ cell-cycle shift, explains ~59% of this change | — |
| [[A-427 (line)]] | wt | 34.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.234× (z -11.7) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[COLO 205 (line)]] | alt | 43.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.286× (z -13.7) ⚠ cell-cycle shift, explains ~61% of this change |
| [[HEC-1-A (line)]] | alt | 55.2 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.72× (z +9.8) ⚠ cell-cycle shift, explains ~61% of this change | — |
| [[HepG2_C3A (line)]] | wt | 17.3 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.119× (z -10.9) ⚠ toxic; cell-cycle shift, explains ~38% of this change |
| [[Hs 766T (line)]] | wt | 50.9 | 0 | 1 | — | [[Medroxyprogesterone acetate (drug)]] 0.05 µM 0.409× (z -8.6) |
| [[LoVo (line)]] | wt | 28.6 | 1 (1 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 2.94× (z +9.8) ⚠ cell-cycle shift, explains ~35% of this change | — |
| [[NCI-H1573 (line)]] | alt | 54.0 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.423× (z -8.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H1792 (line)]] | alt | 28.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.332× (z -12.7) ⚠ cell-cycle shift, explains ~61% of this change |
| [[Panc 03.27 (line)]] | alt | 41.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.375× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SHP-77 (line)]] | alt | 19.3 | 0 | 1 | — | [[Capivasertib (drug)]] 5 µM 0.0718× (z -9.1) |
| [[SW480 (line)]] | alt | 69.2 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.435× (z -11.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 52.8 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 30.5 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 44.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 34.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 32.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 25.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 21.0 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 31.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 26.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 45.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 34.0 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 22.2 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 26.4 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 27.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 31.1 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 37.1 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 47.8 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 17.3 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 29.7 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 33.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 22.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 43.7 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 32.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 35.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 24.3 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 25.2 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 28.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 48.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 20.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 22.0 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 41.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 41.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 21.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 23.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 49.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 27.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11727), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*55 of its nearest partners move with it, 7 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ELOF1]] | +0.58 | +0.40 / +0.54 | both halves | 4e-05 |  |
| [[PDGFB]] | +0.57 | +0.55 / +0.46 | both halves | 3e-05 |  |
| [[AFTPH]] | +0.57 | +0.47 / +0.51 | both halves | 2e-05 |  |
| [[CDKN2D]] | +0.57 | +0.43 / +0.50 | both halves | 3e-05 |  |
| [[IL10RB]] | +0.55 | +0.29 / +0.63 | both halves | 2e-04 |  |
| [[FAM89B]] | +0.55 | +0.41 / +0.39 | both halves | 6e-05 |  |
| [[RHOG]] | +0.55 | +0.45 / +0.51 | both halves | 3e-05 |  |
| [[INIP]] | +0.54 | +0.47 / +0.40 | both halves | 5e-05 |  |
| [[ETHE1]] | +0.53 | +0.45 / +0.35 | both halves | 1e-04 |  |
| [[PITPNA-AS1]] | +0.52 | +0.32 / +0.49 | both halves | 2e-04 |  |
| [[RRAS]] | +0.52 | +0.28 / +0.44 | both halves | 3e-04 |  |
| [[MVP]] | +0.51 | +0.50 / +0.43 | both halves | 3e-05 |  |

## Genes that move opposite

*45 of its nearest partners move opposite, 3 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HCFC1]] | -0.58 | -0.44 / -0.52 | both halves | 3e-05 |  |
| [[RCN1]] | -0.52 | -0.29 / -0.43 | both halves | 2e-04 |  |
| [[CRPPA]] | -0.51 | -0.29 / -0.41 | both halves | 2e-04 |  |
| [[U2AF2]] | -0.51 | -0.22 / -0.50 | both halves | 6e-04 |  |
| [[ILF3]] | -0.50 | -0.26 / -0.52 | both halves | 3e-04 |  |
| [[SRSF5]] | -0.50 | -0.43 / -0.29 | both halves | 3e-04 |  |
| [[SRSF1]] | -0.50 | -0.29 / -0.48 | both halves | 2e-04 |  |
| [[CERS2]] | -0.50 | -0.36 / -0.42 | both halves | 9e-05 |  |
| [[DUS3L]] | -0.50 | -0.41 / -0.34 | both halves | 1e-04 |  |
| [[RCC2]] | -0.50 | -0.28 / -0.43 | both halves | 3e-04 |  |
| [[SNX5]] | -0.50 | -0.30 / -0.40 | both halves | 2e-04 |  |
| [[STRN4]] | -0.49 | -0.36 / -0.42 | both halves | 9e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PDGFB]] | B | PDGFB activity raises CXorf38's level | lines that do not express PDGFB (16) vs lines expressing it (34) | 1.34× lower at baseline in the lines without PDGFB | 0.038 | ⚠ within organs, on part of the lines; also absent: PRAG1, LGALS3, ADAM8 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 020]] — Cap-dependent Translation Initiation; 191 genes; this gene is in the **-** arm (projection on the module's main direction -0.409). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-34.3, -15.3); signed map (-13.5, 3.9). **Vector** length 76.7, 13.7% of its response variance represented; |z| ≥ 3 in 800 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM |  | +3.1 | +10.9 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +3.0 | +7.0 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +2.8 | +6.8 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | +2.5 | +6.2 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +2.1 | +11.1 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.8 | +0.5 |
|  | [[Sivelestat (sodium tetrahydrate) (drug)]] 0.5 µM |  | +1.4 | +2.8 |
|  | [[Palmatine (chloride) (drug)]] 5 µM |  | +1.1 | +0.6 |
|  | [[Arbutin (drug)]] 5 µM |  | +1.1 | +1.2 |
|  | [[Vilanterol (drug)]] 5 µM |  | +1.1 | +1.0 |
| fall | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | -3.9 | +0.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.5 | -2.4 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.5 | -2.0 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.1 | -2.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | -3.0 | +0.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.5 | -1.2 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.1 | -3.4 |
|  | [[Budesonide (drug)]] 5 µM |  | -1.9 | -3.3 |

## What is on record

|  |  |
|---|---|
| Name | chromosome X open reading frame 38 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xp11.4 — chrX:40,626,921-40,647,561 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MGC39350 |
| Matched by | ensembl_id |

UniProt [Q8TB03](https://www.uniprot.org/uniprotkb/Q8TB03) carries no function annotation.

**Summary**, from NCBI Gene [159013](https://www.ncbi.nlm.nih.gov/gene/159013):

> Located in mitochondrion. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:28589](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28589) · Entrez [159013](https://www.ncbi.nlm.nih.gov/gene/159013) · UniProt [Q8TB03](https://www.uniprot.org/uniprotkb/Q8TB03) · Ensembl [ENSG00000185753](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000185753)

## Data

Gene col 11727: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11727); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11727, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11727]; `tensor/DDL_lfc|DDL_z.npy` [11727]; `embed/gene_vectors.npy` [11727]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11727 or target_col == 11727). Every well: [[CXorf38 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CXorf38.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
