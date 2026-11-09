---
symbol: "ADGRL1-AS1"
type: "gene"
col: 15529
ensembl_id: "ENSG00000267169"
name: "ADGRL1 antisense RNA 1"
location: "19p13.12"
module: 101
arm: "+"
pooled_cpm: 8.48
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 0
n_dd_up_clean: 11
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/101"]
generated_by: "tahoemap"
---

# ADGRL1-AS1

*ADGRL1 antisense RNA 1* — 19p13.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (3 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 2.45× (z +12.6, q 2e-33, up in 37 of 46 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 4 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Methotrexate (drug)]] 0.05 µM in 1 line (SNU-423 0.0696×); [[Digitoxin (drug)]] 5 µM in 1 line (H4 0.0671×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change); [[Simotinib (drug)]] 5 µM in 1 line (NCI-H2030 0.120×; ⚠ toxic); [[Cobimetinib (drug)]] 5 µM in 1 line (SW 900 0.0849×); [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM in 1 line (SNU-423 0.101×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GPATCH2L]] (+0.63, fdr 7e-06), [[TRIOBP]] (+0.61, fdr 1e-05), [[TPT1-AS1]] (+0.60, fdr 1e-05); moves opposite to [[ZNF639]] (-0.61, fdr 1e-05), [[PYURF]] (-0.61, fdr 1e-05), [[PAIP1]] (-0.60, fdr 7e-06).
> It is in [[Module 101]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TM4SF19-DYNLT2B]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 3 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15529.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **2.45×** | +12.6 | 2e-33 | 37/46 (RKO, HEC-1-A, …) | top dose only | position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **2.13×** | +10.6 | 8e-24 | 33/48 (HEC-1-A, LoVo, …) | rises with dose | cell-cycle shift (explains ~5% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.70×** | +10.5 | 1e-23 | 32/44 (A498, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.82×** | +8.4 | 5e-15 | 35/48 (HEC-1-A, LoVo, …) | rises with dose | cell-cycle shift (explains ~6% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.50×** | +8.0 | 2e-13 | 26/45 (MIA PaCa-2, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.60×** | +6.3 | 3e-08 | 25/42 (HS-578T, HOP62, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.42×** | +4.9 | 6e-05 | 18/47 (LoVo, KATO III, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.27×** | +4.7 | 2e-04 | 14/48 (MIA PaCa-2, SNU-423, …) | top dose only |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.39×** | +4.6 | 3e-04 | 10/47 (AsPC-1, KATO III, …) | top dose only | position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.39×** | +4.3 | 0.001 | 3/24 (RPMI-7951, HOP62, …) | all doses, flat | cell-cycle shift (explains ~13% here); composition shift |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.71×** | +3.8 | 0.007 | 5/42 (A498, Panc 03.27, …) | top dose only | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~20% of this change | **1.30×** | +3.6 | 0.016 | 4/18 (SW480, HT-29, …) | all doses, flat | composition shift |
| [[Infigratinib (drug)]] 5 µM |  | **1.62×** | +3.4 | 0.025 | 5/43 (NCI-H2347, HS-578T, …) | top dose only | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **1.24×** | +3.0 | 0.098 | 7/36 (C32, LoVo, …) | all doses, flat | composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 15529.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 4 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Methotrexate (drug)]] 0.05 µM in 1 line (SNU-423 0.0696×); [[Digitoxin (drug)]] 5 µM in 1 line (H4 0.0671×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change); [[Simotinib (drug)]] 5 µM in 1 line (NCI-H2030 0.120×; ⚠ toxic); [[Cobimetinib (drug)]] 5 µM in 1 line (SW 900 0.0849×); [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM in 1 line (SNU-423 0.101×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.769× | -3.7 | 0.12 | 11/47 (NCI-H460, Hs 766T, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.09 per unit of S-phase module lfc, -0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15529. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SNU-423 (line)]] | alt | 6.26 | 0 | 3 | — | [[Methotrexate (drug)]] 0.05 µM 0.0696× (z -11.7) |
| [[NCI-H2030 (line)]] | alt | 8.70 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.15× (z +8.7) | [[Simotinib (drug)]] 5 µM 0.120× (z -11.0) ⚠ toxic |
| [[H4 (line)]] | wt | 17.9 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0671× (z -11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change |
| [[HEC-1-A (line)]] | alt | 11.4 | 1 | 0 | [[Auranofin (drug)]] 5 µM 3.97× (z +8.6) | — |
| [[HT-29 (line)]] | alt | 5.82 | 0 | 1 | — | [[Pyridoxine (drug)]] 0.5 µM 0.0711× (z -9.2) |
| [[J82 (line)]] | alt | 10.9 | 0 | 1 (1 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.209× (z -9.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[MIA PaCa-2 (line)]] | alt | 12.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.50× (z +9.2) | — |
| [[NCI-H460 (line)]] | wt | 8.48 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.281× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[RKO (line)]] | wt | 14.2 | 1 | 0 | [[Auranofin (drug)]] 5 µM 7.97× (z +9.9) | — |
| [[SW 900 (line)]] | alt | 8.48 | 0 | 1 | — | [[Cobimetinib (drug)]] 5 µM 0.0849× (z -10.1) |
| [[A-172 (line)]] | wt | 9.06 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 4.99 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 6.29 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 7.27 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 7.23 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 7.15 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 9.94 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 6.61 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 7.12 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 5.07 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.44 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 7.46 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 7.01 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 7.29 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 8.07 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 5.29 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 6.27 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 4.20 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 4.42 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.96 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 8.03 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.59 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 8.41 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.35 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 9.05 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 9.18 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 7.08 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 5.47 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 6.62 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 9.83 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15529), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*64 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GPATCH2L]] | +0.63 | +0.61 / +0.59 | both halves | 7e-06 |  |
| [[TRIOBP]] | +0.61 | +0.52 / +0.65 | both halves | 1e-05 |  |
| [[TPT1-AS1]] | +0.60 | +0.53 / +0.62 | both halves | 1e-05 | same gene group |
| [[PPP1R13L]] | +0.60 | +0.57 / +0.56 | both halves | 1e-05 |  |
| [[SPRED3]] | +0.59 | +0.54 / +0.60 | both halves | 1e-05 |  |
| [[SMTN]] | +0.59 | +0.55 / +0.56 | both halves | 1e-05 |  |
| [[CYTH2]] | +0.59 | +0.59 / +0.52 | both halves | 1e-05 |  |
| [[SPAG5-AS1]] | +0.57 | +0.54 / +0.57 | both halves | 1e-05 | same gene group |
| [[LINC01772]] | +0.57 | +0.50 / +0.59 | both halves | 1e-05 |  |
| [[LUCAT1]] | +0.57 | +0.53 / +0.55 | both halves | 1e-05 |  |
| [[TTLL3]] | +0.57 | +0.53 / +0.56 | both halves | 1e-05 |  |
| [[EXD3]] | +0.57 | +0.33 / +0.65 | both halves | 1e-04 |  |

## Genes that move opposite

*36 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF639]] | -0.61 | -0.55 / -0.58 | both halves | 1e-05 |  |
| [[PYURF]] | -0.61 | -0.52 / -0.60 | both halves | 1e-05 |  |
| [[PAIP1]] | -0.60 | -0.58 / -0.59 | both halves | 7e-06 |  |
| [[PTPN13]] | -0.60 | -0.42 / -0.55 | both halves | 4e-05 |  |
| [[CCDC6]] | -0.56 | -0.50 / -0.58 | both halves | 1e-05 |  |
| [[CAND1]] | -0.55 | -0.51 / -0.53 | both halves | 1e-05 |  |
| [[RAVER2]] | -0.55 | -0.54 / -0.51 | both halves | 1e-05 |  |
| [[NFIA]] | -0.54 | -0.55 / -0.46 | both halves | 3e-05 |  |
| [[SLC25A12]] | -0.54 | -0.41 / -0.51 | both halves | 4e-05 |  |
| [[KCTD3]] | -0.53 | -0.50 / -0.49 | both halves | 1e-05 |  |
| [[COX11]] | -0.53 | -0.52 / -0.54 | both halves | 1e-05 |  |
| [[MRPL19]] | -0.52 | -0.52 / -0.51 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TM4SF19-DYNLT2B]] | B | TM4SF19-DYNLT2B activity raises ADGRL1-AS1's level | lines that do not express TM4SF19-DYNLT2B (20) vs lines expressing it (30) | 1.28× lower at baseline in the lines without TM4SF19-DYNLT2B | 0.046 | ⚠ within organs, on part of the lines; co-absent genes; also absent: ADAMTS9, KYNU, PAK3 |
| [[TOP2A]] | B | TOP2A activity lowers ADGRL1-AS1's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Idarubicin, Mitoxantrone) | 60% of the class's compounds vs 3.1% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 101]]; 46 genes; every member is in the + arm (projection on the module's main direction 0.570). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (22.8, -14.2); signed map (-0.5, 29.2). **Vector** length 71.3, 11.8% of its response variance represented; |z| ≥ 3 in 870 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +6.8 | +12.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.3 | +10.5 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +3.2 | +8.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.3 | +2.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~20% of this change | +2.2 | +3.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.9 | +4.7 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | +1.6 | +2.4 |
|  | [[Celecoxib (drug)]] 0.5 µM |  | +1.6 | +2.2 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -3.1 | -3.7 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.5 | -1.5 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | -2.1 | -3.0 |
|  | [[EX229 (drug)]] 5 µM |  | -2.1 | -2.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.1 | -2.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.1 | -1.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.1 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | ADGRL1 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 19p13.12 — chr19:14,137,146-14,171,267 (+) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:55309](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:55309) · Entrez [100507373](https://www.ncbi.nlm.nih.gov/gene/100507373) · Ensembl [ENSG00000267169](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000267169)

## Data

Gene col 15529: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15529); `tables/drug_effects.parquet` (15 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15529, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15529]; `tensor/DDL_lfc|DDL_z.npy` [15529]; `embed/gene_vectors.npy` [15529]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15529 or target_col == 15529). Every well: [[ADGRL1-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ADGRL1-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
