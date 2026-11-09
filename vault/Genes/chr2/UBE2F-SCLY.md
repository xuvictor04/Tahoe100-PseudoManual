---
symbol: "UBE2F-SCLY"
type: "gene"
col: 15160
ensembl_id: "ENSG00000258984"
name: "UBE2F-SCLY readthrough (NMD candidate)"
location: "2q37.3"
module: 38
arm: "+"
pooled_cpm: 7.21
n_lines_expressing: 50
n_dd_up: 28
n_dd_down: 5
n_dd_up_clean: 17
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/038"]
generated_by: "tahoemap"
---

# UBE2F-SCLY

*UBE2F-SCLY readthrough (NMD candidate)* — 2q37.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 28 drug-doses (11 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.38× (z +16.9, q 0e+00, up in 38 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (2 with an alert ⚠); the strongest is [[NG25 (drug)]] 5 µM: 0.463× (z -5.6, q 1e-05, down in 19 of 35 measured lines) ⚠ cell-cycle shift, explains ~31% of this change. The strongest without an alert is [[HI-TOPK-032 (drug)]] 0.05 µM: 0.697× (z -4.6, q 0.001, down in 12 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SLC22A20P]] (+0.68, fdr 7e-06), [[WNT2B]] (+0.66, fdr 7e-06), [[LRRC69]] (+0.65, fdr 7e-06); moves opposite to [[CLK4]] (-0.56, fdr 2e-05), [[MKS1]] (-0.55, fdr 1e-05), [[ZNF608]] (-0.52, fdr 4e-05).
> It is in [[Module 038]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 13 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 28 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15160.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.38×** | +16.9 | 0e+00 | 38/43 (NCI-H460, MIA PaCa-2, …) | inconsistent across doses | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.58×** | +13.0 | 2e-36 | 42/47 (SW480, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.29×** | +11.4 | 8e-28 | 38/47 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.09×** | +10.1 | 5e-22 | 37/47 (HOP62, SW480, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.19× | +8.1 | 5e-14 | 23/48 (HEC-1-A, A-172, …) | inconsistent across doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.54×** | +5.7 | 1e-06 | 17/41 (NCI-H460, A498, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.50×** | +5.6 | 2e-06 | 15/47 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **1.45×** | +5.1 | 2e-05 | 14/47 (RPMI-7951, A498, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **1.49×** | +5.0 | 3e-05 | 8/24 (A-172, SW1417, …) | all doses, flat | composition shift |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.48×** | +5.0 | 3e-05 | 11/46 (A-172, SW1417, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.28×** | +4.8 | 7e-05 | 13/48 (NCI-H460, A-172, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~51% of this change | **1.44×** | +4.8 | 7e-05 | 13/33 (A498, SW480, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.43×** | +4.5 | 3e-04 | 13/44 (A-172, LS 180, …) | inconsistent across doses | cell-cycle shift (explains ~21% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~56% of this change | **1.38×** | +4.4 | 4e-04 | 8/47 (LOX-IMVI, NCI-H460, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **1.38×** | +4.4 | 5e-04 | 18/47 (HEC-1-A, NCI-H460, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **1.35×** | +4.0 | 0.002 | 9/44 (A549, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Peretinoin (drug)]] 5 µM |  | **1.34×** | +3.8 | 0.004 | 7/46 (A-172, SW 900, …) | top dose only |  |
| [[Brivudine (drug)]] 5 µM |  | **1.66×** | +3.6 | 0.008 | 4/47 (CFPAC-1, A-172, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.30×** | +3.6 | 0.010 | 11/47 (HOP62, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[EX229 (drug)]] 5 µM |  | **1.62×** | +3.5 | 0.013 | 2/39 (NCI-H460, LoVo) | top dose only | noisy plate (z scaled) |
| [[Filgotinib (drug)]] 5 µM |  | **1.26×** | +3.1 | 0.039 | 1/47 (LoVo) | top dose only |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.25×** | +3.1 | 0.044 | 5/47 (HEC-1-A, A498, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 3 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 15160.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.463×** | -5.6 | 1e-05 | 19/35 (NCI-H460, Hs 766T, …) | top dose only | noisy plate (z scaled) |
| [[HI-TOPK-032 (drug)]] 0.05 µM |  | **0.697×** | -4.6 | 0.001 | 12/45 (NCI-H23, SHP-77, …) | inconsistent across doses | low cells (technical?) |
| [[GSK1059615 (drug)]] 0.5 µM |  | **0.639×** | -4.4 | 0.002 | 12/40 (hTERT-HPNE, A-172, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.746×** | -3.8 | 0.024 | 10/42 (NCI-H1792, SW 900, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~40% of this change | **0.770×** | -3.6 | 0.031 | 12/37 (HepG2/C3A, NCI-H2030, …) | inconsistent across doses | low cells (technical?) |
| [[Afatinib (drug)]] 5 µM |  | 0.812× | -3.0 | 0.20 | 11/47 (BT-474, A-172, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | 0.798× | -3.0 | 0.20 | 10/36 (A549, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.43 per unit of S-phase module lfc, -0.37 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15160. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[BT-474 (line)]] | alt | 6.32 | 0 | 3 | — | [[Doxycycline (monohydrate) (drug)]] 5 µM 0.0812× (z -9.3) |
| [[NCI-H460 (line)]] | wt | 8.18 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.87× (z +11.8) | — |
| [[HEC-1-A (line)]] | alt | 9.98 | 0 | 1 | — | [[Drospirenone (drug)]] 0.5 µM 0.181× (z -10.1) |
| [[NCI-H1792 (line)]] | alt | 7.45 | 0 | 1 | — | [[Harringtonine (drug)]] 0.05 µM 0.0743× (z -10.5) |
| [[PANC-1 (line)]] | alt | 3.77 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0901× (z -11.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change |
| [[SW480 (line)]] | alt | 5.60 | 0 | 1 | — | [[Naproxen (drug)]] 0.05 µM 0.206× (z -8.8) |
| [[A-172 (line)]] | wt | 9.74 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 6.85 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 7.07 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 6.53 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 9.69 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 6.27 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 5.29 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 6.89 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 6.72 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.50 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.66 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.73 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 15.5 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 6.49 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 5.54 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 7.76 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 4.07 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.16 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 4.29 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.85 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 13.9 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 7.70 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 12.1 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.83 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 6.28 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.35 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 7.81 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.48 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.09 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.26 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 7.55 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 12.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 6.30 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 7.15 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 8.70 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 4.60 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.83 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 6.13 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 7.31 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 5.41 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15160), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC22A20P]] | +0.68 | +0.59 / +0.73 | both halves | 7e-06 |  |
| [[WNT2B]] | +0.66 | +0.66 / +0.66 | both halves | 7e-06 |  |
| [[LRRC69]] | +0.65 | +0.64 / +0.63 | both halves | 7e-06 |  |
| [[CCDC168]] | +0.65 | +0.56 / +0.64 | both halves | 1e-05 |  |
| [[RSKR]] | +0.63 | +0.54 / +0.67 | both halves | 1e-05 |  |
| [[LINC01588]] | +0.62 | +0.58 / +0.64 | both halves | 7e-06 |  |
| [[MSANTD1]] | +0.62 | +0.52 / +0.72 | both halves | 1e-05 |  |
| [[RAPSN]] | +0.62 | +0.57 / +0.62 | both halves | 1e-05 |  |
| [[SLC27A4]] | +0.60 | +0.55 / +0.61 | both halves | 1e-05 |  |
| [[EFCAB8]] | +0.59 | +0.51 / +0.68 | both halves | 1e-05 |  |
| [[HYAL1]] | +0.59 | +0.48 / +0.65 | both halves | 2e-05 |  |
| [[ATP2A1]] | +0.59 | +0.48 / +0.68 | both halves | 2e-05 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CLK4]] | -0.56 | -0.47 / -0.59 | both halves | 2e-05 |  |
| [[MKS1]] | -0.55 | -0.49 / -0.53 | both halves | 1e-05 |  |
| [[ZNF608]] | -0.52 | -0.40 / -0.50 | both halves | 4e-05 |  |
| [[C2CD5]] | -0.52 | -0.44 / -0.42 | both halves | 4e-05 |  |
| [[NDUFA5]] | -0.51 | -0.50 / -0.48 | both halves | 2e-05 |  |
| [[SETDB2]] | -0.51 | -0.42 / -0.51 | both halves | 4e-05 |  |
| [[NUDT12]] | -0.51 | -0.35 / -0.52 | both halves | 1e-04 |  |
| [[CYB5RL]] | -0.50 | -0.39 / -0.44 | both halves | 6e-05 |  |
| [[SNX2]] | -0.49 | -0.54 / -0.39 | both halves | 5e-05 |  |
| [[GALT]] | -0.49 | -0.45 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers UBE2F-SCLY's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 6.2% of all compounds | 0.047 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 038]]; 122 genes; every member is in the + arm (projection on the module's main direction 0.550). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.28; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (37.1, -20.5); signed map (13.1, 9.3). **Vector** length 61.6, 9.03% of its response variance represented; |z| ≥ 3 in 966 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.6 | +16.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change | +3.3 | +3.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | +3.1 | +5.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | +2.6 | +4.2 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +2.4 | +3.1 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.2 | +5.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.0 | +4.8 |
|  | [[Peretinoin (drug)]] 5 µM |  | +1.8 | +3.8 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +1.7 | +1.2 |
| fall | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -3.4 | -2.1 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | -3.3 | -5.6 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -2.2 | +1.1 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.8 | -2.5 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | -1.8 | -4.6 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | -1.7 | -2.9 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -1.6 | -0.7 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | -1.4 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | UBE2F-SCLY readthrough (NMD candidate) |
| Locus type | readthrough (other) |
| Location | 2q37.3 — chr2:237,967,014-238,099,412 (+) |
| Ensembl biotype | protein_coding |
| Matched by | ensembl_id |

**Summary**, from NCBI Gene [100533179](https://www.ncbi.nlm.nih.gov/gene/100533179):

> This locus represents naturally occurring read-through transcription between the neighboring UBE2F (ubiquitin-conjugating enzyme E2F) and SCLY (selenocysteine lyase) genes on chromosome 2. The read-through transcript is a candidate for non-sense mediated mRNA decay (NMD), and is unlikely to produce a protein product. [provided by RefSeq, Feb 2011]

**Accessions** — [HGNC:48339](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:48339) · Entrez [100533179](https://www.ncbi.nlm.nih.gov/gene/100533179) · Ensembl [ENSG00000258984](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000258984)

## Data

Gene col 15160: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15160); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15160, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15160]; `tensor/DDL_lfc|DDL_z.npy` [15160]; `embed/gene_vectors.npy` [15160]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15160 or target_col == 15160). Every well: [[UBE2F-SCLY — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/UBE2F-SCLY.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
