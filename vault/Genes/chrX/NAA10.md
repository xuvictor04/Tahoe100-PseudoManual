---
symbol: "NAA10"
type: "gene"
col: 2204
ensembl_id: "ENSG00000102030"
name: "N-alpha-acetyltransferase 10, NatA catalytic subunit"
location: "Xq28"
module: 58
arm: "+"
pooled_cpm: 19.1
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 1
n_dd_up_clean: 0
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/058", "evidence-flagged-only"]
generated_by: "tahoemap"
---

# NAA10

*N-alpha-acetyltransferase 10, NatA catalytic subunit* — Xq28

## At a glance

> [!summary] In this data
> ⚠ It is in the vector space only through drug-doses that carry an alert for it (its significant pooled drug-doses and per-line responses; `embed/genes.parquet` evidence_flagged_only): its vector, partners and module rest on changes that may come from what those drug-doses did to the cells rather than from its own regulation.
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (11 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 4.19× (z +9.6, q 3e-19, up in 38 of 41 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 4 lines (NCI-H460 7.65×, SW480 6.84×, LoVo 7.66×, PANC-1 4.40×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change); [[Dinaciclib (drug)]] 0.5 µM in 3 lines (SW480 8.78×, NCI-H460 5.15×, PANC-1 4.25×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 0.623× (z -4.7, q 0.001, down in 29 of 48 measured lines) ⚠ cell-cycle shift, explains ~78% of this change.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Selinexor (drug)]] 5 µM in 1 line (A498 0.323×; ⚠ cell-cycle shift, explains ~78% of this change); [[Cobimetinib (drug)]] 5 µM in 1 line (C32 0.0568×); [[Glycyrrhizic acid (drug)]] 5 µM in 1 line (SNU-1 0.0492×).
> Its strongest partners by |cos| (65 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 38 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ATP5F1D]] (+0.74, fdr 5e-05, ⚠ ATP5F1D in the vector space only through flagged drug-doses), [[PUSL1]] (+0.73, fdr 5e-05), [[SMYD3]] (+0.71, fdr 3e-05), [[STUB1]] (+0.68, fdr 5e-05); moves opposite to [[KRBA2]] (-0.63, fdr 1e-04), [[PBLD]] (-0.63, fdr 0.001, ⚠ not reproduced), [[ZNF610]] (-0.62, fdr 8e-04, ⚠ not reproduced), [[CCT6B]] (-0.61, fdr 3e-04), [[VPS52]] (-0.61, fdr 2e-04).
> It is in [[Module 058]], a single-armed module (oxidative phosphorylation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 11 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2204.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 4 lines (NCI-H460 7.65×, SW480 6.84×, LoVo 7.66×, PANC-1 4.40×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change); [[Dinaciclib (drug)]] 0.5 µM in 3 lines (SW480 8.78×, NCI-H460 5.15×, PANC-1 4.25×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | **4.19×** | +9.6 | 3e-19 | 38/41 (SW480, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | **3.48×** | +8.4 | 1e-14 | 27/28 (NCI-H460, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | **2.52×** | +6.0 | 4e-07 | 33/35 (KATO III, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | **2.19×** | +5.5 | 6e-06 | 39/47 (KATO III, SW480, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **2.15×** | +5.4 | 1e-05 | 39/47 (KATO III, HOP62, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~60% of this change | **2.04×** | +5.0 | 6e-05 | 39/47 (KATO III, SW480, …) | rises with dose | position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~72% of this change | **1.94×** | +4.6 | 3e-04 | 32/46 (NCI-H460, KATO III, …) | top dose only | position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~63% of this change | **1.76×** | +4.0 | 0.005 | 26/43 (CFPAC-1, J82, …) | inconsistent across doses | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.75×** | +3.8 | 0.009 | 26/41 (MIA PaCa-2, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~61% of this change | **1.75×** | +3.8 | 0.010 | 31/42 (NCI-H460, NCI-H1573, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.61×** | +3.4 | 0.041 | 23/46 (A-172, HepG2/C3A, …) | rises with dose | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, 1 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2204.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Selinexor (drug)]] 5 µM in 1 line (A498 0.323×; ⚠ cell-cycle shift, explains ~78% of this change); [[Cobimetinib (drug)]] 5 µM in 1 line (C32 0.0568×); [[Glycyrrhizic acid (drug)]] 5 µM in 1 line (SNU-1 0.0492×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~78% of this change | **0.623×** | -4.7 | 0.001 | 29/48 (A498, HS-578T, …) | all doses, stronger at high dose | low cells (technical?) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.58 per unit of S-phase module lfc, +0.56 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2204. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 21.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 7.65× (z +10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | — |
| [[PANC-1 (line)]] | alt | 34.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.40× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | — |
| [[SW480 (line)]] | alt | 14.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.78× (z +11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | — |
| [[A498 (line)]] | wt | 30.4 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.323× (z -10.5) ⚠ cell-cycle shift, explains ~78% of this change |
| [[C32 (line)]] | wt | 8.58 | 0 | 1 | — | [[Cobimetinib (drug)]] 5 µM 0.0568× (z -10.3) |
| [[LoVo (line)]] | wt | 12.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 7.66× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | — |
| [[SNU-1 (line)]] | wt | 12.2 | 0 | 1 | — | [[Glycyrrhizic acid (drug)]] 5 µM 0.0492× (z -8.9) |
| [[A-172 (line)]] | wt | 20.5 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 26.0 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 18.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 28.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 8.20 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 33.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 11.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 6.22 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 12.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 25.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 10.2 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 22.7 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 24.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 13.4 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 25.4 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 17.5 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 14.3 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 22.3 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 8.56 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 22.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.18 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 31.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 31.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 19.2 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 20.1 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 28.7 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 22.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 16.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2204), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*63 of its nearest partners move with it, 18 of them with an alert (⚠; 15 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATP5F1D]] ⚠ | +0.74 | +0.40 / +0.72 | both halves | 5e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[PUSL1]] | +0.73 | +0.40 / +0.64 | both halves | 5e-05 |  |
| [[SMYD3]] | +0.71 | +0.49 / +0.43 | both halves | 3e-05 |  |
| [[STUB1]] | +0.68 | +0.39 / +0.48 | both halves | 5e-05 |  |
| [[NPM3]] | +0.68 | +0.48 / +0.67 | both halves | 2e-05 |  |
| [[TMEM147]] | +0.67 | +0.59 / +0.61 | both halves | 7e-06 |  |
| [[MICOS13]] | +0.66 | +0.42 / +0.60 | both halves | 4e-05 |  |
| [[ANTKMT]] | +0.66 | +0.31 / +0.53 | both halves | 2e-04 |  |
| [[PAXX]] ⚠ | +0.65 | +0.34 / +0.60 | both halves | 1e-04 | ⚠ in the vector space only through flagged drug-doses |
| [[EIF3K]] | +0.65 | +0.41 / +0.54 | both halves | 4e-05 |  |
| [[MRPL12]] | +0.65 | +0.51 / +0.61 | both halves | 1e-05 |  |
| [[C20orf27]] | +0.65 | +0.49 / +0.44 | both halves | 3e-05 |  |
| [[TMEM256]] | +0.63 | +0.35 / +0.43 | both halves | 1e-04 |  |
| [[ANAPC11]] | +0.62 | +0.24 / +0.48 | both halves | 5e-04 |  |

## Genes that move opposite

*37 of its nearest partners move opposite, 20 of them with an alert (⚠; 20 not replicated); shown: the 12 strongest and the 5 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KRBA2]] | -0.63 | -0.36 / -0.33 | both halves | 1e-04 |  |
| [[PBLD]] | -0.63 | -0.33 / -0.17 | ⚠ not reproduced | 0.001 |  |
| [[ZNF610]] | -0.62 | -0.40 / -0.19 | ⚠ not reproduced | 8e-04 |  |
| [[CCT6B]] | -0.61 | -0.34 / -0.28 | both halves | 3e-04 |  |
| [[VPS52]] | -0.61 | -0.31 / -0.31 | both halves | 2e-04 |  |
| [[RBM48]] | -0.60 | -0.37 / -0.36 | both halves | 1e-04 |  |
| [[PNISR-AS1]] | -0.60 | -0.23 / -0.29 | both halves | 5e-04 |  |
| [[EIF4G2]] | -0.60 | -0.20 / -0.48 | ⚠ not reproduced | 8e-04 |  |
| [[ERCC6L2-AS1]] | -0.59 | -0.30 / -0.19 | ⚠ not reproduced | 8e-04 |  |
| [[CHD3]] | -0.59 | -0.42 / -0.39 | both halves | 5e-05 |  |
| [[MR1]] | -0.59 | -0.37 / -0.18 | ⚠ not reproduced | 0.001 |  |
| [[TRMO]] | -0.59 | -0.46 / -0.42 | both halves | 4e-05 |  |
| [[ZXDA]] | -0.56 | -0.29 / -0.29 | both halves | 3e-04 |  |
| [[POLR2M]] | -0.56 | -0.38 / -0.28 | both halves | 3e-04 |  |
| [[LINC03015]] | -0.56 | -0.31 / -0.39 | both halves | 2e-04 |  |
| [[ERMAP]] | -0.55 | -0.34 / -0.26 | both halves | 3e-04 |  |
| [[LPXN]] | -0.55 | -0.26 / -0.21 | both halves | 7e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity lowers NAA10's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 058]] — oxidative phosphorylation; 80 genes; every member is in the + arm (projection on the module's main direction 0.707). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- ⚠ **In the space only through flagged drug-doses**: its significant pooled drug-doses and per-line responses all carry an alert (`embed/genes.parquet` evidence_flagged_only), so its module and partners may reflect what those drug-doses did to the cells.
- **Nodal map** (x, y) = (-47.8, -15.2); signed map (-31.7, 3.5). **Vector** length 53.7, 12.6% of its response variance represented; |z| ≥ 3 in 610 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Cristae formation* (reactome, mean cos +0.56 to 4).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~60% of this change | +3.3 | +5.0 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | +3.0 | +5.5 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~50% of this change | +2.8 | +5.4 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +2.6 | +2.9 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | +2.0 | +3.4 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.8 | +0.7 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +1.2 | +2.5 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | +1.0 | +1.6 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.0 | +1.7 |
|  | [[EX229 (drug)]] 5 µM |  | +0.9 | +1.7 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~78% of this change | -5.7 | -4.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.4 | +1.0 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.1 | -2.5 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -2.9 | -2.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -2.6 | +3.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.2 | -2.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.8 | +0.2 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.4 | -3.0 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.3 | -2.4 |
|  | [[Filgotinib (drug)]] 5 µM |  | -1.1 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | N-alpha-acetyltransferase 10, NatA catalytic subunit |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xq28 — chrX:153,929,225-153,935,080 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DXS707, TE2; previously ARD1, ARD1A |
| Gene groups (HGNC) | N-alpha-acetyltransferase subunits; GCN5 related N-acetyltransferases |
| Matched by | ensembl_id |

**Function**, from UniProt [P41227](https://www.uniprot.org/uniprotkb/P41227) (N-alpha-acetyltransferase 10):

> Catalytic subunit of N-terminal acetyltransferase complexes which display alpha (N-terminal) acetyltransferase activity. Acetylates amino termini that are devoid of initiator methionine. The alpha (N-terminal) acetyltransferase activity may be important for vascular, hematopoietic and neuronal growth and development. Without NAA15, displays epsilon (internal) acetyltransferase activity towards HIF1A, thereby promoting its degradation. Represses MYLK kinase activity by acetylation, and thus …

**Summary**, from NCBI Gene [8260](https://www.ncbi.nlm.nih.gov/gene/8260):

> N-alpha-acetylation is among the most common post-translational protein modifications in eukaryotic cells. This process involves the transfer of an acetyl group from acetyl-coenzyme A to the alpha-amino group on a nascent polypeptide and is essential for normal cell function. This gene encodes an N-terminal acetyltransferase that functions as the catalytic subunit of the major amino-terminal acetyltransferase A complex. Mutations in this gene are the cause of Ogden syndrome. Alternate splicing …

**Accessions** — [HGNC:18704](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18704) · Entrez [8260](https://www.ncbi.nlm.nih.gov/gene/8260) · UniProt [P41227](https://www.uniprot.org/uniprotkb/P41227) · Ensembl [ENSG00000102030](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000102030)

## Data

Gene col 2204: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2204); `tables/drug_effects.parquet` (12 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2204, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2204]; `tensor/DDL_lfc|DDL_z.npy` [2204]; `embed/gene_vectors.npy` [2204]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2204 or target_col == 2204). Every well: [[NAA10 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NAA10.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
