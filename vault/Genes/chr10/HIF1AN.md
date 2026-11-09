---
symbol: "HIF1AN"
type: "gene"
col: 9242
ensembl_id: "ENSG00000166135"
name: "hypoxia inducible factor 1 subunit alpha inhibitor"
location: "10q24.31"
module: 127
arm: "+"
pooled_cpm: 44.86
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 3
n_dd_up_clean: 4
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/127"]
generated_by: "tahoemap"
---

# HIF1AN

*hypoxia inducible factor 1 subunit alpha inhibitor* — 10q24.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 0.5 µM: 2.25× (z +12.6, q 7e-34, up in 46 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.625× (z -7.1, q 8e-10, down in 24 of 42 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 7 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 4 lines (LS 180 0.102×, HCT15 0.115×, C-33 A 0.207×, SW 900 0.321×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 3 lines (KATO III 0.247×, CHP-212 0.0769×, A-427 0.301×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 3 lines (Hs 766T 0.368×, SNU-423 0.452×, LOX-IMVI 0.496×; ⚠ cell-cycle shift, explains ~0% of this change); [[Medroxyprogesterone acetate (drug)]] 0.5 µM in 1 line (CHP-212 0.154×).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FCHSD1]] (+0.62, fdr 2e-05), [[PRPF31]] (+0.58, fdr 2e-05), [[RNF123]] (+0.57, fdr 4e-05); moves opposite to [[REV3L]] (-0.58, fdr 5e-05), [[ZCCHC8]] (-0.56, fdr 4e-05), [[ATXN2]] (-0.55, fdr 2e-05).
> It is in [[Module 127]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 2 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9242.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **2.25×** | +12.6 | 7e-34 | 46/48 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.13×** | +11.8 | 2e-29 | 45/48 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.73×** | +8.5 | 3e-15 | 45/48 (SW480, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.26×** | +5.1 | 4e-05 | 24/48 (NCI-H1573, A498, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~61% of this change | 1.17× | +3.4 | 0.071 | 18/48 (J82, LOX-IMVI, …) | top dose only | low cells (technical?) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.07× | +3.3 | 0.089 | 0/49 | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | 1.15× | +3.1 | 0.18 | 11/48 (HS-578T, A498, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 4 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9242.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 7 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 4 lines (LS 180 0.102×, HCT15 0.115×, C-33 A 0.207×, SW 900 0.321×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 3 lines (KATO III 0.247×, CHP-212 0.0769×, A-427 0.301×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 3 lines (Hs 766T 0.368×, SNU-423 0.452×, LOX-IMVI 0.496×; ⚠ cell-cycle shift, explains ~0% of this change); [[Medroxyprogesterone acetate (drug)]] 0.5 µM in 1 line (CHP-212 0.154×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.625×** | -7.1 | 8e-10 | 24/42 (LS 180, HCT15, …) | rises with dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **0.760×** | -4.3 | 0.005 | 28/47 (KATO III, CHP-212, …) | rises with dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~22% of this change | **0.767×** | -4.0 | 0.010 | 23/47 (SNU-423, NCI-H661, …) | top dose only | position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.836× | -4.0 | 0.010 | 22/48 (Hs 766T, SNU-423, …) | top dose only |  |
| [[Sivelestat (sodium tetrahydrate) (drug)]] 0.5 µM |  | 0.822× | -3.1 | 0.24 | 14/47 (J82, HEC-1-A, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.01 per unit of S-phase module lfc, -0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9242. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 35.0 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 2.67× (z +9.2) | — |
| [[LS 180 (line)]] | wt | 34.7 | 2 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.36× (z +10.8) | [[Dinaciclib (drug)]] 5 µM 0.102× (z -19.9) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 52.7 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.63× (z +14.1) | — |
| [[A-172 (line)]] | wt | 44.8 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.62× (z +8.7) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.364× (z -8.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[C-33 A (line)]] | alt | 58.5 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 3.53× (z +9.2) | [[Dinaciclib (drug)]] 5 µM 0.207× (z -11.0) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 50.9 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0769× (z -12.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change · without an alert: [[Medroxyprogesterone acetate (drug)]] 0.5 µM 0.154× (z -8.8) |
| [[HOP62 (line)]] | alt | 53.9 | 0 | 2 (2 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.394× (z -9.3) ⚠ cell-cycle shift, explains ~0% of this change |
| [[Hs 766T (line)]] | wt | 31.8 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.21× (z +8.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.368× (z -10.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HS-578T (line)]] | alt | 25.7 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.38× (z +9.4) | — |
| [[KATO III (line)]] | alt | 39.4 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.247× (z -12.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change |
| [[LoVo (line)]] | wt | 40.5 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 3.71× (z +12.3) | — |
| [[PANC-1 (line)]] | alt | 63.0 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.26× (z +9.1) | — |
| [[RKO (line)]] | wt | 49.3 | 0 | 2 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.133× (z -16.1) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[SNU-423 (line)]] | alt | 50.4 | 0 | 2 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.452× (z -9.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-427 (line)]] | wt | 47.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.301× (z -11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change |
| [[A549 (line)]] | wt | 47.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.372× (z -8.7) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 56.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.150× (z -9.0) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 55.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.115× (z -13.7) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 39.6 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.496× (z -9.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[MIA PaCa-2 (line)]] | alt | 44.3 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.86× (z +9.2) | — |
| [[NCI-H1573 (line)]] | alt | 53.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.36× (z +11.0) | — |
| [[NCI-H1792 (line)]] | alt | 39.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.353× (z -8.6) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 42.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.318× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change |
| [[SW 900 (line)]] | alt | 47.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.321× (z -9.3) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 35.8 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 31.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 45.6 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 53.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 45.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 55.8 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 48.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 49.3 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 31.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 43.8 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 21.9 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 40.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 40.7 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 62.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 32.4 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 47.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 43.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 27.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 56.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 37.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 45.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 53.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 35.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 48.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 46.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 44.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9242), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*68 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FCHSD1]] | +0.62 | +0.47 / +0.57 | both halves | 2e-05 |  |
| [[PRPF31]] | +0.58 | +0.48 / +0.54 | both halves | 2e-05 |  |
| [[RNF123]] | +0.57 | +0.42 / +0.47 | both halves | 4e-05 |  |
| [[POLR2J3]] | +0.57 | +0.59 / +0.49 | both halves | 1e-05 |  |
| [[ZNF445]] | +0.57 | +0.44 / +0.44 | both halves | 3e-05 |  |
| [[RNF40]] | +0.56 | +0.51 / +0.49 | both halves | 1e-05 |  |
| [[SNAP47]] | +0.55 | +0.38 / +0.51 | both halves | 7e-05 |  |
| [[SRRD]] | +0.55 | +0.50 / +0.46 | both halves | 3e-05 |  |
| [[ZNF473]] | +0.55 | +0.45 / +0.55 | both halves | 3e-05 |  |
| [[EXOC3]] | +0.55 | +0.54 / +0.46 | both halves | 3e-05 |  |
| [[MIER2]] | +0.54 | +0.41 / +0.53 | both halves | 4e-05 |  |
| [[ZNF558]] | +0.54 | +0.55 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

*32 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[REV3L]] | -0.58 | -0.52 / -0.39 | both halves | 5e-05 |  |
| [[ZCCHC8]] | -0.56 | -0.51 / -0.40 | both halves | 4e-05 |  |
| [[ATXN2]] | -0.55 | -0.55 / -0.47 | both halves | 2e-05 |  |
| [[COBLL1]] | -0.54 | -0.47 / -0.40 | both halves | 5e-05 |  |
| [[SGMS1]] | -0.54 | -0.55 / -0.37 | both halves | 9e-05 |  |
| [[ZBTB8A]] | -0.53 | -0.38 / -0.40 | both halves | 6e-05 |  |
| [[ATAD2B]] | -0.53 | -0.38 / -0.46 | both halves | 6e-05 |  |
| [[UVRAG]] | -0.53 | -0.50 / -0.47 | both halves | 2e-05 |  |
| [[TDRD3]] | -0.52 | -0.30 / -0.48 | both halves | 2e-04 |  |
| [[CABLES1]] | -0.52 | -0.45 / -0.36 | both halves | 1e-04 |  |
| [[HOXB7]] | -0.51 | -0.40 / -0.39 | both halves | 5e-05 |  |
| [[GNAQ]] | -0.51 | -0.39 / -0.46 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity lowers HIF1AN's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 0.8% of all compounds | 0.044 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[MOCS1]] | B | MOCS1 activity raises HIF1AN's level | lines that do not express MOCS1 (13) vs lines expressing it (36) | 1.14× lower at baseline in the lines without MOCS1 | 0.048 | ⚠ within organs, on part of the lines; also absent: SNRPN, MYH10, ANKRD6 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 127]]; 37 genes; every member is in the + arm (projection on the module's main direction 0.601). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.27; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-0.0, -25.3); signed map (-14.1, -28.9). **Vector** length 80.0, 16.8% of its response variance represented; |z| ≥ 3 in 776 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM |  | +5.4 | +12.6 |
|  | [[Panobinostat (drug)]] 5 µM |  | +4.8 | +11.8 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | +3.9 | +0.1 |
|  | [[Belinostat (drug)]] 5 µM |  | +3.1 | +8.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.8 | +2.3 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.6 | +1.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.2 | +2.2 |
|  | [[Infigratinib (drug)]] 0.05 µM |  | +1.7 | -0.2 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +1.6 | +0.9 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -7.0 | -4.0 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -5.2 | -2.1 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -4.7 | -2.4 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~22% of this change | -4.3 | -4.0 |
|  | [[Binimetinib (drug)]] 5 µM |  | -2.3 | -1.5 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.3 | -0.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.2 | -2.4 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.1 | -0.8 |
|  | [[Binimetinib (drug)]] 0.05 µM |  | -1.8 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | hypoxia inducible factor 1 subunit alpha inhibitor |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q24.31 — chr10:100,529,072-100,559,998 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ20615, DKFZp762F1811, FLJ22027, FIH1 |
| Gene groups (HGNC) | JmjC hydroxylases |
| Reactome | 3 pathways, smallest: Cellular response to hypoxia; Cellular responses to stress; Cellular responses to stimuli |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NWT6](https://www.uniprot.org/uniprotkb/Q9NWT6) (Hypoxia-inducible factor 1-alpha inhibitor):

> Hydroxylates HIF-1 alpha at 'Asn-803' in the C-terminal transactivation domain (CAD). Functions as an oxygen sensor and, under normoxic conditions, the hydroxylation prevents interaction of HIF-1 with transcriptional coactivators including Cbp/p300-interacting transactivator. Involved in transcriptional repression through interaction with HIF1A, VHL and histone deacetylases. Hydroxylates specific Asn residues within ankyrin repeat domains (ARD) of NFKB1, NFKBIA, NOTCH1, ASB4, PPP1R12A and …

**Summary**, from NCBI Gene [55662](https://www.ncbi.nlm.nih.gov/gene/55662):

> Enables several functions, including 2-oxoglutarate-dependent dioxygenase activity; NF-kappaB binding activity; and transition metal ion binding activity. Involved in negative regulation of Notch signaling pathway and positive regulation of myoblast differentiation. Located in cytosol; nucleoplasm; and perinuclear region of cytoplasm. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:17113](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17113) · Entrez [55662](https://www.ncbi.nlm.nih.gov/gene/55662) · UniProt [Q9NWT6](https://www.uniprot.org/uniprotkb/Q9NWT6) · Ensembl [ENSG00000166135](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000166135)

## Data

Gene col 9242: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9242); `tables/drug_effects.parquet` (12 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9242, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9242]; `tensor/DDL_lfc|DDL_z.npy` [9242]; `embed/gene_vectors.npy` [9242]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9242 or target_col == 9242). Every well: [[HIF1AN — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HIF1AN.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
