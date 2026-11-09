---
symbol: "MTHFSD"
type: "gene"
col: 2341
ensembl_id: "ENSG00000103248"
name: "methenyltetrahydrofolate synthetase domain containing"
location: "16q24.1"
module: 135
arm: "+"
pooled_cpm: 11.88
n_lines_expressing: 50
n_dd_up: 0
n_dd_down: 12
n_dd_up_clean: 0
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/135"]
generated_by: "tahoemap"
---

# MTHFSD

*methenyltetrahydrofolate synthetase domain containing* — 16q24.1

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (9 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.534× (z -7.9, q 1e-12, down in 29 of 44 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 0.737× (z -5.4, q 5e-06, down in 26 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF507]] (+0.76, fdr 7e-06), [[DNAJC11]] (+0.75, fdr 7e-06), [[TMEM128]] (+0.74, fdr 7e-06); moves opposite to [[CARHSP1]] (-0.71, fdr 7e-06), [[GMCL1]] (-0.69, fdr 1e-05), [[GNB2]] (-0.68, fdr 4e-05).
> It sits in the **+** arm of [[Module 135]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[ZNF613]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 2 with an alert ⚠. 0 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2341.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belumosudil (drug)]] 5 µM |  | 1.31× | +3.2 | 0.23 | 12/46 (LS 180, KATO III, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | 1.19× | +3.1 | 0.23 | 14/48 (NCI-H1573, Panc 03.27, …) | rises with dose | low cells (technical?) |
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | 1.19× | +3.1 | 0.23 | 6/48 (LS 180, LoVo, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | 1.28× | +3.1 | 0.23 | 15/45 (A498, NCI-H1573, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Benztropine (mesylate) (drug)]] 0.05 µM |  | 1.27× | +3.1 | 0.23 | 3/47 (SW480, HEC-1-A, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 5 µM |  | 1.28× | +3.0 | 0.23 | 10/45 (NCI-H23, RKO, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 9 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2341.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **0.534×** | -7.9 | 1e-12 | 29/44 (SW480, NCI-H23, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.554×** | -7.5 | 3e-11 | 33/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.577×** | -6.9 | 7e-10 | 28/48 (PANC-1, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.637×** | -5.7 | 2e-06 | 25/47 (SW1417, RKO, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.639×** | -5.7 | 2e-06 | 24/47 (RKO, SNU-423, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **0.737×** | -5.4 | 5e-06 | 26/48 (MIA PaCa-2, PANC-1, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.679×** | -4.9 | 8e-05 | 22/46 (SW480, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **0.716×** | -4.2 | 0.002 | 20/47 (NCI-H23, SHP-77, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.746×** | -3.7 | 0.013 | 13/47 (RPMI-7951, SHP-77, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.752×** | -3.6 | 0.018 | 15/48 (SW1417, HepG2/C3A, …) | all doses, stronger at high dose |  |
| [[Mebendazole (drug)]] 5 µM |  | **0.749×** | -3.5 | 0.023 | 9/48 (NCI-H23, RPMI-7951, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~56% of this change | **0.762×** | -3.3 | 0.045 | 17/40 (NCI-H23, LoVo, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.21 per unit of S-phase module lfc, -0.30 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2341. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 11.7 | 0 | 3 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.182× (z -12.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change |
| [[NCI-H23 (line)]] | alt | 16.1 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.141× (z -12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change |
| [[NCI-H460 (line)]] | wt | 11.2 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.177× (z -10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change |
| [[PANC-1 (line)]] | alt | 10.8 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.218× (z -10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change |
| [[SHP-77 (line)]] | alt | 15.7 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.187× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Gemfibrozil (drug)]] 0.5 µM 0.212× (z -8.5) |
| [[HCT15 (line)]] | alt | 17.5 | 0 | 1 | — | [[Canagliflozin (drug)]] 0.05 µM 0.0813× (z -10.9) |
| [[HT-29 (line)]] | alt | 12.0 | 0 | 1 (1 ⚠) | — | [[TAK-901 (drug)]] 5 µM 0.0470× (z -9.3) ⚠ cell-cycle shift, explains ~38% of this change |
| [[J82 (line)]] | alt | 13.9 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.221× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change |
| [[LoVo (line)]] | wt | 11.3 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.240× (z -9.0) ⚠ toxic; cell-cycle shift, explains ~56% of this change |
| [[NCI-H1792 (line)]] | alt | 16.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.158× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[RPMI-7951 (line)]] | alt | 12.4 | 0 | 1 | — | [[Orlistat (drug)]] 0.05 µM 0.0664× (z -11.2) |
| [[SNU-423 (line)]] | alt | 12.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.120× (z -10.2) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 13.3 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.217× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change |
| [[A-172 (line)]] | wt | 12.0 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 12.8 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 8.03 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 10.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 9.79 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 6.40 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 15.1 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 8.31 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 6.89 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 11.3 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 9.23 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 14.1 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 7.82 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 8.15 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 9.42 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 20.8 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 6.10 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 8.91 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 14.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 13.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 7.70 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 8.47 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2341), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*79 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF507]] | +0.76 | +0.75 / +0.58 | both halves | 7e-06 |  |
| [[DNAJC11]] | +0.75 | +0.76 / +0.59 | both halves | 7e-06 |  |
| [[TMEM128]] | +0.74 | +0.71 / +0.65 | both halves | 7e-06 |  |
| [[PSME3IP1]] | +0.73 | +0.72 / +0.55 | both halves | 1e-05 |  |
| [[PEF1]] | +0.73 | +0.72 / +0.48 | both halves | 2e-05 |  |
| [[GATB]] | +0.72 | +0.73 / +0.61 | both halves | 7e-06 |  |
| [[KICS2]] | +0.72 | +0.75 / +0.47 | both halves | 2e-05 |  |
| [[MRRF]] | +0.71 | +0.64 / +0.66 | both halves | 7e-06 |  |
| [[ZXDA]] | +0.71 | +0.64 / +0.54 | both halves | 1e-05 |  |
| [[INTS14]] | +0.71 | +0.71 / +0.50 | both halves | 1e-05 |  |
| [[ZSCAN29]] | +0.71 | +0.73 / +0.47 | both halves | 2e-05 |  |
| [[CLHC1]] | +0.70 | +0.69 / +0.37 | both halves | 7e-05 |  |

## Genes that move opposite

*21 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CARHSP1]] | -0.71 | -0.59 / -0.59 | both halves | 7e-06 |  |
| [[GMCL1]] | -0.69 | -0.65 / -0.52 | both halves | 1e-05 |  |
| [[GNB2]] | -0.68 | -0.66 / -0.40 | both halves | 4e-05 |  |
| [[RPS6KA5]] | -0.67 | -0.62 / -0.52 | both halves | 1e-05 |  |
| [[PCMT1]] | -0.67 | -0.62 / -0.40 | both halves | 4e-05 |  |
| [[CBFA2T2]] | -0.66 | -0.68 / -0.40 | both halves | 4e-05 |  |
| [[TNNI3]] | -0.65 | -0.41 / -0.61 | both halves | 4e-05 |  |
| [[IGSF8]] | -0.65 | -0.62 / -0.40 | both halves | 5e-05 |  |
| [[DNAAF3]] | -0.65 | -0.44 / -0.52 | both halves | 3e-05 |  |
| [[CARD19]] | -0.65 | -0.51 / -0.58 | both halves | 1e-05 |  |
| [[SLC27A1]] | -0.65 | -0.53 / -0.50 | both halves | 1e-05 |  |
| [[KIAA1958]] | -0.64 | -0.56 / -0.51 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF613]] | B | ZNF613 activity raises MTHFSD's level | lines that do not express ZNF613 (7) vs lines expressing it (43) | 1.19× lower at baseline in the lines without ZNF613 | 0.052 | ⚠ within organs, on part of the lines; also absent: ZNF850, ENSG00000283201, ZNF571 |
| [[NRTN]] | C | NRTN activity raises MTHFSD's level | lines that do not express NRTN (4) vs lines expressing it (46) | 1.43× lower at baseline in the lines without NRTN | 0.0999 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: FOXRED2, ATP11A, BRME1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 135]]; 35 genes; this gene is in the **+** arm (projection on the module's main direction 0.747). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.39).
- **Nodal map** (x, y) = (-18.1, 7.0); signed map (9.4, -30.5). **Vector** length 65.0, 10.1% of its response variance represented; |z| ≥ 3 in 925 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.7 | +3.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.1 | +2.1 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +4.1 | +1.1 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.3 | +0.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +2.7 | +0.6 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.3 | +1.4 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.1 | +3.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.0 | +2.7 |
|  | [[Amsacrine (drug)]] 5 µM |  | +1.3 | +1.3 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -5.0 | -5.4 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~25% of this change | -3.9 | -3.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.7 | -2.6 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | -3.6 | -5.7 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | -3.5 | -6.9 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.1 | -1.9 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.2 | -0.4 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -1.1 | -1.3 |
|  | [[Cyclosporin A (drug)]] 0.05 µM |  | -1.1 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | methenyltetrahydrofolate synthetase domain containing |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16q24.1 — chr16:86,530,178-86,555,235 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ12998 |
| Gene groups (HGNC) | RNA binding motif containing |
| Matched by | ensembl_id |

UniProt [Q2M296](https://www.uniprot.org/uniprotkb/Q2M296) carries no function annotation.

**Summary**, from NCBI Gene [64779](https://www.ncbi.nlm.nih.gov/gene/64779):

> Enables RNA binding activity. Predicted to be active in cytoplasm. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:25778](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25778) · Entrez [64779](https://www.ncbi.nlm.nih.gov/gene/64779) · UniProt [Q2M296](https://www.uniprot.org/uniprotkb/Q2M296) · Ensembl [ENSG00000103248](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000103248)

## Data

Gene col 2341: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2341); `tables/drug_effects.parquet` (18 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2341, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2341]; `tensor/DDL_lfc|DDL_z.npy` [2341]; `embed/gene_vectors.npy` [2341]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2341 or target_col == 2341). Every well: [[MTHFSD — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MTHFSD.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
