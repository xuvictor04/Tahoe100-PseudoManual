---
symbol: "TBC1D10B"
type: "gene"
col: 9775
ensembl_id: "ENSG00000169221"
name: "TBC1 domain family member 10B"
location: "16p11.2"
module: 2
arm: "+"
pooled_cpm: 13.78
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 12
n_dd_up_clean: 5
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/002"]
generated_by: "tahoemap"
---

# TBC1D10B

*TBC1 domain family member 10B* — 16p11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (2 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 2.37× (z +7.3, q 1e-10, up in 24 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (5 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 0.763× (z -6.2, q 3e-07, down in 25 of 48 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PHRF1]] (+0.69, fdr 7e-06), [[SETD1A]] (+0.66, fdr 1e-05), [[ESS2]] (+0.64, fdr 7e-06); moves opposite to [[NT5DC1]] (-0.54, fdr 1e-05), [[MATR3-1]] (-0.51, fdr 3e-05), [[SDCBP]] (-0.50, fdr 3e-05).
> It sits in the **+** arm of [[Module 002]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 3 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9775.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **2.37×** | +7.3 | 1e-10 | 24/48 (SW480, PANC-1, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **2.07×** | +6.2 | 2e-07 | 25/43 (SW480, PANC-1, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **1.36×** | +5.0 | 9e-05 | 22/45 (RKO, COLO 205, …) | two highest doses | cell-cycle shift (explains ~6% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.36×** | +5.0 | 9e-05 | 20/48 (SW480, MIA PaCa-2, …) | two highest doses | cell-cycle shift (explains ~19% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~16% of this change | **1.22×** | +4.5 | 6e-04 | 18/46 (A549, NCI-H460, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **1.28×** | +4.1 | 0.005 | 16/47 (SW480, MIA PaCa-2, …) | two highest doses |  |
| [[Peretinoin (drug)]] 0.05 µM |  | **1.26×** | +3.5 | 0.035 | 4/47 (SW1417, NCI-H460, …) | inconsistent across doses | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~27% of this change | 1.22× | +3.1 | 0.13 | 11/41 (NCI-H2030, SW480, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 6 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9775.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **0.763×** | -6.2 | 3e-07 | 25/48 (MIA PaCa-2, CHP-212, …) | rises with dose | position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.768×** | -6.0 | 4e-07 | 26/47 (hTERT-HPNE, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.693×** | -6.0 | 5e-07 | 23/47 (HEC-1-A, NCI-H460, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.741×** | -4.7 | 4e-04 | 15/27 (HT-29, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **0.830×** | -4.3 | 0.002 | 14/48 (SW 900, A-427, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.776×** | -4.1 | 0.004 | 17/47 (CFPAC-1, COLO 205, …) | rises with dose | cell-cycle shift (explains ~7% here); position effect removed |
| [[Glycyrrhizic acid (drug)]] 5 µM |  | **0.775×** | -4.0 | 0.005 | 15/47 (HOP62, Panc 03.27, …) | top dose only | position effect removed |
| [[Bosentan (hydrate) (drug)]] 0.5 µM |  | **0.783×** | -4.0 | 0.005 | 8/47 (HEC-1-A, AsPC-1, …) | inconsistent across doses |  |
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.786×** | -3.9 | 0.006 | 10/48 (PANC-1, A-172, …) | inconsistent across doses |  |
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.851× | -3.7 | 0.012 | 7/48 (SW 1271, BT-474, …) | top dose only | position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.785×** | -3.6 | 0.014 | 14/32 (SW480, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~10% of this change | **0.816×** | -3.2 | 0.072 | 15/47 (H4, A-172, …) | rises with dose | composition shift; position effect removed |
| [[Fumaric acid (drug)]] 0.5 µM |  | **0.825×** | -3.1 | 0.080 | 2/48 (NCI-H460, A498) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.14 per unit of S-phase module lfc, -0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9775. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SHP-77 (line)]] | alt | 20.9 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.129× (z -13.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.265× (z -8.5) |
| [[C32 (line)]] | wt | 10.3 | 0 | 2 | — | [[Simotinib (drug)]] 0.05 µM 0.0770× (z -10.5) |
| [[A-172 (line)]] | wt | 24.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.440× (z -9.1) |
| [[A498 (line)]] | wt | 24.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.443× (z -10.6) |
| [[BT-474 (line)]] | alt | 10.8 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.102× (z -10.3) |
| [[H4 (line)]] | wt | 14.4 | 0 | 1 | — | [[Pyridoxine (drug)]] 0.5 µM 0.114× (z -8.5) |
| [[HCT15 (line)]] | alt | 19.1 | 0 | 1 | — | [[Medroxyprogesterone acetate (drug)]] 0.5 µM 0.167× (z -8.6) |
| [[HEC-1-A (line)]] | alt | 15.6 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.242× (z -9.7) |
| [[Hs 766T (line)]] | wt | 14.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.226× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HS-578T (line)]] | alt | 14.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.343× (z -8.6) |
| [[HT-29 (line)]] | alt | 15.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0934× (z -13.7) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 17.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.188× (z -11.5) |
| [[PANC-1 (line)]] | alt | 14.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.350× (z -8.5) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 17.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.306× (z -9.8) |
| [[RPMI-7951 (line)]] | alt | 13.3 | 0 | 1 | — | [[Pimozide (drug)]] 0.05 µM 0.0754× (z -11.6) |
| [[SNU-423 (line)]] | alt | 13.0 | 0 | 1 (1 ⚠) | — | [[AZD2858 (drug)]] 0.5 µM 0.0963× (z -9.3) ⚠ toxic |
| [[SW 900 (line)]] | alt | 15.3 | 0 | 1 | — | [[Selinexor (drug)]] 5 µM 0.321× (z -9.1) |
| [[SW48 (line)]] | wt | 12.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0785× (z -9.3) ⚠ cell-cycle shift, explains ~19% of this change |
| [[SW480 (line)]] | alt | 13.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.254× (z -10.5) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 13.8 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 11.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 21.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 9.65 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 14.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 16.3 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 11.7 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 13.1 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 12.4 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 9.25 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 7.25 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 9.08 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 9.59 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 11.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 13.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9775), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PHRF1]] | +0.69 | +0.62 / +0.63 | both halves | 7e-06 |  |
| [[SETD1A]] | +0.66 | +0.74 / +0.55 | both halves | 1e-05 |  |
| [[ESS2]] | +0.64 | +0.59 / +0.63 | both halves | 7e-06 |  |
| [[NDOR1]] | +0.63 | +0.59 / +0.68 | both halves | 7e-06 |  |
| [[PPP1R16A]] | +0.62 | +0.57 / +0.61 | both halves | 9e-06 |  |
| [[BRPF1]] | +0.61 | +0.52 / +0.66 | both halves | 1e-05 |  |
| [[DGCR8]] | +0.61 | +0.55 / +0.63 | both halves | 1e-05 |  |
| [[TUBGCP6]] | +0.61 | +0.67 / +0.45 | both halves | 3e-05 |  |
| [[RNF31]] | +0.60 | +0.55 / +0.56 | both halves | 1e-05 |  |
| [[PPP6R1]] | +0.59 | +0.56 / +0.54 | both halves | 1e-05 |  |
| [[MLLT1]] | +0.59 | +0.63 / +0.51 | both halves | 1e-05 |  |
| [[SERTAD3]] | +0.58 | +0.63 / +0.46 | both halves | 2e-05 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NT5DC1]] | -0.54 | -0.52 / -0.53 | both halves | 1e-05 |  |
| [[MATR3-1]] | -0.51 | -0.46 / -0.50 | both halves | 3e-05 |  |
| [[SDCBP]] | -0.50 | -0.49 / -0.44 | both halves | 3e-05 |  |
| [[PTER]] | -0.50 | -0.52 / -0.44 | both halves | 3e-05 |  |
| [[NPL]] | -0.49 | -0.55 / -0.37 | both halves | 7e-05 |  |
| [[RFK]] | -0.47 | -0.42 / -0.50 | both halves | 4e-05 |  |
| [[ABLIM1]] | -0.47 | -0.31 / -0.51 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity lowers TBC1D10B's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 002]]; 248 genes; this gene is in the **+** arm (projection on the module's main direction 0.513). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.21).
- **Nodal map** (x, y) = (-31.2, -10.7); signed map (-41.4, 4.5). **Vector** length 73.9, 12.1% of its response variance represented; |z| ≥ 3 in 825 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +4.7 | +7.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.3 | +6.2 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +3.4 | +5.0 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | +2.6 | +2.8 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~22% of this change | +2.1 | +4.1 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +1.5 | +2.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.3 | +2.3 |
|  | [[crizotinib (drug)]] 5 µM |  | +1.3 | +1.5 |
|  | [[Gallic acid (hydrate) (drug)]] 0.5 µM |  | +1.2 | +1.9 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -4.9 | -6.2 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -4.3 | -6.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -4.2 | -4.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~19% of this change | -3.5 | -2.9 |
|  | [[Selinexor (drug)]] 5 µM |  | -3.3 | -4.3 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.6 | -2.7 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.1 | -1.6 |
|  | [[Bosentan (hydrate) (drug)]] 0.5 µM |  | -1.7 | -4.0 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.6 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | TBC1 domain family member 10B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16p11.2 — chr16:30,357,102-30,370,494 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZP434P1750, Rab27A-GAPbeta, FLJ13130, EPI64B |
| Gene groups (HGNC) | TBC1 domain family members |
| Reactome | 4 pathways, smallest: TBC/RABGAPs; Rab regulation of trafficking; Membrane Trafficking |
| Matched by | ensembl_id |

**Function**, from UniProt [Q4KMP7](https://www.uniprot.org/uniprotkb/Q4KMP7) (TBC1 domain family member 10B):

> Acts as a GTPase-activating protein for RAB3A, RAB22A, RAB27A, and RAB35. Does not act on RAB2A and RAB6A.

**Summary**, from NCBI Gene [26000](https://www.ncbi.nlm.nih.gov/gene/26000):

> Small G proteins of the RAB family (see MIM 179508) function in intracellular vesicle trafficking by switching from the GTP-bound state to the GDP-bound state with the assistance of guanine nucleotide exchange factors (GEFs; see MIM 609700) and GTPase-activating proteins (GAPs). TBC1D10B functions as a GAP for several proteins of the Rab family (Ishibashi et al., 2009 [PubMed 19077034]).[supplied by OMIM, Nov 2010]

**Accessions** — [HGNC:24510](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24510) · Entrez [26000](https://www.ncbi.nlm.nih.gov/gene/26000) · UniProt [Q4KMP7](https://www.uniprot.org/uniprotkb/Q4KMP7) · Ensembl [ENSG00000169221](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000169221)

## Data

Gene col 9775: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9775); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9775, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9775]; `tensor/DDL_lfc|DDL_z.npy` [9775]; `embed/gene_vectors.npy` [9775]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9775 or target_col == 9775). Every well: [[TBC1D10B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TBC1D10B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
