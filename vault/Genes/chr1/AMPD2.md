---
symbol: "AMPD2"
type: "gene"
col: 3790
ensembl_id: "ENSG00000116337"
name: "adenosine monophosphate deaminase 2"
location: "1p13.3"
module: 42
arm: "+"
pooled_cpm: 18.35
n_lines_expressing: 49
n_dd_up: 0
n_dd_down: 14
n_dd_up_clean: 0
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/042"]
generated_by: "tahoemap"
---

# AMPD2

*adenosine monophosphate deaminase 2* — 1p13.3

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 1 line (A498 2.70×).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.497× (z -12.4, q 2e-32, down in 36 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DDB1]] (+0.69, fdr 7e-06), [[MLF2]] (+0.65, fdr 1e-05), [[P3H1]] (+0.64, fdr 1e-05); moves opposite to [[RNF115]] (-0.66, fdr 1e-05), [[TLK1]] (-0.64, fdr 3e-05), [[UBXN2A]] (-0.62, fdr 4e-05).
> It is in [[Module 042]], a single-armed module (UPR ER).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[MARVELD3]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 2 with an alert ⚠. 0 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3790.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 1 line (A498 2.70×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | 1.23× | +3.7 | 0.11 | 12/47 (RPMI-7951, HOP62, …) | inconsistent across doses | position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | 1.34× | +3.6 | 0.11 | 9/26 (NCI-H1792, A498, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | 1.31× | +3.4 | 0.15 | 15/38 (A498, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Pentoxifylline (drug)]] 5 µM |  | 1.29× | +3.2 | 0.18 | 11/47 (HOP62, A498, …) | rises with dose | position effect removed |
| [[L-Thyroxine (sodium salt pentahydrate) (drug)]] 5 µM |  | 1.29× | +3.1 | 0.19 | 14/47 (J82, HepG2/C3A, …) | rises with dose | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 1 with an alert ⚠. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3790.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.497×** | -12.4 | 2e-32 | 36/46 (RKO, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.469×** | -9.1 | 3e-17 | 35/46 (RKO, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.498×** | -8.7 | 5e-16 | 29/45 (RKO, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.606×** | -6.3 | 5e-08 | 28/46 (RKO, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.619×** | -6.0 | 2e-07 | 26/45 (H4, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.671×** | -4.8 | 1e-04 | 20/45 (HOP62, AN3 CA, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.699×** | -4.5 | 6e-04 | 21/47 (SNU-1, KATO III, …) | rises with dose | cell-cycle shift (explains ~3% here); composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.781×** | -4.4 | 9e-04 | 22/45 (RPMI-7951, H4, …) | rises with dose | cell-cycle shift (explains ~1% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.733×** | -3.9 | 0.007 | 20/47 (RKO, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.756×** | -3.5 | 0.026 | 15/46 (HOP62, A498, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Allantoin (drug)]] 5 µM |  | **0.828×** | -3.3 | 0.043 | 14/47 (HEC-1-A, HCT15, …) | top dose only | position effect removed |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **0.829×** | -3.3 | 0.043 | 15/47 (A498, SW 1271, …) | top dose only |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.769×** | -3.3 | 0.043 | 18/46 (AsPC-1, HOP62, …) | inconsistent across doses |  |
| [[Medroxyprogesterone acetate (drug)]] 5 µM |  | **0.832×** | -3.2 | 0.047 | 15/47 (NCI-H2347, HEC-1-A, …) | rises with dose | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.03 per unit of S-phase module lfc, -0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3790. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[RKO (line)]] | wt | 25.5 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.0894× (z -20.6) |
| [[MIA PaCa-2 (line)]] | alt | 28.1 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.276× (z -11.0) |
| [[HOP62 (line)]] | alt | 30.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.305× (z -12.4) |
| [[SW 900 (line)]] | alt | 16.7 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.211× (z -11.4) |
| [[A498 (line)]] | wt | 34.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.70× (z +12.1) | — |
| [[AsPC-1 (line)]] | alt | 8.95 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.124× (z -8.7) ⚠ transcription drop; cell-cycle shift, explains ~0% of this change |
| [[CFPAC-1 (line)]] | alt | 15.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.245× (z -11.6) |
| [[H4 (line)]] | wt | 36.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.225× (z -11.5) |
| [[HS-578T (line)]] | alt | 44.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.339× (z -11.5) |
| [[J82 (line)]] | alt | 23.3 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.287× (z -8.8) ⚠ toxic; cell-cycle shift, explains ~3% of this change |
| [[LOX-IMVI (line)]] | wt | 26.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.411× (z -8.9) |
| [[NCI-H2030 (line)]] | alt | 23.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.316× (z -11.4) |
| [[NCI-H23 (line)]] | alt | 39.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.387× (z -11.0) |
| [[NCI-H2347 (line)]] | alt | 10.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.332× (z -9.3) |
| [[SW48 (line)]] | wt | 10.3 | 0 | 1 | — | [[Ivermectin (drug)]] 0.5 µM 0.0874× (z -8.6) |
| [[A-172 (line)]] | wt | 22.7 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 10.2 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 11.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.41 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 17.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 9.92 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 7.86 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 8.83 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 21.5 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 6.04 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 31.1 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 7.63 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 8.93 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 9.39 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 25.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 13.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 8.05 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 30.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 62.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 16.6 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 25.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 31.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 9.26 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 10.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3790), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*80 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DDB1]] | +0.69 | +0.68 / +0.64 | both halves | 7e-06 |  |
| [[MLF2]] | +0.65 | +0.64 / +0.56 | both halves | 1e-05 |  |
| [[P3H1]] | +0.64 | +0.63 / +0.57 | both halves | 1e-05 |  |
| [[EPN1]] | +0.64 | +0.61 / +0.53 | both halves | 1e-05 |  |
| [[RCN3]] | +0.63 | +0.50 / +0.56 | both halves | 1e-05 |  |
| [[B4GALT7]] | +0.62 | +0.67 / +0.52 | both halves | 1e-05 |  |
| [[P4HB]] | +0.62 | +0.64 / +0.54 | both halves | 1e-05 |  |
| [[SEC24C]] | +0.61 | +0.68 / +0.51 | both halves | 1e-05 |  |
| [[ARFGAP1]] | +0.61 | +0.65 / +0.49 | both halves | 2e-05 |  |
| [[CPSF1]] | +0.60 | +0.62 / +0.43 | both halves | 3e-05 |  |
| [[ABHD17A]] | +0.60 | +0.63 / +0.41 | both halves | 4e-05 |  |
| [[SEC61A1]] | +0.59 | +0.64 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

*20 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RNF115]] | -0.66 | -0.66 / -0.54 | both halves | 1e-05 |  |
| [[TLK1]] | -0.64 | -0.51 / -0.46 | both halves | 3e-05 |  |
| [[UBXN2A]] | -0.62 | -0.74 / -0.41 | both halves | 4e-05 |  |
| [[RDX]] | -0.61 | -0.62 / -0.50 | both halves | 1e-05 |  |
| [[SCAF11]] | -0.58 | -0.55 / -0.43 | both halves | 3e-05 |  |
| [[SETD2]] | -0.58 | -0.53 / -0.45 | both halves | 3e-05 |  |
| [[DCUN1D1]] | -0.57 | -0.58 / -0.46 | both halves | 3e-05 |  |
| [[HACD1]] | -0.57 | -0.64 / -0.33 | both halves | 1e-04 |  |
| [[ATAD2B]] | -0.55 | -0.54 / -0.38 | both halves | 6e-05 |  |
| [[ITSN2]] | -0.55 | -0.48 / -0.41 | both halves | 4e-05 |  |
| [[HSPBAP1]] | -0.54 | -0.57 / -0.39 | both halves | 6e-05 |  |
| [[CUX1]] | -0.54 | -0.55 / -0.34 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MARVELD3]] | B | MARVELD3 activity lowers AMPD2's level | lines that do not express MARVELD3 (28) vs lines expressing it (22) | 1.96× higher at baseline in the lines without MARVELD3 | 0.053 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CRB3, KDF1, ESRP2 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 042]] — UPR ER; 103 genes; every member is in the + arm (projection on the module's main direction 0.606). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (9.1, -25.8); signed map (-52.1, 2.2). **Vector** length 95.8, 20.6% of its response variance represented; |z| ≥ 3 in 884 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +4.1 | +0.0 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +3.6 | +2.8 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +3.6 | -0.8 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.3 | -0.2 |
|  | [[Abemaciclib (drug)]] 0.05 µM | ⚠ unreliable plate only | +2.5 | +3.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.3 | +1.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.1 | +1.5 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.5 µM |  | +2.0 | +2.2 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +1.9 | +2.4 |
|  | [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | +1.8 | +3.7 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -5.0 | -9.1 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -4.3 | -6.3 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -4.3 | -12.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -4.1 | -8.7 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -3.3 | -6.0 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | -3.2 | -3.3 |
|  | [[Verteporfin (drug)]] 5 µM |  | -3.0 | -1.4 |
|  | [[Binimetinib (drug)]] 0.05 µM |  | -2.9 | -2.1 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.8 | -2.6 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.8 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | adenosine monophosphate deaminase 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p13.3 — chr1:109,616,104-109,632,051 (+) |
| Ensembl biotype | protein_coding |
| Also known as | SPG63 |
| Gene groups (HGNC) | Adenosine deaminase family |
| Reactome | 3 pathways, smallest: Purine salvage; Nucleotide salvage; Metabolism of nucleotides |
| Matched by | ensembl_id |

**Function**, from UniProt [Q01433](https://www.uniprot.org/uniprotkb/Q01433) (AMP deaminase 2):

> AMP deaminase plays a critical role in energy metabolism. Catalyzes the deamination of AMP to IMP and plays an important role in the purine nucleotide cycle.

**Summary**, from NCBI Gene [271](https://www.ncbi.nlm.nih.gov/gene/271):

> The protein encoded by this gene is important in purine metabolism by converting AMP to IMP. The encoded protein, which acts as a homotetramer, is one of three AMP deaminases found in mammals. Several transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Apr 2012]

**Accessions** — [HGNC:469](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:469) · Entrez [271](https://www.ncbi.nlm.nih.gov/gene/271) · UniProt [Q01433](https://www.uniprot.org/uniprotkb/Q01433) · Ensembl [ENSG00000116337](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000116337)

## Data

Gene col 3790: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3790); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3790, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3790]; `tensor/DDL_lfc|DDL_z.npy` [3790]; `embed/gene_vectors.npy` [3790]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3790 or target_col == 3790). Every well: [[AMPD2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/AMPD2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
