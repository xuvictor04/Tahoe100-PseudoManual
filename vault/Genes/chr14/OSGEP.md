---
symbol: "OSGEP"
type: "gene"
col: 1687
ensembl_id: "ENSG00000092094"
name: "O-sialoglycoprotein endopeptidase"
location: "14q11.2"
module: 28
arm: "+"
pooled_cpm: 14.14
n_lines_expressing: 50
n_dd_up: 20
n_dd_down: 6
n_dd_up_clean: 15
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/028"]
generated_by: "tahoemap"
---

# OSGEP

*O-sialoglycoprotein endopeptidase* — 14q11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.65× (z +13.3, q 2e-37, up in 35 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (none with an alert); the strongest is [[Auranofin (drug)]] 5 µM: 0.537× (z -11.7, q 1e-28, down in 34 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FAM133B]] (+0.63, fdr 7e-06), [[PRPF39]] (+0.61, fdr 1e-05), [[EBAG9]] (+0.60, fdr 1e-05); moves opposite to [[PRDX1]] (-0.59, fdr 1e-05), [[TXN]] (-0.59, fdr 7e-06), [[CTDP1]] (-0.52, fdr 3e-05).
> It sits in the **+** arm of [[Module 028]] (Intraflagellar transport).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 6 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1687.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.65×** | +13.3 | 2e-37 | 35/47 (NCI-H460, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.57×** | +8.2 | 1e-13 | 26/47 (NCI-H460, A-427, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Belumosudil (drug)]] 5 µM |  | **1.55×** | +7.9 | 6e-13 | 30/47 (NCI-H460, NCI-H1573, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.45×** | +6.7 | 4e-09 | 21/43 (NCI-H1573, SW480, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.28×** | +6.5 | 1e-08 | 22/48 (Panc 03.27, HS-578T, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.36×** | +5.8 | 8e-07 | 22/47 (NCI-H460, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.31×** | +5.0 | 4e-05 | 14/48 (CFPAC-1, HOP62, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~15% of this change | **1.30×** | +4.8 | 9e-05 | 18/47 (LoVo, NCI-H1573, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.29×** | +4.8 | 9e-05 | 12/47 (J82, C32, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.31×** | +4.6 | 2e-04 | 8/31 (KATO III, HOP62, …) | all doses, flat | cell-cycle shift (explains ~15% here); composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~18% of this change | **1.28×** | +4.6 | 2e-04 | 16/48 (LoVo, LOX-IMVI, …) | rises with dose |  |
| [[NG25 (drug)]] 5 µM |  | **1.56×** | +4.3 | 7e-04 | 7/44 (HCT15, NCI-H23, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **1.53×** | +4.2 | 0.001 | 15/48 (A-427, LS 180, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~3% here); composition shift; noisy plate (z scaled) |
| [[Pralsetinib (drug)]] 5 µM |  | **1.49×** | +3.9 | 0.004 | 6/46 (NCI-H1573, PANC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Radotinib (drug)]] 5 µM |  | 1.16× | +3.8 | 0.005 | 14/48 (NCI-H2030, CFPAC-1, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.43×** | +3.5 | 0.016 | 8/45 (LS 180, PANC-1, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Glycyrrhizic acid (drug)]] 0.5 µM |  | **1.20×** | +3.4 | 0.019 | 6/47 (PANC-1, SW480, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[venetoclax (drug)]] 5 µM |  | **1.40×** | +3.3 | 0.030 | 1/45 (RPMI-7951) | inconsistent across doses | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 0.5 µM |  | 1.18× | +3.0 | 0.068 | 8/47 (SW480, SK-MEL-2, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 2 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 1687.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **0.537×** | -11.7 | 1e-28 | 34/47 (SW480, NCI-H23, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.682×** | -7.2 | 2e-10 | 25/47 (SHP-77, NCI-H2347, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.715×** | -6.3 | 5e-08 | 25/47 (SNU-1, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.747×** | -5.5 | 6e-06 | 16/48 (SW480, NCI-H23, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.750×** | -5.4 | 7e-06 | 17/47 (SW480, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.758×** | -5.2 | 2e-05 | 16/48 (SW480, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | 0.844× | -3.2 | 0.11 | 11/46 (SW480, NCI-H1792, …) | all doses, flat | position effect removed |
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | 0.846× | -3.2 | 0.11 | 7/48 (SW 1088, NCI-H2347, …) | inconsistent across doses |  |
| [[Peretinoin (drug)]] 5 µM |  | 0.845× | -3.1 | 0.14 | 9/47 (A-427, NCI-H1573, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.09 per unit of S-phase module lfc, -0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1687. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 10.5 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.97× (z +18.4) | [[Dinaciclib (drug)]] 5 µM 0.245× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change |
| [[SW480 (line)]] | alt | 17.3 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.142× (z -16.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.298× (z -10.6) |
| [[LoVo (line)]] | wt | 10.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.02× (z +10.2) | — |
| [[LS 180 (line)]] | wt | 24.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.12× (z +12.7) | — |
| [[NCI-H2030 (line)]] | alt | 23.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.19× (z +8.8) | — |
| [[NCI-H23 (line)]] | alt | 16.2 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.233× (z -9.3) |
| [[Panc 03.27 (line)]] | alt | 15.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.135× (z -11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change |
| [[RKO (line)]] | wt | 12.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.45× (z +8.7) | — |
| [[SNU-1 (line)]] | wt | 18.1 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.155× (z -8.5) |
| [[A-172 (line)]] | wt | 6.81 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 18.2 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 10.0 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 12.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 23.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 8.59 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 28.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 7.71 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 14.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 11.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 22.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 11.6 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 8.77 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 11.5 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 7.10 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 8.50 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 8.44 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 9.69 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 26.7 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 31.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 21.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 8.92 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 12.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1687), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FAM133B]] | +0.63 | +0.63 / +0.68 | both halves | 7e-06 |  |
| [[PRPF39]] | +0.61 | +0.54 / +0.64 | both halves | 1e-05 |  |
| [[EBAG9]] | +0.60 | +0.65 / +0.56 | both halves | 1e-05 |  |
| [[C2CD5]] | +0.60 | +0.65 / +0.51 | both halves | 1e-05 |  |
| [[ZDHHC17]] | +0.59 | +0.54 / +0.50 | both halves | 1e-05 |  |
| [[SNHG11]] | +0.58 | +0.60 / +0.58 | both halves | 7e-06 |  |
| [[CLK4]] | +0.58 | +0.59 / +0.57 | both halves | 8e-06 |  |
| [[SPEF2]] | +0.58 | +0.60 / +0.54 | both halves | 1e-05 |  |
| [[ZNF428]] | +0.58 | +0.66 / +0.57 | both halves | 1e-05 |  |
| [[PTBP2]] | +0.57 | +0.53 / +0.50 | both halves | 1e-05 |  |
| [[SUCLG1]] | +0.57 | +0.65 / +0.56 | both halves | 1e-05 |  |
| [[MKS1]] | +0.57 | +0.59 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PRDX1]] | -0.59 | -0.54 / -0.57 | both halves | 1e-05 |  |
| [[TXN]] | -0.59 | -0.61 / -0.58 | both halves | 7e-06 |  |
| [[CTDP1]] | -0.52 | -0.46 / -0.58 | both halves | 3e-05 |  |
| [[CBL]] | -0.51 | -0.65 / -0.40 | both halves | 5e-05 |  |
| [[TICAM2]] | -0.51 | -0.36 / -0.60 | both halves | 1e-04 |  |
| [[MIB1]] | -0.49 | -0.33 / -0.57 | both halves | 1e-04 |  |
| [[HSPA8]] | -0.48 | -0.42 / -0.53 | both halves | 4e-05 |  |
| [[GAN]] | -0.48 | -0.43 / -0.45 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 028]] — Intraflagellar transport; 154 genes; this gene is in the **+** arm (projection on the module's main direction 0.534). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-25.0, 1.5); signed map (-20.6, -15.7). **Vector** length 78.3, 14.1% of its response variance represented; |z| ≥ 3 in 771 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +4.6 | +13.3 |
|  | [[Harringtonine (drug)]] 5 µM |  | +3.5 | +8.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.1 | +5.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +3.0 | +5.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +3.0 | +6.7 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.6 | +3.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.2 | +1.8 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.0 | +7.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.0 | +3.5 |
| fall | [[Auranofin (drug)]] 5 µM |  | -8.0 | -11.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.7 | -1.3 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -3.4 | -6.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -2.9 | -7.2 |
|  | [[Digitoxin (drug)]] 0.05 µM |  | -2.4 | -5.4 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.1 | -3.0 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.7 | -2.4 |
|  | [[Gefitinib (drug)]] 5 µM |  | -1.5 | -3.0 |
|  | [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | -1.4 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | O-sialoglycoprotein endopeptidase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q11.2 — chr14:20,446,401-20,455,089 (-) |
| Ensembl biotype | protein_coding |
| Also known as | PRSMG1, GCPL1, OSGEP1, KAE1, TCS3 |
| Gene groups (HGNC) | KEOPS complex; OSGEP family |
| Reactome | 3 pathways, smallest: tRNA modification in the nucleus and cytosol; tRNA processing; Metabolism of RNA |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NPF4](https://www.uniprot.org/uniprotkb/Q9NPF4) (tRNA N6-adenosine threonylcarbamoyltransferase):

> Component of the EKC/KEOPS complex that is required for the formation of a threonylcarbamoyl group on adenosine at position 37 (t(6)A37) in tRNAs that read codons beginning with adenine. The complex is probably involved in the transfer of the threonylcarbamoyl moiety of threonylcarbamoyl-AMP (TC-AMP) to the N6 group of A37. OSGEP likely plays a direct catalytic role in this reaction, but requires other protein(s) of the complex to fulfill this activity.

**Summary**, from NCBI Gene [55644](https://www.ncbi.nlm.nih.gov/gene/55644):

> Enables tRNA N(6)-L-threonylcarbamoyladenine synthase activity. Involved in tRNA threonylcarbamoyladenosine modification. Located in cytosol and nucleoplasm. Part of EKC/KEOPS complex. Implicated in Galloway-Mowat syndrome 3. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:18028](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18028) · Entrez [55644](https://www.ncbi.nlm.nih.gov/gene/55644) · UniProt [Q9NPF4](https://www.uniprot.org/uniprotkb/Q9NPF4) · Ensembl [ENSG00000092094](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000092094)

## Data

Gene col 1687: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1687); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1687, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1687]; `tensor/DDL_lfc|DDL_z.npy` [1687]; `embed/gene_vectors.npy` [1687]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1687 or target_col == 1687). Every well: [[OSGEP — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/OSGEP.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
