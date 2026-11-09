---
symbol: "RAP2A"
type: "gene"
col: 4597
ensembl_id: "ENSG00000125249"
name: "RAP2A, member of RAS oncogene family"
location: "13q32.1"
module: 99
arm: "+"
pooled_cpm: 39.8
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 4
n_dd_up_clean: 7
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/099"]
generated_by: "tahoemap"
---

# RAP2A

*RAP2A, member of RAS oncogene family* — 13q32.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (1 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 1.46× (z +10.8, q 1e-24, up in 34 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.679× (z -15.8, q 0e+00, down in 35 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TMEM65]] (+0.61, fdr 1e-05), [[GNB2]] (+0.60, fdr 1e-05), [[CTXN1]] (+0.59, fdr 1e-04); moves opposite to [[GABPB2]] (-0.62, fdr 5e-05), [[TTC27]] (-0.61, fdr 2e-05), [[TXNRD2]] (-0.58, fdr 9e-05).
> It is in [[Module 099]], a single-armed module (hypoxia).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[ECHDC2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 6 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4597.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **1.46×** | +10.8 | 1e-24 | 34/48 (PANC-1, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.32×** | +8.0 | 3e-13 | 26/48 (HT-29, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~5% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.32×** | +8.0 | 3e-13 | 31/48 (SW480, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.21×** | +7.9 | 6e-13 | 21/48 (Hs 766T, SW1417, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.29×** | +7.3 | 4e-11 | 22/48 (HT-29, SW480, …) | all doses, flat | cell-cycle shift (explains ~4% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.07× | +6.6 | 3e-09 | 0/49 | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.25×** | +6.4 | 9e-09 | 21/48 (PANC-1, HT-29, …) | all doses, flat | cell-cycle shift (explains ~6% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.53×** | +6.4 | 1e-08 | 19/48 (HT-29, Panc 03.27, …) | top dose only | plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~10% of this change | **1.22×** | +5.5 | 2e-06 | 23/47 (PANC-1, J82, …) | top dose only | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~3% of this change | 1.16× | +4.0 | 0.003 | 15/46 (COLO 205, LS 180, …) | top dose only |  |
| [[Neratinib (maleate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.15× | +3.9 | 0.004 | 11/48 (SW1417, hTERT-HPNE, …) | two highest doses |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 1.13× | +3.4 | 0.028 | 6/47 (SW480, SHP-77, …) | inconsistent across doses | low cells (technical?) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~8% of this change | 1.13× | +3.4 | 0.029 | 8/48 (LS 180, HOP62, …) | top dose only |  |
| [[Roxadustat (drug)]] 5 µM |  | 1.13× | +3.3 | 0.040 | 4/47 (C32, HOP62, …) | top dose only |  |
| [[Trifluridine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~11% of this change | 1.11× | +3.1 | 0.074 | 4/48 (SW480, PANC-1, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 2 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 4597.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.679×** | -15.8 | 0e+00 | 35/47 (A-427, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.604×** | -14.0 | 4e-42 | 34/48 (NCI-H1573, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.655×** | -12.2 | 5e-32 | 35/47 (NCI-H1573, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.760×** | -7.9 | 3e-13 | 24/48 (NCI-H1573, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belumosudil (drug)]] 5 µM |  | 0.860× | -4.2 | 0.003 | 12/48 (C-33 A, SW480, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~3% of this change | 0.879× | -3.7 | 0.017 | 11/48 (NCI-H1573, SW 900, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~21% of this change | 0.892× | -3.3 | 0.074 | 13/48 (SW 1271, HCT15, …) | two highest doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.03 per unit of S-phase module lfc, +0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4597. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 79.3 | 0 | 8 (4 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.240× (z -17.3) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.249× (z -16.8) |
| [[A-172 (line)]] | wt | 60.3 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.342× (z -16.9) |
| [[LOX-IMVI (line)]] | wt | 51.9 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.338× (z -16.7) |
| [[PANC-1 (line)]] | alt | 29.5 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.11× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Belinostat (drug)]] 5 µM 2.01× (z +8.5) | — |
| [[A-427 (line)]] | wt | 30.4 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.127× (z -27.3) |
| [[AsPC-1 (line)]] | alt | 27.2 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.439× (z -9.4) |
| [[HOP62 (line)]] | alt | 35.7 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.285× (z -20.6) |
| [[Panc 03.27 (line)]] | alt | 39.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.474× (z -10.3) |
| [[SHP-77 (line)]] | alt | 183 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.324× (z -17.5) |
| [[A498 (line)]] | wt | 30.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.01× (z +9.0) | — |
| [[AN3 CA (line)]] | alt | 37.8 | 0 | 1 | — | [[Bentamapimod (drug)]] 0.05 µM 0.128× (z -8.9) |
| [[BT-474 (line)]] | alt | 22.4 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.268× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[C32 (line)]] | wt | 82.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.455× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HCT15 (line)]] | alt | 37.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.112× (z -14.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[Hs 766T (line)]] | wt | 55.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.81× (z +8.6) | — |
| [[HS-578T (line)]] | alt | 30.1 | 0 | 1 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.175× (z -8.6) ⚠ toxic |
| [[J82 (line)]] | alt | 75.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.584× (z -9.8) |
| [[NCI-H1792 (line)]] | alt | 26.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.288× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H2030 (line)]] | alt | 11.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.278× (z -10.9) |
| [[NCI-H23 (line)]] | alt | 25.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.420× (z -9.8) |
| [[RKO (line)]] | wt | 26.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.358× (z -11.2) |
| [[SW1417 (line)]] | alt | 19.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.16× (z +8.6) | — |
| [[SW480 (line)]] | alt | 72.1 | 0 | 1 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.311× (z -9.5) ⚠ toxic |
| [[A549 (line)]] | wt | 26.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 29.2 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 20.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 41.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 59.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 26.2 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 30.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 33.5 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 45.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 41.8 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 36.3 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 25.1 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 33.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 40.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 27.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 48.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 35.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 37.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 32.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 40.9 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 43.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 36.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 50.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 28.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 27.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4597), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*64 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM65]] | +0.61 | +0.62 / +0.52 | both halves | 1e-05 |  |
| [[GNB2]] | +0.60 | +0.51 / +0.56 | both halves | 1e-05 |  |
| [[CTXN1]] | +0.59 | +0.53 / +0.36 | both halves | 1e-04 |  |
| [[SNX25]] | +0.59 | +0.60 / +0.44 | both halves | 3e-05 |  |
| [[PLEKHA8]] | +0.59 | +0.60 / +0.49 | both halves | 1e-05 |  |
| [[WRNIP1]] | +0.58 | +0.61 / +0.46 | both halves | 3e-05 |  |
| [[IGSF8]] | +0.58 | +0.56 / +0.41 | both halves | 4e-05 |  |
| [[PDXP]] | +0.58 | +0.55 / +0.44 | both halves | 3e-05 |  |
| [[ALKBH5]] | +0.58 | +0.49 / +0.55 | both halves | 1e-05 |  |
| [[HDAC3]] | +0.58 | +0.54 / +0.45 | both halves | 3e-05 |  |
| [[TSPAN17]] | +0.57 | +0.52 / +0.50 | both halves | 1e-05 |  |
| [[MOSPD3]] | +0.57 | +0.58 / +0.45 | both halves | 3e-05 |  |

## Genes that move opposite

*36 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GABPB2]] | -0.62 | -0.64 / -0.39 | both halves | 5e-05 |  |
| [[TTC27]] | -0.61 | -0.62 / -0.47 | both halves | 2e-05 |  |
| [[TXNRD2]] | -0.58 | -0.59 / -0.37 | both halves | 9e-05 |  |
| [[YJU2]] | -0.55 | -0.56 / -0.29 | both halves | 2e-04 |  |
| [[ZC3HC1]] | -0.55 | -0.60 / -0.35 | both halves | 1e-04 |  |
| [[GCFC2]] | -0.55 | -0.54 / -0.44 | both halves | 3e-05 |  |
| [[GPATCH4]] | -0.55 | -0.58 / -0.42 | both halves | 4e-05 |  |
| [[RPL7L1]] | -0.54 | -0.58 / -0.37 | both halves | 7e-05 |  |
| [[PYM1]] | -0.54 | -0.50 / -0.38 | both halves | 6e-05 |  |
| [[OCIAD1]] | -0.53 | -0.51 / -0.42 | both halves | 4e-05 |  |
| [[METTL18]] | -0.53 | -0.55 / -0.40 | both halves | 5e-05 |  |
| [[LINC00174]] | -0.53 | -0.53 / -0.46 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ECHDC2]] | B | ECHDC2 activity lowers RAP2A's level | lines that do not express ECHDC2 (12) vs lines expressing it (38) | 1.29× higher at baseline in the lines without ECHDC2 | 0.047 | ⚠ within organs, on part of the lines; also absent: STXBP2, C10orf88B |
| [[HDAC6]] | B | HDAC6 activity lowers RAP2A's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 099]] — hypoxia; 48 genes; every member is in the + arm (projection on the module's main direction 0.598). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.29; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-14.8, 7.8); signed map (-36.8, 15.8). **Vector** length 94.1, 19.1% of its response variance represented; |z| ≥ 3 in 952 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 0.5 µM |  | +5.2 | +8.0 |
|  | [[Belinostat (drug)]] 5 µM |  | +5.0 | +10.8 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +3.5 | +7.3 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +3.5 | +6.4 |
|  | [[Panobinostat (drug)]] 5 µM |  | +3.4 | +8.0 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +2.5 | +3.4 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.4 | +6.4 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.2 | +1.8 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +2.1 | +0.9 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +2.0 | +1.6 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -7.0 | -12.2 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -6.8 | -15.8 |
|  | [[Harringtonine (drug)]] 5 µM |  | -5.9 | -14.0 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -3.7 | -7.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.5 | -2.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.1 | +2.2 |
|  | [[Lactate (calcium) (drug)]] 0.5 µM |  | -1.6 | -2.7 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.6 | -4.2 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | -1.5 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | RAP2A, member of RAS oncogene family |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 13q32.1 — chr13:97,434,169-97,469,128 (+) |
| Ensembl biotype | protein_coding |
| Also known as | K-REV; previously RAP2 |
| Gene groups (HGNC) | RAS type GTPase family |
| Matched by | ensembl_id |

**Function**, from UniProt [P10114](https://www.uniprot.org/uniprotkb/P10114) (Ras-related protein Rap-2a):

> Small GTP-binding protein which cycles between a GDP-bound inactive and a GTP-bound active form. In its active form interacts with and regulates several effectors including MAP4K4, MINK1 and TNIK. Part of a signaling complex composed of NEDD4, RAP2A and TNIK which regulates neuronal dendrite extension and arborization during development. More generally, it is part of several signaling cascades and regulates cytoskeletal rearrangements, cell migration, cell adhesion and cell spreading.

**Summary**, from NCBI Gene [5911](https://www.ncbi.nlm.nih.gov/gene/5911):

> Enables G protein activity; guanyl ribonucleotide binding activity; and magnesium ion binding activity. Involved in several processes, including regulation of JNK cascade; regulation of plasma membrane bounded cell projection organization; and regulation of synapse assembly. Acts upstream of or within establishment of protein localization. Located in Golgi apparatus; endosome; and lamellipodium membrane. Is active in Schaffer collateral - CA1 synapse. [provided by Alliance of Genome Resources, …

**Accessions** — [HGNC:9861](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9861) · Entrez [5911](https://www.ncbi.nlm.nih.gov/gene/5911) · UniProt [P10114](https://www.uniprot.org/uniprotkb/P10114) · Ensembl [ENSG00000125249](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000125249)

## Data

Gene col 4597: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4597); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4597, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4597]; `tensor/DDL_lfc|DDL_z.npy` [4597]; `embed/gene_vectors.npy` [4597]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4597 or target_col == 4597). Every well: [[RAP2A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RAP2A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
