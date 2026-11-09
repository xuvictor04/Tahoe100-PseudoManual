---
symbol: "NINJ2"
type: "gene"
col: 10171
ensembl_id: "ENSG00000171840"
name: "ninjurin 2"
location: "12p13.33"
module: 35
arm: "+"
pooled_cpm: 2.25
n_lines_expressing: 48
n_dd_up: 20
n_dd_down: 0
n_dd_up_clean: 11
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/035"]
generated_by: "tahoemap"
---

# NINJ2

*ninjurin 2* — 12p13.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (9 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 5.91× (z +22.3, q 0e+00, up in 17 of 17 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 2 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Belinostat (drug)]] 5 µM in 2 lines (LoVo 0.121×, LS 180 0.0564×); [[Panobinostat (drug)]] 5 µM in 2 lines (LoVo 0.122×, KATO III 0.199×; ⚠ cell-cycle shift, explains ~0% of this change); [[Panobinostat (drug)]] 0.5 µM in 1 line (KATO III 0.161×); [[Methotrexate (drug)]] 0.05 µM in 1 line (HT-29 0.0790×).
> Its strongest partners by |cos| (72 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 28 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FAM174B]] (+0.72, fdr 3e-05), [[EFCAB5]] (+0.68, fdr 3e-04), [[EPS15-AS1]] (+0.68, fdr 3e-04); moves opposite to [[GNAI2]] (-0.62, fdr 1.00, ⚠ one half only (not replicated)), [[ARRB2]] (-0.60, fdr 0.008, ⚠ not reproduced), [[YIF1B]] (-0.58, fdr 1.00, ⚠ one half only (not replicated)), [[ALAD]] (-0.57, fdr 6e-04).
> It sits in the **+** arm of [[Module 035]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 9 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10171.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **5.91×** | +22.3 | 0e+00 | 17/17 (LoVo, SW480, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **5.19×** | +14.0 | 2e-42 | 1/1 (NCI-H2347) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.48×** | +11.1 | 4e-26 | 7/10 (SW 900, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.06×** | +9.2 | 7e-18 | 2/4 (NCI-H2347, LoVo) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.80×** | +8.8 | 2e-16 | 14/22 (SW480, KATO III, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.89×** | +8.0 | 1e-13 | 14/35 (SW480, SW 900, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.38×** | +7.4 | 1e-11 | 10/16 (SW480, KATO III, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **2.12×** | +6.6 | 2e-09 | 18/32 (SW480, HT-29, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.70×** | +4.5 | 4e-04 | 2/8 (LoVo, LS 180) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.62×** | +4.3 | 1e-03 | 0/9 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.35×** | +4.0 | 0.004 | 0/1 | top dose only | noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.53×** | +3.8 | 0.008 | 3/25 (LS 180, HOP62, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **1.33×** | +3.6 | 0.017 | 4/37 (LoVo, SW 900, …) | top dose only | low cells (technical?) |
| [[Drospirenone (drug)]] 0.5 µM |  | **1.47×** | +3.4 | 0.028 | 3/19 (KATO III, RKO, …) | inconsistent across doses | position effect removed |
| [[Lidocaine (hydrochloride) (drug)]] 0.05 µM |  | **1.45×** | +3.3 | 0.039 | 1/10 (RKO) | inconsistent across doses | low cells (technical?) |
| [[Palmatine (chloride) (drug)]] 0.5 µM |  | **1.43×** | +3.2 | 0.054 | 0/14 | inconsistent across doses |  |
| [[Bicalutamide (drug)]] 0.5 µM |  | **1.42×** | +3.1 | 0.057 | 3/28 (RPMI-7951, SW480, …) | inconsistent across doses |  |
| [[Oxaprozin (drug)]] 0.5 µM |  | **1.41×** | +3.0 | 0.067 | 1/17 (HOP62) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 10171.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 2 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Belinostat (drug)]] 5 µM in 2 lines (LoVo 0.121×, LS 180 0.0564×); [[Panobinostat (drug)]] 5 µM in 2 lines (LoVo 0.122×, KATO III 0.199×; ⚠ cell-cycle shift, explains ~0% of this change); [[Panobinostat (drug)]] 0.5 µM in 1 line (KATO III 0.161×); [[Methotrexate (drug)]] 0.05 µM in 1 line (HT-29 0.0790×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.05 µM |  | 0.684× | -3.4 | 0.42 | 8/38 (RKO, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | 0.714× | -3.0 | 0.60 | 12/36 (LoVo, LS 180, …) | top dose only | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.16 per unit of S-phase module lfc, -0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10171. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 11.4 | 1 | 3 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.49× (z +13.4) | [[Belinostat (drug)]] 5 µM 0.121× (z -11.8) |
| [[KATO III (line)]] | alt | 12.2 | 1 | 2 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.18× (z +12.3) | [[Panobinostat (drug)]] 0.5 µM 0.161× (z -9.7) |
| [[HT-29 (line)]] | alt | 4.12 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.28× (z +10.5) | [[Methotrexate (drug)]] 0.05 µM 0.0790× (z -8.9) |
| [[LS 180 (line)]] | wt | 5.61 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.06× (z +10.1) | [[Belinostat (drug)]] 5 µM 0.0564× (z -10.5) |
| [[RKO (line)]] | wt | 5.37 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.95× (z +8.8) | — |
| [[SW480 (line)]] | alt | 5.15 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.34× (z +12.7) | — |
| [[A-172 (line)]] | wt | 0.563 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 2.09 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.683 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 0.751 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.41 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.635 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 0.770 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.626 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.784 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.16 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.701 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 7.42 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 0.564 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.724 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 0.787 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.03 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.31 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.97 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 0.545 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.578 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 0.608 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.666 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.922 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 0.720 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.795 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 0.567 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 1.75 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.952 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.35 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.931 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.66 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.869 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.24 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.48 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.03 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.854 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.60 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.604 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 0.846 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 0.679 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.08 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.30 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.25 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.83 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10171), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 25 of them with an alert (⚠; 25 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FAM174B]] | +0.72 | +0.50 / +0.43 | both halves | 3e-05 |  |
| [[EFCAB5]] | +0.68 | +0.56 / +0.27 | both halves | 3e-04 |  |
| [[EPS15-AS1]] | +0.68 | +0.75 / +0.27 | both halves | 3e-04 |  |
| [[CRPPA]] | +0.67 | +0.47 / +0.22 | both halves | 6e-04 |  |
| [[MMADHC-DT]] | +0.66 | +0.57 / +0.19 | ⚠ one half (not replicated) | 8e-04 |  |
| [[SIAH2-AS1]] | +0.66 | +0.53 / +0.42 | both halves | 4e-05 |  |
| [[CIBAR1-DT]] | +0.66 | +0.47 / +0.26 | both halves | 4e-04 |  |
| [[RAD9B]] | +0.66 | +0.43 / +0.46 | both halves | 3e-05 |  |
| [[CASC11]] | +0.66 | +0.58 / +0.39 | both halves | 5e-05 |  |
| [[CCNO-DT]] | +0.65 | +0.52 / +0.36 | both halves | 9e-05 |  |
| [[SATB1-AS1]] | +0.65 | +0.60 / +0.36 | both halves | 1e-04 |  |
| [[NIPAL2]] | +0.64 | +0.51 / +0.20 | both halves | 7e-04 |  |
| [[ST7-AS2]] | +0.64 | +0.39 / +0.48 | both halves | 5e-05 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 3 of them with an alert (⚠; 3 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GNAI2]] | -0.62 | -0.51 / +0.09 | ⚠ one half (not replicated) | 1.00 |  |
| [[ARRB2]] | -0.60 | -0.42 / -0.01 | ⚠ not reproduced | 0.008 |  |
| [[YIF1B]] | -0.58 | -0.53 / +0.04 | ⚠ one half (not replicated) | 1.00 |  |
| [[ALAD]] | -0.57 | -0.33 / -0.21 | both halves | 6e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers NINJ2's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.8% of all compounds | 0.028 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 035]]; 137 genes; this gene is in the **+** arm (projection on the module's main direction 0.671). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (10.6, 20.2); signed map (26.2, -4.6). **Vector** length 39.7, 5.22% of its response variance represented; |z| ≥ 3 in 811 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.7 | +22.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.1 | +8.0 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +3.8 | +7.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.2 | +14.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | +3.1 | +6.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.4 | +3.8 |
|  | [[Amsacrine (drug)]] 5 µM |  | +1.3 | +1.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.1 | +2.2 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +1.0 | +2.7 |
| fall | [[Belinostat (drug)]] 5 µM |  | -2.1 | -3.0 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -1.8 | -1.8 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.6 | +0.0 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -1.5 | -0.7 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -1.3 | -3.4 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.1 | -2.1 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -0.9 | -2.0 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -0.8 | -1.5 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -0.7 | -2.3 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.5 µM |  | -0.7 | -0.4 |

## What is on record

|  |  |
|---|---|
| Name | ninjurin 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12p13.33 — chr12:564,296-663,589 (-) |
| Ensembl biotype | protein_coding |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NZG7](https://www.uniprot.org/uniprotkb/Q9NZG7) (Ninjurin-2):

> Its role in unclear. In contrast to NINJ1 paralog, does not mediate plasma membrane rupture (cytolysis) downstream of necroptotic and pyroptotic programmed cell death. While it is able to oligomerize and form filaments, filaments are curved toward the intracellular space, preventing circularization to mediate plasma membrane rupture. May act as a homophilic transmembrane adhesion molecule involved in nerve regeneration. Promotes axonal growth.

**Summary**, from NCBI Gene [4815](https://www.ncbi.nlm.nih.gov/gene/4815):

> The protein encoded by this gene belongs to the ninjurin (for nerve injury induced) family. It is a cell surface adhesion protein that is upregulated in Schwann cells surrounding the distal segment of injured nerve, and promotes neurite outgrowth, thus may have a role in nerve regeneration after nerve injury. [provided by RefSeq, Oct 2011]

**Accessions** — [HGNC:7825](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7825) · Entrez [4815](https://www.ncbi.nlm.nih.gov/gene/4815) · UniProt [Q9NZG7](https://www.uniprot.org/uniprotkb/Q9NZG7) · Ensembl [ENSG00000171840](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000171840)

## Data

Gene col 10171: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10171); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10171, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10171]; `tensor/DDL_lfc|DDL_z.npy` [10171]; `embed/gene_vectors.npy` [10171]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10171 or target_col == 10171). Every well: [[NINJ2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NINJ2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
