---
symbol: "MAD2L2"
type: "gene"
col: 3817
ensembl_id: "ENSG00000116670"
name: "mitotic arrest deficient 2 like 2"
location: "1p36.22"
module: 85
arm: "+"
pooled_cpm: 10.93
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 0
n_dd_up_clean: 5
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/085"]
generated_by: "tahoemap"
---

# MAD2L2

*mitotic arrest deficient 2 like 2* — 1p36.22

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.57× (z +11.6, q 2e-28, up in 32 of 36 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change. The strongest without an alert is [[Panobinostat (drug)]] 0.5 µM: 2.29× (z +10.2, q 3e-22, up in 41 of 47 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (A-427 0.198×, MIA PaCa-2 0.172×; ⚠ cell-cycle shift, explains ~0% of this change); [[Crizotinib (hydrochloride) (drug)]] 0.5 µM in 1 line (LS 180 0.0530×); [[Vilanterol (drug)]] 0.05 µM in 1 line (LS 180 0.0793×).
> Its strongest partners by |cos| (89 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 11 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CARD19]] (+0.65, fdr 2e-05), [[CARHSP1]] (+0.64, fdr 1e-05), [[ARL3]] (+0.63, fdr 5e-05); moves opposite to [[GABPB1-AS1]] (-0.59, fdr 3e-04), [[DNAJC11]] (-0.57, fdr 4e-05), [[EPM2A]] (-0.57, fdr 4e-04).
> It sits in the **+** arm of [[Module 085]].
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[MPP2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 8 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3817.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **2.57×** | +11.6 | 2e-28 | 32/36 (SW480, SHP-77, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **2.43×** | +10.5 | 3e-23 | 14/19 (SW480, HT-29, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.29×** | +10.2 | 3e-22 | 41/47 (PANC-1, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **2.16×** | +9.5 | 3e-19 | 43/48 (PANC-1, SW480, …) | all doses, stronger at high dose | position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **2.13×** | +9.3 | 2e-18 | 39/47 (PANC-1, LoVo, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.48×** | +6.8 | 9e-10 | 26/45 (SK-MEL-2, NCI-H460, …) | top dose only | cell-cycle shift (explains ~19% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.62×** | +6.0 | 2e-07 | 20/39 (PANC-1, NCI-H2030, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~24% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.49×** | +4.9 | 6e-05 | 20/45 (LoVo, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.48×** | +4.9 | 8e-05 | 21/48 (HEC-1-A, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | **1.56×** | +4.5 | 4e-04 | 12/29 (LoVo, PANC-1, …) | all doses, stronger at high dose | composition shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.45×** | +4.4 | 6e-04 | 19/41 (HT-29, NCI-H460, …) | top dose only | cell-cycle shift (explains ~23% here) |
| [[Nimesulide (drug)]] 5 µM | ⚠ toxic; unreliable plate only | **1.32×** | +3.4 | 0.033 | 13/45 (NCI-H2347, SW1417, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.29×** | +3.1 | 0.084 | 12/46 (NCI-H2030, PANC-1, …) | inconsistent across doses |  |

## Drugs that lower it

No drug-dose lowers it in the pooled data (pooled over the cell lines, median: none with |z| ≥ 3 or q < 0.10). A response seen in fewer than about half of the measured lines does not reach the pooled data; see [[#In which cell lines]].

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (A-427 0.198×, MIA PaCa-2 0.172×; ⚠ cell-cycle shift, explains ~0% of this change); [[Crizotinib (hydrochloride) (drug)]] 0.5 µM in 1 line (LS 180 0.0530×); [[Vilanterol (drug)]] 0.05 µM in 1 line (LS 180 0.0793×).

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.35 per unit of S-phase module lfc, +0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3817. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LS 180 (line)]] | wt | 3.86 | 0 | 2 | — | [[Crizotinib (hydrochloride) (drug)]] 0.5 µM 0.0530× (z -10.4) |
| [[A-427 (line)]] | wt | 18.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.198× (z -10.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[MIA PaCa-2 (line)]] | alt | 14.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.172× (z -9.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SHP-77 (line)]] | alt | 16.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.58× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | — |
| [[SW1417 (line)]] | alt | 11.0 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.40× (z +9.5) ⚠ cell-cycle shift, would explain all of this change | — |
| [[SW480 (line)]] | alt | 16.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.05× (z +12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | — |
| [[A-172 (line)]] | wt | 10.5 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 10.2 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 6.69 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 5.14 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 12.1 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 7.52 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.71 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.57 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 12.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 16.2 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 11.2 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 5.92 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 8.00 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 5.82 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 8.63 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 7.02 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 5.63 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 6.92 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.96 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 8.87 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 6.44 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 8.53 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 6.11 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 14.1 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 9.77 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 10.3 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 8.68 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 9.87 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 13.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3817), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*76 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CARD19]] | +0.65 | +0.54 / +0.49 | both halves | 2e-05 |  |
| [[CARHSP1]] | +0.64 | +0.49 / +0.54 | both halves | 1e-05 |  |
| [[ARL3]] | +0.63 | +0.40 / +0.50 | both halves | 5e-05 |  |
| [[YIF1B]] | +0.62 | +0.39 / +0.41 | both halves | 6e-05 |  |
| [[PLA2G15]] | +0.61 | +0.47 / +0.39 | both halves | 5e-05 |  |
| [[INPP5F]] | +0.61 | +0.51 / +0.38 | both halves | 6e-05 |  |
| [[MAST3]] | +0.60 | +0.46 / +0.29 | both halves | 2e-04 |  |
| [[CABLES2]] | +0.60 | +0.42 / +0.40 | both halves | 5e-05 |  |
| [[SH2B2]] | +0.60 | +0.51 / +0.34 | both halves | 1e-04 |  |
| [[MOSPD3]] | +0.60 | +0.42 / +0.41 | both halves | 4e-05 |  |
| [[SLC27A1]] | +0.60 | +0.42 / +0.37 | both halves | 8e-05 |  |
| [[METTL26]] | +0.59 | +0.42 / +0.38 | both halves | 7e-05 |  |

## Genes that move opposite

*24 of its nearest partners move opposite, 9 of them with an alert (⚠; 9 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GABPB1-AS1]] | -0.59 | -0.53 / -0.28 | both halves | 3e-04 |  |
| [[DNAJC11]] | -0.57 | -0.47 / -0.41 | both halves | 4e-05 |  |
| [[EPM2A]] | -0.57 | -0.52 / -0.26 | both halves | 4e-04 |  |
| [[MMADHC-DT]] | -0.57 | -0.37 / -0.21 | both halves | 7e-04 |  |
| [[ITPA]] | -0.56 | -0.52 / -0.21 | both halves | 6e-04 |  |
| [[HEXIM2-AS1]] | -0.56 | -0.44 / -0.23 | both halves | 6e-04 |  |
| [[DPH5-DT]] | -0.56 | -0.44 / -0.27 | both halves | 3e-04 |  |
| [[ST7L]] | -0.56 | -0.31 / -0.30 | both halves | 2e-04 |  |
| [[ADCK1]] | -0.55 | -0.42 / -0.21 | both halves | 6e-04 |  |
| [[MTHFSD]] | -0.55 | -0.44 / -0.36 | both halves | 1e-04 |  |
| [[MFF-DT]] | -0.54 | -0.38 / -0.13 | ⚠ not reproduced | 0.002 |  |
| [[CRPPA]] | -0.54 | -0.39 / -0.29 | both halves | 2e-04 |  |
| [[METAP1D]] | -0.54 | -0.47 / -0.37 | both halves | 8e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 2, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MPP2]] | B | MPP2 activity raises MAD2L2's level | lines that do not express MPP2 (7) vs lines expressing it (43) | 1.68× lower at baseline in the lines without MPP2 | 0.023 | ⚠ within organs, on part of the lines; also absent: FAM229B, STARD9, CNN3-DT |
| [[SNTA1]] | B | SNTA1 activity raises MAD2L2's level | lines that do not express SNTA1 (5) vs lines expressing it (45) | 1.70× lower at baseline in the lines without SNTA1 | 0.067 | ⚠ within organs, on part of the lines; also absent: SACS, CLTCL1, MXRA7; maybe low, not absent |
| [[NAB2]] | C | NAB2 activity raises MAD2L2's level | lines that do not express NAB2 (3) vs lines expressing it (47) | 2.19× lower at baseline in the lines without NAB2 | 0.018 | ⚠ few lines (3 vs 47); across organs; co-absent genes; co-occurs with CTNNB1; also absent: DPF1, PPP2R3A, NKAIN1; maybe low, not absent |
| [[CIB1]] | C | CIB1 activity lowers MAD2L2's level | lines that do not express CIB1 (4) vs lines expressing it (46) | 1.51× higher at baseline in the lines without CIB1 | 0.096 | ⚠ few lines (4 vs 46); within organs, on part of the lines; co-absent genes; also absent: SHB, NIBAN2, IER3; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 085]]; 52 genes; this gene is in the **+** arm (projection on the module's main direction 0.690). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.43).
- **Nodal map** (x, y) = (4.8, -2.5); signed map (-30.5, 17.2). **Vector** length 52.1, 7.41% of its response variance represented; |z| ≥ 3 in 713 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | +3.4 | +9.3 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | +3.2 | +9.5 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +3.0 | +10.2 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +2.1 | +4.9 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +1.9 | +4.9 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +1.1 | -0.1 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.0 | +2.4 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +0.9 | +2.3 |
|  | [[Belinostat (drug)]] 0.05 µM |  | +0.8 | +2.1 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.5 µM |  | +0.8 | +1.2 |
| fall | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.0 | -0.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -2.9 | -1.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -1.7 | +1.7 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -1.7 | +1.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.6 | -1.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.3 | -2.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.3 | -0.2 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.2 | +1.3 |
|  | [[Binimetinib (drug)]] 0.05 µM |  | -1.2 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | mitotic arrest deficient 2 like 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p36.22 — chr1:11,658,918-11,691,811 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MAD2B, REV7, POLZ2, FANCV |
| Gene groups (HGNC) | DNA polymerases; FA complementation groups; HORMA domain containing |
| Reactome | 12 pathways, smallest: Translesion synthesis by REV1; Translesion synthesis by POLI; Translesion synthesis by POLK |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UI95](https://www.uniprot.org/uniprotkb/Q9UI95) (Mitotic spindle assembly checkpoint protein MAD2B):

> Adapter protein able to interact with different proteins and involved in different biological processes. Mediates the interaction between the error-prone DNA polymerase zeta catalytic subunit REV3L and the inserter polymerase REV1, thereby mediating the second polymerase switching in translesion DNA synthesis. Translesion DNA synthesis releases the replication blockade of replicative polymerases, stalled in presence of DNA lesions. Component of the shieldin complex, which plays an important …

**Summary**, from NCBI Gene [10459](https://www.ncbi.nlm.nih.gov/gene/10459):

> The protein encoded by this gene is a component of the mitotic spindle assembly checkpoint that prevents the onset of anaphase until all chromosomes are properly aligned at the metaphase plate. The encoded protein, which is similar to MAD2L1, is capable of interacting with ADAM9, ADAM15, REV1, and REV3 proteins. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:6764](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6764) · Entrez [10459](https://www.ncbi.nlm.nih.gov/gene/10459) · UniProt [Q9UI95](https://www.uniprot.org/uniprotkb/Q9UI95) · Ensembl [ENSG00000116670](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000116670)

## Data

Gene col 3817: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3817); `tables/drug_effects.parquet` (13 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3817, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3817]; `tensor/DDL_lfc|DDL_z.npy` [3817]; `embed/gene_vectors.npy` [3817]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3817 or target_col == 3817). Every well: [[MAD2L2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MAD2L2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
