---
symbol: "BCKDK"
type: "gene"
col: 2376
ensembl_id: "ENSG00000103507"
name: "branched chain keto acid dehydrogenase kinase"
location: "16p11.2"
module: 50
arm: "+"
pooled_cpm: 11.26
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 16
n_dd_up_clean: 3
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/050"]
generated_by: "tahoemap"
---

# BCKDK

*branched chain keto acid dehydrogenase kinase* — 16p11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (3 with an alert ⚠); the strongest is [[Adagrasib (drug)]] 0.05 µM: 1.22× (z +7.6, q 2e-11, up in 20 of 48 measured lines) ⚠ position not correctable. The strongest without an alert is [[Selinexor (drug)]] 5 µM: 1.44× (z +5.8, q 1e-06, up in 22 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.305× (z -18.8, q 0e+00, down in 44 of 47 measured lines).
> Its strongest partners by |cos| (93 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 7 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MPI]] (+0.72, fdr 7e-06), [[TTLL12]] (+0.68, fdr 1e-05), [[PHB1]] (+0.66, fdr 9e-06); moves opposite to [[BORCS7-ASMT]] (-0.63, fdr 4e-05), [[MAFG]] (-0.61, fdr 5e-05), [[MIA]] (-0.60, fdr 4e-05).
> It is in [[Module 050]], a single-armed module (Extracellular matrix organization).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[ZNF785]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 3 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2376.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | **1.22×** | +7.6 | 2e-11 | 20/48 (HEC-1-A, PANC-1, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.87×** | +6.7 | 5e-09 | 13/22 (HEC-1-A, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift; position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **1.44×** | +5.8 | 1e-06 | 22/48 (A498, MIA PaCa-2, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.60×** | +5.2 | 2e-05 | 22/36 (A498, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift; position effect removed |
| [[Megestrol (drug)]] 0.05 µM |  | **1.37×** | +3.5 | 0.056 | 12/48 (A498, Panc 03.27, …) | inconsistent across doses | cell-cycle shift (explains ~11% here) |
| [[Omeprazole (drug)]] 0.05 µM |  | **1.35×** | +3.4 | 0.068 | 4/48 (NCI-H460, SNU-423, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 1 with an alert ⚠. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2376.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.305×** | -18.8 | 0e+00 | 44/47 (MIA PaCa-2, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.401×** | -14.5 | 7e-45 | 44/45 (MIA PaCa-2, J82, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.361×** | -11.4 | 1e-27 | 34/46 (LoVo, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.404×** | -10.1 | 6e-22 | 40/48 (NCI-H23, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.429×** | -9.5 | 4e-19 | 39/46 (A-427, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.486×** | -8.1 | 7e-14 | 33/45 (RPMI-7951, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.517×** | -7.4 | 1e-11 | 34/46 (A-427, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.549×** | -6.4 | 8e-09 | 28/45 (RPMI-7951, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.552×** | -6.4 | 1e-08 | 25/46 (MIA PaCa-2, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.622×** | -5.1 | 2e-05 | 26/47 (SK-MEL-2, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.652×** | -4.8 | 9e-05 | 27/47 (LS 180, J82, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.653×** | -4.8 | 9e-05 | 25/48 (SW 900, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.637×** | -4.5 | 3e-04 | 22/46 (SK-MEL-2, Hs 766T, …) | all doses, flat | cell-cycle shift (explains ~11% here); position effect removed |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.686×** | -4.2 | 1e-03 | 18/46 (NCI-H1792, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Glycyrrhizic acid (drug)]] 0.5 µM |  | **0.745×** | -3.3 | 0.038 | 17/46 (SNU-423, NCI-H2030, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[EX229 (drug)]] 5 µM |  | **0.578×** | -3.2 | 0.048 | 14/43 (SNU-1, HepG2/C3A, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.03 per unit of S-phase module lfc, +0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2376. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 22.9 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0978× (z -21.3) |
| [[NCI-H460 (line)]] | wt | 9.45 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.224× (z -12.6) |
| [[LS 180 (line)]] | wt | 10.0 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.150× (z -12.3) |
| [[NCI-H2030 (line)]] | alt | 16.2 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.208× (z -12.8) |
| [[A-427 (line)]] | wt | 15.2 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0481× (z -17.2) |
| [[AsPC-1 (line)]] | alt | 9.18 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.171× (z -10.2) |
| [[CFPAC-1 (line)]] | alt | 14.7 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.277× (z -10.7) |
| [[HEC-1-A (line)]] | alt | 12.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.312× (z -9.7) |
| [[J82 (line)]] | alt | 17.4 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.188× (z -13.5) |
| [[LoVo (line)]] | wt | 6.06 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0844× (z -11.7) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.187× (z -11.2) |
| [[NCI-H1573 (line)]] | alt | 6.89 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.144× (z -11.1) |
| [[NCI-H2347 (line)]] | alt | 5.11 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0927× (z -11.0) |
| [[RPMI-7951 (line)]] | alt | 13.5 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0486× (z -13.4) |
| [[A549 (line)]] | wt | 9.55 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.264× (z -8.7) |
| [[BT-474 (line)]] | alt | 13.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.157× (z -12.3) |
| [[COLO 205 (line)]] | alt | 7.91 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0544× (z -10.1) |
| [[H4 (line)]] | wt | 13.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.167× (z -9.1) |
| [[HCT15 (line)]] | alt | 23.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.156× (z -8.8) |
| [[HOP62 (line)]] | alt | 6.84 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.243× (z -9.1) |
| [[KATO III (line)]] | alt | 9.76 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.212× (z -10.7) |
| [[LOX-IMVI (line)]] | wt | 8.70 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.111× (z -14.7) |
| [[NCI-H23 (line)]] | alt | 9.06 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.105× (z -10.5) |
| [[Panc 03.27 (line)]] | alt | 6.41 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0528× (z -11.4) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 15.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.284× (z -13.1) |
| [[SK-MEL-2 (line)]] | alt | 12.6 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.113× (z -10.8) |
| [[A-172 (line)]] | wt | 14.4 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 14.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 6.92 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 11.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 8.66 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 10.4 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 9.75 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 7.89 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 12.0 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 8.95 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.77 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 9.85 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 8.99 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 14.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 18.2 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 8.70 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 7.71 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 7.15 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 11.5 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 6.45 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2376), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*54 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MPI]] | +0.72 | +0.66 / +0.73 | both halves | 7e-06 | pathway: Diseases of metabolism |
| [[TTLL12]] | +0.68 | +0.61 / +0.50 | both halves | 1e-05 |  |
| [[PHB1]] | +0.66 | +0.59 / +0.57 | both halves | 9e-06 |  |
| [[ECHS1]] | +0.64 | +0.47 / +0.48 | both halves | 2e-05 | pathway: Branched-chain amino acid catabolism; STRING 509 |
| [[KCTD17]] | +0.63 | +0.57 / +0.34 | both halves | 1e-04 |  |
| [[GPS1]] | +0.63 | +0.51 / +0.49 | both halves | 1e-05 |  |
| [[APEH]] | +0.61 | +0.55 / +0.45 | both halves | 3e-05 |  |
| [[RAB3D]] | +0.60 | +0.56 / +0.35 | both halves | 1e-04 |  |
| [[LDHA]] | +0.60 | +0.63 / +0.56 | both halves | 1e-05 |  |
| [[STUB1]] | +0.60 | +0.53 / +0.28 | both halves | 3e-04 |  |
| [[RPUSD1]] | +0.59 | +0.38 / +0.40 | both halves | 6e-05 |  |
| [[CANT1]] | +0.58 | +0.61 / +0.43 | both halves | 3e-05 |  |

## Genes that move opposite

*46 of its nearest partners move opposite, 5 of them with an alert (⚠; 5 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BORCS7-ASMT]] | -0.63 | -0.56 / -0.41 | both halves | 4e-05 |  |
| [[MAFG]] | -0.61 | -0.59 / -0.40 | both halves | 5e-05 |  |
| [[MIA]] | -0.60 | -0.54 / -0.42 | both halves | 4e-05 |  |
| [[ZNF460-AS1]] | -0.58 | -0.57 / -0.23 | both halves | 5e-04 |  |
| [[GALNT7-DT]] | -0.58 | -0.51 / -0.37 | both halves | 7e-05 |  |
| [[CASS4]] | -0.58 | -0.61 / -0.24 | both halves | 5e-04 |  |
| [[PSMD6-AS2]] | -0.57 | -0.48 / -0.34 | both halves | 1e-04 |  |
| [[KMT2E-AS1]] | -0.56 | -0.52 / -0.14 | ⚠ one half (not replicated) | 0.002 |  |
| [[PNISR]] | -0.56 | -0.59 / -0.30 | both halves | 2e-04 |  |
| [[PPP1R12A-AS2]] | -0.56 | -0.50 / -0.33 | both halves | 1e-04 |  |
| [[GTF2IRD2]] | -0.56 | -0.48 / -0.26 | both halves | 4e-04 |  |
| [[TSTD3]] | -0.55 | -0.56 / -0.18 | ⚠ one half (not replicated) | 1e-03 |  |
| [[PABPN1]] | -0.55 | -0.49 / -0.45 | both halves | 3e-05 |  |
| [[UPP2]] | -0.55 | -0.50 / -0.37 | both halves | 9e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF785]] | B | ZNF785 activity lowers BCKDK's level | lines that do not express ZNF785 (9) vs lines expressing it (41) | 1.31× higher at baseline in the lines without ZNF785 | 0.060 | ⚠ within organs, on part of the lines; also absent: TNFRSF14, BDH1, PARP8 |
| [[TOP2A]] | B | TOP2A activity raises BCKDK's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 3.1% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 050]] — Extracellular matrix organization; 92 genes; every member is in the + arm (projection on the module's main direction 0.452). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.27; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-22.1, -27.3); signed map (-26.8, -44.3). **Vector** length 82.3, 16.9% of its response variance represented; |z| ≥ 3 in 894 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +5.3 | +1.5 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +4.9 | +0.2 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +4.8 | +1.3 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +3.8 | +0.0 |
|  | [[Selinexor (drug)]] 5 µM |  | +3.6 | +5.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.7 | -1.1 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.8 | +2.0 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +1.5 | +2.3 |
|  | [[Relugolix (drug)]] 0.5 µM |  | +1.3 | +1.7 |
|  | [[Sonidegib (drug)]] 0.5 µM |  | +1.3 | +2.0 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -6.9 | -14.5 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -3.6 | -18.8 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -3.6 | -6.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -3.4 | -9.5 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -3.2 | -5.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | -3.0 | -2.8 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.5 | -1.5 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | -2.3 | -0.7 |
|  | [[Bimiralisib (drug)]] 0.05 µM |  | -1.9 | -2.3 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.8 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | branched chain keto acid dehydrogenase kinase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16p11.2 — chr16:31,106,107-31,112,791 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Pyruvate dehydrogenase kinase family; Branched chain alpha-keto acid dehydrogenase complex subunits |
| Reactome | 5 pathways, smallest: Branched-chain ketoacid dehydrogenase kinase deficiency; Diseases of branched-chain amino acid catabolism; Branched-chain amino acid catabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [O14874](https://www.uniprot.org/uniprotkb/O14874) (Branched-chain alpha-ketoacid dehydrogenase kinase):

> Serine/threonine-protein kinase component of macronutrients metabolism. Forms a functional kinase and phosphatase pair with PPM1K, serving as a metabolic regulatory node that coordinates branched-chain amino acids (BCAAs) with glucose and lipid metabolism via two distinct phosphoprotein targets: mitochondrial BCKDHA subunit of the branched-chain alpha-ketoacid dehydrogenase (BCKDH) complex and cytosolic ACLY, a lipogenic enzyme of Krebs cycle. Phosphorylates and inactivates mitochondrial BCKDH …

**Summary**, from NCBI Gene [10295](https://www.ncbi.nlm.nih.gov/gene/10295):

> The branched-chain alpha-ketoacid dehydrogenase complex (BCKD) is an important regulator of the valine, leucine, and isoleucine catabolic pathways. The protein encoded by this gene is found in the mitochondrion, where it phosphorylates and inactivates BCKD. Several transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Dec 2012]

**Accessions** — [HGNC:16902](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16902) · Entrez [10295](https://www.ncbi.nlm.nih.gov/gene/10295) · UniProt [O14874](https://www.uniprot.org/uniprotkb/O14874) · Ensembl [ENSG00000103507](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000103507)

## Data

Gene col 2376: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2376); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2376, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2376]; `tensor/DDL_lfc|DDL_z.npy` [2376]; `embed/gene_vectors.npy` [2376]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2376 or target_col == 2376). Every well: [[BCKDK — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BCKDK.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
