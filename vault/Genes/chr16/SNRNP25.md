---
symbol: "SNRNP25"
type: "gene"
col: 8468
ensembl_id: "ENSG00000161981"
name: "small nuclear ribonucleoprotein U11/U12 subunit 25"
location: "16p13.3"
module: 58
arm: "+"
pooled_cpm: 5.26
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 2
n_dd_up_clean: 0
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/058"]
generated_by: "tahoemap"
---

# SNRNP25

*small nuclear ribonucleoprotein U11/U12 subunit 25* — 16p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (10 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 5.30× (z +12.6, q 7e-34, up in 24 of 26 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (PANC-1 5.74×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 0.575× (z -4.2, q 0.009, down in 18 of 39 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Bortezomib (drug)]] 0.05 µM in 1 line (A498 0.0387×; ⚠ cell-cycle shift, would explain all of this change); [[Lidocaine (hydrochloride) (drug)]] 0.05 µM in 1 line (NCI-H460 0.104×); [[Homoharringtonine (drug)]] 5 µM in 1 line (NCI-H2030 0.194×).
> Its strongest partners by |cos| (80 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 23 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZDHHC12]] (+0.73, fdr 1e-05), [[PAFAH1B3]] (+0.72, fdr 1e-05), [[CDK5]] (+0.70, fdr 3e-05); moves opposite to [[SMIM15-AS1]] (-0.63, fdr 7e-05), [[TAS2R4]] (-0.63, fdr 2e-04), [[GALNT7-DT]] (-0.62, fdr 6e-04).
> It is in [[Module 058]], a single-armed module (oxidative phosphorylation).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[UCP2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 10 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8468.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (PANC-1 5.74×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | **5.30×** | +12.6 | 7e-34 | 24/26 (PANC-1, A498, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | **3.94×** | +10.0 | 5e-21 | 10/11 (A498, HOP62, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **3.35×** | +9.2 | 1e-17 | 45/46 (SW480, NCI-H460, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **3.18×** | +8.8 | 3e-16 | 40/46 (SW480, KATO III, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | **3.24×** | +8.2 | 2e-14 | 10/14 (A498, J82, …) | all doses, stronger at high dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~38% of this change | **2.24×** | +6.1 | 9e-08 | 13/26 (PANC-1, KATO III, …) | inconsistent across doses | low cells (technical?) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~71% of this change | **2.06×** | +5.5 | 3e-06 | 30/46 (SW480, AsPC-1, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~56% of this change | **1.84×** | +4.5 | 6e-04 | 16/31 (PANC-1, A-427, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~34% of this change | **1.66×** | +3.7 | 0.014 | 11/28 (HCT15, HT-29, …) | inconsistent across doses |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~71% of this change | **1.38×** | +3.4 | 0.034 | 14/47 (SNU-1, A-172, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 8468.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Bortezomib (drug)]] 0.05 µM in 1 line (A498 0.0387×; ⚠ cell-cycle shift, would explain all of this change); [[Lidocaine (hydrochloride) (drug)]] 0.05 µM in 1 line (NCI-H460 0.104×); [[Homoharringtonine (drug)]] 5 µM in 1 line (NCI-H2030 0.194×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.575×** | -4.2 | 0.009 | 18/39 (LOX-IMVI, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.678×** | -4.1 | 0.009 | 24/40 (NCI-H2030, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.77 per unit of S-phase module lfc, +0.38 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8468. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 7.11 | 0 | 1 (1 ⚠) | — | [[Bortezomib (drug)]] 0.05 µM 0.0387× (z -14.2) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H2030 (line)]] | alt | 6.55 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.194× (z -8.9) |
| [[NCI-H460 (line)]] | wt | 3.86 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.104× (z -9.0) |
| [[PANC-1 (line)]] | alt | 7.84 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.74× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | — |
| [[A-172 (line)]] | wt | 6.70 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 9.94 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 4.86 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 7.65 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.60 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 7.78 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.33 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 4.00 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.59 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.94 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.41 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 7.28 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 8.12 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.71 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 3.08 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.76 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 4.13 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 6.06 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.66 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 5.61 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 8.71 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 3.77 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.83 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 6.99 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.63 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.96 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.19 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.70 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.84 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 5.60 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.93 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.53 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 5.14 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.73 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 8.97 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.50 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.72 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.32 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.45 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.61 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.39 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 7.69 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.32 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 3.92 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8468), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*66 of its nearest partners move with it, 6 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZDHHC12]] | +0.73 | +0.52 / +0.67 | both halves | 1e-05 |  |
| [[PAFAH1B3]] | +0.72 | +0.52 / +0.59 | both halves | 1e-05 |  |
| [[CDK5]] | +0.70 | +0.46 / +0.70 | both halves | 3e-05 |  |
| [[POP5]] | +0.69 | +0.41 / +0.69 | both halves | 4e-05 |  |
| [[STUB1]] | +0.69 | +0.43 / +0.53 | both halves | 4e-05 |  |
| [[AP2S1]] | +0.69 | +0.57 / +0.48 | both halves | 2e-05 |  |
| [[NUDT1]] | +0.68 | +0.56 / +0.71 | both halves | 1e-05 |  |
| [[SLC39A3]] | +0.66 | +0.49 / +0.51 | both halves | 1e-05 |  |
| [[ANTKMT]] | +0.66 | +0.38 / +0.59 | both halves | 7e-05 |  |
| [[CENPW]] | +0.65 | +0.48 / +0.62 | both halves | 2e-05 |  |
| [[C20orf27]] | +0.65 | +0.45 / +0.50 | both halves | 3e-05 |  |
| [[POLR3K]] | +0.65 | +0.31 / +0.64 | both halves | 2e-04 | STRING 689; ⚠ same locus (0.2 kb: neighbours can correlate without regulation) |
| [[WRAP73]] | +0.65 | +0.42 / +0.42 | both halves | 4e-05 |  |

## Genes that move opposite

*34 of its nearest partners move opposite, 17 of them with an alert (⚠; 17 not replicated); shown: the 12 strongest and the 5 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SMIM15-AS1]] | -0.63 | -0.47 / -0.38 | both halves | 7e-05 |  |
| [[TAS2R4]] | -0.63 | -0.57 / -0.30 | both halves | 2e-04 |  |
| [[GALNT7-DT]] | -0.62 | -0.46 / -0.22 | both halves | 6e-04 |  |
| [[LRRC37A3]] | -0.62 | -0.46 / -0.25 | both halves | 4e-04 |  |
| [[CHD1-DT]] | -0.62 | -0.44 / -0.32 | both halves | 2e-04 |  |
| [[LHFPL3]] | -0.62 | -0.49 / -0.29 | both halves | 3e-04 |  |
| [[PPP1R12A-AS2]] | -0.60 | -0.44 / -0.17 | ⚠ not reproduced | 0.001 |  |
| [[MFF-DT]] | -0.60 | -0.41 / -0.26 | both halves | 4e-04 |  |
| [[ATE1OSP]] | -0.60 | -0.55 / -0.18 | ⚠ one half (not replicated) | 9e-04 |  |
| [[MAILR]] | -0.59 | -0.44 / -0.10 | ⚠ not reproduced | 0.003 |  |
| [[SEPTIN7-DT]] | -0.59 | -0.47 / -0.17 | ⚠ not reproduced | 0.001 |  |
| [[INTS6-AS1]] | -0.59 | -0.51 / -0.17 | ⚠ one half (not replicated) | 0.001 |  |
| [[DDX59-AS1]] | -0.57 | -0.44 / -0.27 | both halves | 3e-04 |  |
| [[CDKL3]] | -0.57 | -0.54 / -0.21 | both halves | 6e-04 |  |
| [[CROCC]] | -0.57 | -0.36 / -0.43 | both halves | 1e-04 |  |
| [[UGDH-AS1]] | -0.56 | -0.50 / -0.27 | both halves | 3e-04 |  |
| [[PCBP1-AS1]] | -0.56 | -0.35 / -0.23 | both halves | 5e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[UCP2]] | B | UCP2 activity raises SNRNP25's level | lines that do not express UCP2 (18) vs lines expressing it (32) | 1.32× lower at baseline in the lines without UCP2 | 0.079 | ⚠ within organs, on part of the lines; also absent: WNK2 |
| [[TCF19]] | B | TCF19 activity raises SNRNP25's level | lines that do not express TCF19 (5) vs lines expressing it (45) | 1.56× lower at baseline in the lines without TCF19 | 0.088 | ⚠ within organs, on part of the lines; also absent: CLSPN, AURKB, SMARCD3; maybe low, not absent |
| [[HDAC6]] | B | HDAC6 activity lowers SNRNP25's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 058]] — oxidative phosphorylation; 80 genes; every member is in the + arm (projection on the module's main direction 0.733). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-49.9, -14.1); signed map (-31.3, 2.6). **Vector** length 53.9, 9.23% of its response variance represented; |z| ≥ 3 in 680 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Cristae formation* (reactome, mean cos +0.50 to 4).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | +4.6 | +9.2 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~41% of this change | +4.2 | +8.8 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~71% of this change | +3.7 | +5.5 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~56% of this change | +2.7 | +4.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | +1.7 | +12.6 |
|  | [[Berbamine (drug)]] 0.05 µM |  | +1.0 | +2.3 |
|  | [[vincristine (drug)]] 0.5 µM |  | +0.9 | +2.5 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +0.9 | +2.4 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | +0.9 | +1.8 |
|  | [[Arbutin (drug)]] 5 µM |  | +0.9 | +2.9 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -3.8 | -4.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.0 | -0.7 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -2.8 | -4.1 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | -1.5 | -1.5 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.3 | -1.4 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.3 | +0.1 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -1.2 | -2.7 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.1 | -1.8 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -1.1 | -2.9 |

## What is on record

|  |  |
|---|---|
| Name | small nuclear ribonucleoprotein U11/U12 subunit 25 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16p13.3 — chr16:53,828-57,669 (+) |
| Ensembl biotype | protein_coding |
| Also known as | U11/U12-25K; previously C16orf33 |
| Gene groups (HGNC) | U11/U12 di-snRNP; U11 small nuclear ribonucleoprotein |
| Reactome | 4 pathways, smallest: mRNA Splicing - Minor Pathway; mRNA Splicing; Processing of Capped Intron-Containing Pre-mRNA |
| Matched by | ensembl_id |

UniProt [Q9BV90](https://www.uniprot.org/uniprotkb/Q9BV90) carries no function annotation.

**Summary**, from NCBI Gene [79622](https://www.ncbi.nlm.nih.gov/gene/79622):

> Two types of spliceosomes catalyze splicing of pre-mRNAs. The major U2-type spliceosome is found in all eukaryotes and removes U2-type introns, which represent more than 99% of pre-mRNA introns. The minor U12-type spliceosome is found in some eukaryotes and removes U12-type introns, which are rare and have distinct splice consensus signals. The U12-type spliceosome consists of several small nuclear RNAs and associated proteins. This gene encodes a 25K protein that is a component of the U12-type …

**Accessions** — [HGNC:14161](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14161) · Entrez [79622](https://www.ncbi.nlm.nih.gov/gene/79622) · UniProt [Q9BV90](https://www.uniprot.org/uniprotkb/Q9BV90) · Ensembl [ENSG00000161981](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000161981)

## Data

Gene col 8468: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8468); `tables/drug_effects.parquet` (12 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8468, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8468]; `tensor/DDL_lfc|DDL_z.npy` [8468]; `embed/gene_vectors.npy` [8468]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8468 or target_col == 8468). Every well: [[SNRNP25 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SNRNP25.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
