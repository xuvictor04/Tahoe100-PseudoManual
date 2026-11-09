---
symbol: "FBXL14"
type: "gene"
col: 10168
ensembl_id: "ENSG00000171823"
name: "F-box and leucine rich repeat protein 14"
location: "12p13.33"
module: 89
arm: "+"
pooled_cpm: 11.22
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 8
n_dd_up_clean: 7
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/089"]
generated_by: "tahoemap"
---

# FBXL14

*F-box and leucine rich repeat protein 14* — 12p13.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (3 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 2.84× (z +15.5, q 0e+00, up in 39 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (2 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.599× (z -7.6, q 1e-11, down in 21 of 47 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZIC2]] (+0.59, fdr 9e-06), [[ZKSCAN4]] (+0.56, fdr 1e-05), [[BCOR]] (+0.54, fdr 3e-05); moves opposite to [[WDR59]] (-0.45, fdr 3e-05), [[AP2B1]] (-0.45, fdr 3e-05), [[TMTC3]] (-0.44, fdr 5e-04).
> It is in [[Module 089]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[PSMB5]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 4 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10168.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **2.84×** | +15.5 | 0e+00 | 39/47 (A-427, A-172, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.64×** | +10.4 | 5e-23 | 27/46 (HEC-1-A, A549, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.50×** | +6.0 | 4e-07 | 19/38 (KATO III, SW1417, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~25% here); position effect removed |
| [[Ponatinib (drug)]] 5 µM |  | **1.31×** | +4.0 | 0.009 | 9/47 (HOP62, KATO III, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.21×** | +3.9 | 0.009 | 7/48 (NCI-H2347, NCI-H460, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.30×** | +3.9 | 0.010 | 7/47 (NCI-H2347, A-172, …) | inconsistent across doses | cell-cycle shift (explains ~7% here) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.27×** | +3.5 | 0.034 | 14/45 (hTERT-HPNE, HOP62, …) | all doses, flat |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | 1.18× | +3.5 | 0.037 | 10/48 (LOX-IMVI, NCI-H23, …) | rises with dose | position effect removed |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.28×** | +3.4 | 0.037 | 9/45 (SW48, MIA PaCa-2, …) | inconsistent across doses | low cells (technical?) |
| [[Nimesulide (drug)]] 5 µM | ⚠ toxic; unreliable plate only | **1.24×** | +3.2 | 0.087 | 12/46 (SW480, RKO, …) | top dose only |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.24×** | +3.1 | 0.094 | 9/47 (MIA PaCa-2, NCI-H1792, …) | top dose only |  |
| [[Carbamazepine (drug)]] 5 µM |  | 1.23× | +3.1 | 0.11 | 6/47 (LOX-IMVI, SW 900, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 2 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10168.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.599×** | -7.6 | 1e-11 | 21/47 (NCI-H460, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.613×** | -7.3 | 1e-10 | 28/47 (NCI-H2030, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.679×** | -5.8 | 1e-06 | 21/44 (SW 900, C-33 A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.665×** | -5.7 | 1e-06 | 22/46 (H4, NCI-H1792, …) | inconsistent across doses | cell-cycle shift (explains ~20% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.690×** | -5.5 | 4e-06 | 19/47 (SW 900, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.704×** | -5.2 | 2e-05 | 22/47 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.750×** | -4.3 | 0.002 | 17/47 (BT-474, SK-MEL-2, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.778×** | -3.7 | 0.013 | 9/46 (J82, A-427, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.02 per unit of S-phase module lfc, +0.22 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10168. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 17.0 | 1 | 2 (1 ⚠) | [[Auranofin (drug)]] 5 µM 4.67× (z +10.1) | [[HI-TOPK-032 (drug)]] 0.05 µM 0.182× (z -10.5) |
| [[SW 900 (line)]] | alt | 16.3 | 1 | 2 (1 ⚠) | [[Auranofin (drug)]] 5 µM 4.52× (z +8.6) | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0989× (z -13.1) |
| [[HOP62 (line)]] | alt | 13.8 | 1 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 3.98× (z +9.1) | [[Dinaciclib (drug)]] 5 µM 0.0672× (z -17.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H23 (line)]] | alt | 29.0 | 1 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 5.46× (z +12.2) | [[Dinaciclib (drug)]] 0.05 µM 0.220× (z -10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change |
| [[NCI-H460 (line)]] | wt | 12.5 | 0 | 2 | — | [[Digitoxin (drug)]] 0.5 µM 0.274× (z -9.5) |
| [[RKO (line)]] | wt | 11.6 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.108× (z -9.7) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 6.29 | 1 | 0 | [[Auranofin (drug)]] 5 µM 13.1× (z +12.8) | — |
| [[A-427 (line)]] | wt | 28.7 | 1 | 0 | [[Auranofin (drug)]] 5 µM 7.37× (z +14.3) | — |
| [[A549 (line)]] | wt | 7.28 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.78× (z +8.5) | — |
| [[C-33 A (line)]] | alt | 14.0 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.105× (z -10.2) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 10.3 | 0 | 1 | — | [[Bortezomib (drug)]] 0.05 µM 0.0820× (z -8.6) |
| [[HEC-1-A (line)]] | alt | 14.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.42× (z +9.2) | — |
| [[Hs 766T (line)]] | wt | 6.26 | 0 | 1 | — | [[LY-2584702 (tosylate salt) (drug)]] 0.05 µM 0.0750× (z -8.8) |
| [[HT-29 (line)]] | alt | 8.94 | 1 | 0 | [[Auranofin (drug)]] 5 µM 7.08× (z +9.5) | — |
| [[LoVo (line)]] | wt | 12.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.139× (z -11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change |
| [[LS 180 (line)]] | wt | 11.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.193× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change |
| [[NCI-H1792 (line)]] | alt | 8.49 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.154× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[Panc 03.27 (line)]] | alt | 17.0 | 1 | 0 | [[Auranofin (drug)]] 5 µM 4.91× (z +9.6) | — |
| [[SW48 (line)]] | wt | 8.95 | 0 | 1 | — | [[Decitabine (drug)]] 5 µM 0.0719× (z -8.6) |
| [[SW480 (line)]] | alt | 14.4 | 1 | 0 | [[Auranofin (drug)]] 5 µM 3.81× (z +10.5) | — |
| [[A498 (line)]] | wt | 7.62 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.03 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 7.59 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 13.7 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.98 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 6.96 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 7.53 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 9.24 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 7.55 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 4.59 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 9.03 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 16.6 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 7.30 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.77 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 7.81 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 9.63 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 9.88 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 5.94 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 8.95 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 7.15 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 8.97 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 21.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 9.91 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10168), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZIC2]] | +0.59 | +0.57 / +0.59 | both halves | 9e-06 |  |
| [[ZKSCAN4]] | +0.56 | +0.59 / +0.53 | both halves | 1e-05 |  |
| [[BCOR]] | +0.54 | +0.60 / +0.44 | both halves | 3e-05 |  |
| [[ZBTB2]] | +0.53 | +0.64 / +0.48 | both halves | 2e-05 |  |
| [[TMEM223]] | +0.50 | +0.34 / +0.59 | both halves | 1e-04 |  |
| [[SURF6]] | +0.50 | +0.62 / +0.44 | both halves | 3e-05 |  |
| [[RSBN1]] | +0.49 | +0.28 / +0.57 | both halves | 3e-04 |  |
| [[PIK3R1]] | +0.48 | +0.46 / +0.49 | both halves | 3e-05 |  |
| [[ABT1]] | +0.48 | +0.55 / +0.40 | both halves | 4e-05 |  |
| [[RUNDC1]] | +0.48 | +0.47 / +0.44 | both halves | 3e-05 |  |
| [[PURA]] | +0.48 | +0.40 / +0.55 | both halves | 5e-05 |  |
| [[TMEM186]] | +0.48 | +0.50 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[WDR59]] | -0.45 | -0.48 / -0.45 | both halves | 3e-05 |  |
| [[AP2B1]] | -0.45 | -0.51 / -0.43 | both halves | 3e-05 |  |
| [[TMTC3]] | -0.44 | -0.24 / -0.44 | both halves | 5e-04 |  |
| [[TPMT]] | -0.43 | -0.36 / -0.43 | both halves | 9e-05 |  |
| [[MAGT1]] | -0.43 | -0.38 / -0.40 | both halves | 7e-05 |  |
| [[CA5B]] | -0.42 | -0.47 / -0.37 | both halves | 7e-05 |  |
| [[NAP1L4]] | -0.42 | -0.52 / -0.37 | both halves | 9e-05 |  |
| [[ODF2L]] | -0.42 | -0.12 / -0.56 | ⚠ one half (not replicated) | 0.002 |  |
| [[DYNC1LI2]] | -0.41 | -0.23 / -0.51 | both halves | 5e-04 |  |
| [[RTN3]] | -0.41 | -0.52 / -0.25 | both halves | 4e-04 |  |
| [[RAB22A]] | -0.41 | -0.61 / -0.35 | both halves | 1e-04 |  |
| [[IQGAP1]] | -0.39 | -0.52 / -0.33 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PSMB5]] | B | PSMB5 activity raises FBXL14's level | compounds that target PSMB5: 2 of 2 lower it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 089]]; 51 genes; every member is in the + arm (projection on the module's main direction 0.217). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-46.0, 7.4); signed map (-5.7, -19.2). **Vector** length 69.2, 11.1% of its response variance represented; |z| ≥ 3 in 813 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +8.5 | +15.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | +3.6 | +3.5 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +2.8 | +2.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.4 | +2.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.3 | +0.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.8 | +4.0 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.6 | +1.1 |
| fall | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | -6.4 | -2.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | -6.2 | -1.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | -4.2 | +2.0 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -3.3 | -7.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.1 | -4.3 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -1.1 | +0.6 |
|  | [[EX229 (drug)]] 5 µM |  | -1.0 | -1.2 |
|  | [[TAK-733 (drug)]] 0.05 µM |  | -0.9 | -2.4 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -0.8 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | F-box and leucine rich repeat protein 14 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12p13.33 — chr12:1,565,993-1,594,581 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MGC40195, Fbl14 |
| Gene groups (HGNC) | F-box and leucine rich repeat proteins |
| Reactome | 4 pathways, smallest: Neddylation; Antigen processing: Ubiquitination & Proteasome degradation; Class I MHC mediated antigen processing & presentation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8N1E6](https://www.uniprot.org/uniprotkb/Q8N1E6) (F-box/LRR-repeat protein 14):

> Substrate-recognition component of some SCF (SKP1-CUL1-F-box protein)-type E3 ubiquitin-protein ligase complexes. The SCF(FBXL14) complex acts by mediating ubiquitination and subsequent degradation of SNAI1.

**Summary**, from NCBI Gene [144699](https://www.ncbi.nlm.nih.gov/gene/144699):

> Members of the F-box protein family, such as FBXL14, are characterized by an approximately 40-amino acid F-box motif. SCF complexes, formed by SKP1 (MIM 601434), cullin (see CUL1; MIM 603134), and F-box proteins, act as protein-ubiquitin ligases. F-box proteins interact with SKP1 through the F box, and they interact with ubiquitination targets through other protein interaction domains (Jin et al., 2004 [PubMed 15520277]).[supplied by OMIM, Mar 2008]

**Accessions** — [HGNC:28624](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28624) · Entrez [144699](https://www.ncbi.nlm.nih.gov/gene/144699) · UniProt [Q8N1E6](https://www.uniprot.org/uniprotkb/Q8N1E6) · Ensembl [ENSG00000171823](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000171823)

## Data

Gene col 10168: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10168); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10168, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10168]; `tensor/DDL_lfc|DDL_z.npy` [10168]; `embed/gene_vectors.npy` [10168]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10168 or target_col == 10168). Every well: [[FBXL14 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FBXL14.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
