---
symbol: "ENPP7P4"
type: "gene"
col: 14263
ensembl_id: "ENSG00000241278"
name: "ectonucleotide pyrophosphatase/phosphodiesterase 7 pseudogene 4"
location: "3q21.2"
module: 75
arm: "+"
pooled_cpm: 4.05
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 9
n_dd_up_clean: 3
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/075"]
generated_by: "tahoemap"
---

# ENPP7P4

*ectonucleotide pyrophosphatase/phosphodiesterase 7 pseudogene 4* — 3q21.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.57× (z +10.9, q 7e-25, up in 3 of 5 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 1.57× (z +7.8, q 2e-12, up in 20 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (7 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.609× (z -6.1, q 7e-07, down in 19 of 47 measured lines) ⚠ cell-cycle shift, explains ~30% of this change. The strongest without an alert is [[Harringtonine (drug)]] 0.5 µM: 0.736× (z -3.8, q 0.025, down in 11 of 45 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 14 here, 5 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (SW48 0.192×, NCI-H23 0.230×; ⚠ cell-cycle shift, explains ~0% of this change); [[Ouabain (Octahydrate) (drug)]] 0.5 µM in 1 line (LoVo 0.0982×; ⚠ cell-cycle shift, explains ~37% of this change); [[Vilanterol (drug)]] 0.5 µM in 1 line (Panc 03.27 0.0468×); [[Oxaprozin (drug)]] 0.05 µM in 1 line (NCI-H2030 0.0700×); [[Bisoprolol (hemifumarate) (drug)]] 0.5 µM in 1 line (SNU-1 0.0613×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CFAP92]] (+0.59, fdr 1e-05), [[SLC9C1]] (+0.57, fdr 1e-05), [[PPP1R9A-AS1]] (+0.57, fdr 1e-05).
> It is in [[Module 075]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[APLN]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 3 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14263.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.57×** | +10.9 | 7e-25 | 3/5 (A498, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.57×** | +7.8 | 2e-12 | 20/45 (SW480, PANC-1, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.82×** | +7.3 | 5e-11 | 16/43 (NCI-H1573, LoVo, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.71×** | +6.6 | 8e-09 | 6/18 (SW480, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.49×** | +4.5 | 7e-04 | 4/8 (NCI-H2347, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.38×** | +3.9 | 0.008 | 13/43 (SK-MEL-2, HT-29, …) | top dose only |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | 1.41× | +3.0 | 0.20 | 1/32 (J82) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 7 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14263.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 14 here, 5 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (SW48 0.192×, NCI-H23 0.230×; ⚠ cell-cycle shift, explains ~0% of this change); [[Ouabain (Octahydrate) (drug)]] 0.5 µM in 1 line (LoVo 0.0982×; ⚠ cell-cycle shift, explains ~37% of this change); [[Vilanterol (drug)]] 0.5 µM in 1 line (Panc 03.27 0.0468×); [[Oxaprozin (drug)]] 0.05 µM in 1 line (NCI-H2030 0.0700×); [[Bisoprolol (hemifumarate) (drug)]] 0.5 µM in 1 line (SNU-1 0.0613×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.609×** | -6.1 | 7e-07 | 19/47 (NCI-H23, SW48, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.664×** | -5.0 | 1e-04 | 19/44 (NCI-H1573, SW48, …) | all doses, stronger at high dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.700×** | -4.4 | 0.002 | 13/45 (SW1417, HCT15, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.736×** | -3.8 | 0.025 | 11/45 (SW48, SNU-1, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **0.753×** | -3.5 | 0.054 | 13/46 (SW48, LoVo, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change | **0.755×** | -3.4 | 0.054 | 16/33 (SW480, SNU-1, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.758×** | -3.4 | 0.054 | 14/44 (LoVo, SNU-1, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **0.749×** | -3.4 | 0.054 | 9/43 (COLO 205, A-172, …) | rises with dose | composition shift |
| [[Ranolazine (drug)]] 0.5 µM |  | **0.762×** | -3.3 | 0.054 | 4/44 (HT-29, A-172, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.17 per unit of S-phase module lfc, -0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14263. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW48 (line)]] | wt | 19.7 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.192× (z -9.4) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.122× (z -8.5) |
| [[NCI-H2030 (line)]] | alt | 4.67 | 0 | 2 | — | [[Oxaprozin (drug)]] 0.05 µM 0.0700× (z -10.7) |
| [[SNU-1 (line)]] | wt | 8.82 | 0 | 2 (1 ⚠) | — | [[Bisoprolol (hemifumarate) (drug)]] 0.5 µM 0.0613× (z -9.4) |
| [[SW480 (line)]] | alt | 2.70 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.101× (z -10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change · without an alert: [[Valdecoxib (drug)]] 0.5 µM 0.128× (z -9.1) |
| [[COLO 205 (line)]] | alt | 10.5 | 0 | 1 | — | [[Orlistat (drug)]] 0.05 µM 0.0850× (z -8.7) |
| [[LoVo (line)]] | wt | 7.57 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0982× (z -12.7) ⚠ cell-cycle shift, explains ~37% of this change |
| [[NCI-H23 (line)]] | alt | 7.72 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.230× (z -8.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H2347 (line)]] | alt | 2.11 | 0 | 1 | — | [[Dexamethasone (drug)]] 0.5 µM 0.0653× (z -8.8) |
| [[Panc 03.27 (line)]] | alt | 5.48 | 0 | 1 | — | [[Vilanterol (drug)]] 0.5 µM 0.0468× (z -11.2) |
| [[PANC-1 (line)]] | alt | 1.90 | 0 | 1 | — | [[Canagliflozin (drug)]] 5 µM 0.0887× (z -9.0) |
| [[A-172 (line)]] | wt | 2.24 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 10.6 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.02 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.34 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 5.21 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.41 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.73 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 6.63 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.96 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.35 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.87 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.68 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 6.29 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 4.85 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.27 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.64 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.96 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.32 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.53 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.57 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 5.71 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 5.54 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.70 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 5.32 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.41 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 6.46 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.26 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.54 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.61 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.87 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.77 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 10.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.59 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.12 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.74 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.36 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.02 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 9.50 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.84 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.41 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14263), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CFAP92]] | +0.59 | +0.64 / +0.57 | both halves | 1e-05 |  |
| [[SLC9C1]] | +0.57 | +0.59 / +0.55 | both halves | 1e-05 |  |
| [[PPP1R9A-AS1]] | +0.57 | +0.61 / +0.51 | both halves | 1e-05 |  |
| [[FER1L6]] | +0.56 | +0.47 / +0.58 | both halves | 2e-05 |  |
| [[LINC02511]] | +0.56 | +0.53 / +0.53 | both halves | 1e-05 |  |
| [[DSG2-AS1]] | +0.56 | +0.42 / +0.54 | both halves | 4e-05 |  |
| [[MYO16]] | +0.56 | +0.55 / +0.60 | both halves | 1e-05 |  |
| [[SYT9-AS1]] | +0.55 | +0.56 / +0.54 | both halves | 1e-05 |  |
| [[DLGAP2]] | +0.55 | +0.50 / +0.55 | both halves | 1e-05 |  |
| [[CDH23]] | +0.54 | +0.50 / +0.59 | both halves | 1e-05 |  |
| [[RBFOX3]] | +0.54 | +0.50 / +0.60 | both halves | 1e-05 |  |
| [[LINC02932]] | +0.54 | +0.41 / +0.53 | both halves | 4e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[APLN]] | B | APLN activity lowers ENPP7P4's level | lines that do not express APLN (13) vs lines expressing it (37) | 1.34× higher at baseline in the lines without APLN | 0.084 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[ATF7IP2]] | B | ATF7IP2 activity raises ENPP7P4's level | lines that do not express ATF7IP2 (12) vs lines expressing it (38) | 1.56× lower at baseline in the lines without ATF7IP2 | 0.085 | ⚠ within organs, on part of the lines |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 075]]; 60 genes; every member is in the + arm (projection on the module's main direction 0.561). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (19.0, 31.9); signed map (30.7, 12.2). **Vector** length 49.2, 5.48% of its response variance represented; |z| ≥ 3 in 1,049 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +4.7 | +7.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.6 | +7.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.4 | +3.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.9 | +10.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.9 | +4.5 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.8 | +2.0 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +1.3 | +0.5 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | +1.0 | +2.3 |
| fall | [[Ipatasertib (drug)]] 5 µM |  | -1.1 | -1.1 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -0.9 | -2.0 |
|  | [[Vandetanib (drug)]] 5 µM |  | -0.8 | -1.4 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | -0.8 | -2.1 |
|  | [[Radotinib (drug)]] 5 µM |  | -0.8 | -0.3 |
|  | [[L-Thyroxine (sodium salt pentahydrate) (drug)]] 5 µM |  | -0.8 | -0.1 |
|  | [[Ralimetinib dimesylate (drug)]] 5 µM |  | -0.7 | +0.0 |

## What is on record

|  |  |
|---|---|
| Name | ectonucleotide pyrophosphatase/phosphodiesterase 7 pseudogene 4 |
| Locus type | pseudogene |
| Location | 3q21.2 — chr3:125,848,223-125,909,372 (+) |
| Ensembl biotype | transcribed_unprocessed_pseudogene |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:48687](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:48687) · Entrez [100421816](https://www.ncbi.nlm.nih.gov/gene/100421816) · Ensembl [ENSG00000241278](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000241278)

## Data

Gene col 14263: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14263); `tables/drug_effects.parquet` (16 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14263, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14263]; `tensor/DDL_lfc|DDL_z.npy` [14263]; `embed/gene_vectors.npy` [14263]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14263 or target_col == 14263). Every well: [[ENPP7P4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ENPP7P4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
