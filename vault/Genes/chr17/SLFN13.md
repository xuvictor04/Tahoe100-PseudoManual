---
symbol: "SLFN13"
type: "gene"
col: 7835
ensembl_id: "ENSG00000154760"
name: "schlafen family member 13"
location: "17q12"
module: 6
arm: "+"
pooled_cpm: 6.12
n_lines_expressing: 20
n_dd_up: 21
n_dd_down: 1
n_dd_up_clean: 4
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/006"]
generated_by: "tahoemap"
---

# SLFN13

*schlafen family member 13* — 17q12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (17 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 4.22× (z +13.0, q 1e-35, up in 5 of 9 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 1.64× (z +6.5, q 9e-09, up in 10 of 17 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Ouabain (Octahydrate) (drug)]] 0.5 µM: 0.668× (z -3.8, q 0.076, down in 9 of 16 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 2 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Bortezomib (drug)]] 0.05 µM in 1 line (KATO III 0.138×; ⚠ cell-cycle shift, explains ~29% of this change); [[Roxadustat (drug)]] 0.05 µM in 1 line (J82 0.0618×); [[Ixazomib citrate (drug)]] 5 µM in 1 line (KATO III 0.226×); [[Auranofin (drug)]] 5 µM in 1 line (KATO III 0.251×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[E2F8]] (+0.72, fdr 7e-06), [[MCM2]] (+0.68, fdr 7e-06), [[FAM111B]] (+0.68, fdr 7e-06); moves opposite to [[NSA2]] (-0.54, fdr 4e-05), [[NOXRED1]] (-0.53, fdr 2e-04).
> It sits in the **+** arm of [[Module 006]] (E2F targets).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 17 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 17 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7835.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **4.22×** | +13.0 | 1e-35 | 5/9 (PANC-1, NCI-H2347, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | **3.14×** | +10.7 | 3e-24 | 6/12 (PANC-1, HEC-1-A, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **2.83×** | +9.0 | 4e-17 | 7/11 (Panc 03.27, CFPAC-1, …) | all doses, stronger at high dose | composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.64×** | +6.5 | 9e-09 | 10/17 (CFPAC-1, NCI-H2347, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~32% of this change | **1.82×** | +5.4 | 8e-06 | 6/13 (PANC-1, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~67% of this change | **1.69×** | +4.9 | 8e-05 | 11/17 (J82, PANC-1, …) | all doses, flat | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.68×** | +4.8 | 1e-04 | 15/17 (PANC-1, KATO III, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~35% of this change | **1.69×** | +4.7 | 2e-04 | 4/13 (CFPAC-1, NCI-H1573, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **1.41×** | +4.5 | 4e-04 | 3/16 (A549, NCI-H2347, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~88% of this change | **1.62×** | +4.5 | 4e-04 | 11/17 (J82, PANC-1, …) | all doses, flat | position effect removed |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **1.95×** | +4.5 | 4e-04 | 1/12 (NCI-H2347) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~82% of this change | **1.57×** | +4.2 | 0.001 | 7/17 (PANC-1, NCI-H1573, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.47×** | +3.6 | 0.013 | 7/17 (NCI-H1573, SW 900, …) | all doses, flat | position effect removed |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **2.08×** | +3.6 | 0.014 | 0/11 | top dose only | noisy plate (z scaled) |
| [[Trifluridine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **1.30×** | +3.5 | 0.019 | 4/17 (PANC-1, NCI-H23, …) | rises with dose | position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.27×** | +3.1 | 0.053 | 5/17 (NCI-H2347, PANC-1, …) | top dose only |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.58×** | +3.1 | 0.062 | 1/13 (CFPAC-1) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.37×** | +2.9 | 0.098 | 3/15 (NCI-H2030, PANC-1, …) | inconsistent across doses | low cells (technical?); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 3 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 7835.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 2 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Bortezomib (drug)]] 0.05 µM in 1 line (KATO III 0.138×; ⚠ cell-cycle shift, explains ~29% of this change); [[Roxadustat (drug)]] 0.05 µM in 1 line (J82 0.0618×); [[Ixazomib citrate (drug)]] 5 µM in 1 line (KATO III 0.226×); [[Auranofin (drug)]] 5 µM in 1 line (KATO III 0.251×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.668×** | -3.8 | 0.076 | 9/16 (PANC-1, NCI-H1573, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Neratinib (maleate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | 0.695× | -3.4 | 0.11 | 8/16 (CFPAC-1, KATO III, …) | inconsistent across doses |  |
| [[Mebendazole (drug)]] 5 µM |  | 0.686× | -3.4 | 0.11 | 1/17 (A549) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | 0.707× | -3.3 | 0.14 | 7/18 (KATO III, HEC-1-A, …) | inconsistent across doses |  |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | 0.794× | -3.1 | 0.22 | 8/17 (KATO III, HEC-1-A, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.728× | -3.0 | 0.24 | 7/17 (PANC-1, SW 1271, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.63 per unit of S-phase module lfc, -0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7835. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[KATO III (line)]] | alt | 61.1 | 0 | 3 (1 ⚠) | — | [[Bortezomib (drug)]] 0.05 µM 0.138× (z -12.1) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.226× (z -9.6) |
| [[A498 (line)]] | wt | 6.20 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.202× (z -8.7) ⚠ cell-cycle shift, explains ~27% of this change |
| [[CFPAC-1 (line)]] | alt | 11.0 | 0 | 1 | — | [[Vinblastine (sulfate) (drug)]] 0.5 µM 0.177× (z -8.6) |
| [[J82 (line)]] | alt | 5.51 | 0 | 1 | — | [[Roxadustat (drug)]] 0.05 µM 0.0618× (z -9.8) |
| [[A-172 (line)]] | wt | 0.870 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.502 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 2.46 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 0.695 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 7.84 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 0.447 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.639 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.805 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.575 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.458 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 1.06 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.485 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 25.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.519 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 5.25 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.33 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.451 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.487 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.940 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.470 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.703 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.435 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.370 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 2.35 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.864 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 3.16 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.59 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 7.48 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 7.51 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.40 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 2.55 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.36 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 19.9 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 23.7 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.472 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.08 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.418 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.44 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.564 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.24 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 0.900 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 8.19 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.33 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.558 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.523 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7835), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[E2F8]] | +0.72 | +0.61 / +0.74 | both halves | 7e-06 |  |
| [[MCM2]] | +0.68 | +0.60 / +0.70 | both halves | 7e-06 |  |
| [[FAM111B]] | +0.68 | +0.63 / +0.71 | both halves | 7e-06 |  |
| [[ZWINT]] | +0.68 | +0.57 / +0.72 | both halves | 1e-05 |  |
| [[CENPM]] | +0.67 | +0.58 / +0.66 | both halves | 7e-06 |  |
| [[FAM111A]] | +0.66 | +0.60 / +0.77 | both halves | 7e-06 |  |
| [[HELLS]] | +0.66 | +0.61 / +0.66 | both halves | 7e-06 |  |
| [[MCM4]] | +0.66 | +0.57 / +0.67 | both halves | 1e-05 |  |
| [[DNMT1]] | +0.66 | +0.60 / +0.65 | both halves | 7e-06 |  |
| [[ATAD2]] | +0.64 | +0.58 / +0.66 | both halves | 8e-06 |  |
| [[ESCO2]] | +0.64 | +0.59 / +0.66 | both halves | 7e-06 |  |
| [[DYNC2I2]] | +0.63 | +0.53 / +0.63 | both halves | 1e-05 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NSA2]] | -0.54 | -0.42 / -0.50 | both halves | 4e-05 |  |
| [[NOXRED1]] | -0.53 | -0.32 / -0.56 | both halves | 2e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 006]] — E2F targets; 236 genes; this gene is in the **+** arm (projection on the module's main direction 0.630). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (-37.1, -43.7); signed map (-38.1, -47.5). **Vector** length 46.4, 12.7% of its response variance represented; |z| ≥ 3 in 390 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *DNA strand elongation* (reactome, mean cos +0.51 to 28); *E2F G1/S* (control, mean cos +0.50 to 23); *Cell Cycle Checkpoints* (reactome, mean cos +0.51 to 45).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | +5.6 | +13.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | +4.9 | +10.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | +4.5 | +9.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.9 | +6.5 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~35% of this change | +2.7 | +4.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.7 | +3.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | +1.4 | +2.8 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +1.2 | +2.1 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.1 | +3.1 |
| fall | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~29% of this change | -1.6 | -2.9 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -1.5 | -1.7 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.5 | -2.2 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.5 | -1.9 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | -1.4 | -3.1 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.3 | -2.8 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.2 | -3.3 |

## What is on record

|  |  |
|---|---|
| Name | schlafen family member 13 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q12 — chr17:35,435,096-35,448,837 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ31952 |
| Gene groups (HGNC) | Schlafen family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q68D06](https://www.uniprot.org/uniprotkb/Q68D06) (Schlafen family member 13):

> Endoribonuclease that cleaves tRNAs and rRNAs. Cleaves tRNAs 11 nucleotides from the 3'-terminus at the acceptor stem. Does not act on tRNA(Sec). Able to restrict HIV-1 virus replication; ability to inhibit HIV-1 replication is dependent on endoribonuclease activity.

**Summary**, from NCBI Gene [146857](https://www.ncbi.nlm.nih.gov/gene/146857):

> Enables RNA endonuclease activity. Involved in rRNA catabolic process and tRNA decay. Located in cytoplasm. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:26481](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26481) · Entrez [146857](https://www.ncbi.nlm.nih.gov/gene/146857) · UniProt [Q68D06](https://www.uniprot.org/uniprotkb/Q68D06) · Ensembl [ENSG00000154760](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000154760)

## Data

Gene col 7835: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7835); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7835, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7835]; `tensor/DDL_lfc|DDL_z.npy` [7835]; `embed/gene_vectors.npy` [7835]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7835 or target_col == 7835). Every well: [[SLFN13 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SLFN13.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
