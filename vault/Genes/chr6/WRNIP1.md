---
symbol: "WRNIP1"
type: "gene"
col: 4538
ensembl_id: "ENSG00000124535"
name: "WRN helicase interacting protein 1"
location: "6p25.2"
module: 50
arm: "+"
pooled_cpm: 38.45
n_lines_expressing: 50
n_dd_up: 1
n_dd_down: 4
n_dd_up_clean: 0
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/050"]
generated_by: "tahoemap"
---

# WRNIP1

*WRN helicase interacting protein 1* — 6p25.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[Niclosamide (olamine) (drug)]] 5 µM: 1.26× (z +4.5, q 0.005, up in 20 of 47 measured lines) ⚠ toxic; cell-cycle shift, explains ~15% of this change.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.05 µM in 1 line (SW480 2.31×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~73% of this change); [[Niclosamide (olamine) (drug)]] 5 µM in 1 line (LoVo 2.45×; ⚠ toxic; cell-cycle shift, explains ~15% of this change).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.553× (z -17.0, q 0e+00, down in 42 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[METAP1]] (+0.71, fdr 1e-05), [[TBC1D24]] (+0.68, fdr 1e-05), [[RNF4]] (+0.67, fdr 7e-06); moves opposite to [[LARP7]] (-0.66, fdr 1e-05), [[NSRP1]] (-0.66, fdr 7e-06), [[RBM23]] (-0.64, fdr 1e-05).
> It is in [[Module 050]], a single-armed module (Extracellular matrix organization).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 6 with an alert ⚠. 1 of them raises it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4538.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.05 µM in 1 line (SW480 2.31×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~73% of this change); [[Niclosamide (olamine) (drug)]] 5 µM in 1 line (LoVo 2.45×; ⚠ toxic; cell-cycle shift, explains ~15% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~15% of this change | **1.26×** | +4.5 | 0.005 | 20/47 (LoVo, NCI-H460, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 1.20× | +3.7 | 0.059 | 16/48 (CFPAC-1, Panc 03.27, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | 1.19× | +3.6 | 0.059 | 16/48 (SNU-423, HOP62, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~18% of this change | 1.19× | +3.5 | 0.059 | 19/48 (SW480, LoVo, …) | inconsistent across doses | position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | 1.19× | +3.5 | 0.059 | 16/48 (LoVo, SNU-423, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | 1.13× | +3.4 | 0.059 | 13/48 (A-427, KATO III, …) | top dose only |  |
| [[5-Azacytidine (drug)]] 0.5 µM |  | 1.17× | +3.1 | 0.15 | 5/47 (NCI-H23, HT-29, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 1 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 4538.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.553×** | -17.0 | 0e+00 | 42/48 (SNU-1, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.887× | -8.6 | 2e-15 | 6/48 (MIA PaCa-2, NCI-H23, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.645×** | -8.6 | 2e-15 | 31/48 (A-172, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.772×** | -5.3 | 2e-05 | 23/48 (A-172, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Auranofin (drug)]] 5 µM |  | 0.841× | -3.5 | 0.042 | 12/48 (SK-MEL-2, BT-474, …) | top dose only |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.785×** | -3.5 | 0.042 | 18/46 (J82, SNU-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Sodium Salicylate (drug)]] 5 µM |  | 0.899× | -3.1 | 0.17 | 5/48 (NCI-H2347, NCI-H460, …) | rises with dose | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.12 per unit of S-phase module lfc, -0.00 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4538. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 49.1 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.312× (z -16.5) |
| [[SNU-1 (line)]] | wt | 58.9 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.198× (z -18.1) |
| [[A-427 (line)]] | wt | 32.5 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.214× (z -12.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~73% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.484× (z -8.9) |
| [[AsPC-1 (line)]] | alt | 33.7 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.404× (z -10.5) |
| [[LoVo (line)]] | wt | 40.9 | 1 (1 ⚠) | 1 | [[Niclosamide (olamine) (drug)]] 5 µM 2.45× (z +9.7) ⚠ toxic; cell-cycle shift, explains ~15% of this change | [[Homoharringtonine (drug)]] 5 µM 0.583× (z -8.6) |
| [[NCI-H1573 (line)]] | alt | 23.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.379× (z -10.7) |
| [[AN3 CA (line)]] | alt | 65.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.179× (z -13.0) |
| [[BT-474 (line)]] | alt | 33.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.452× (z -9.0) |
| [[CFPAC-1 (line)]] | alt | 41.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.441× (z -11.3) |
| [[CHP-212 (line)]] | wt | 39.9 | 0 | 1 | — | [[Acetohexamide (drug)]] 0.5 µM 0.0771× (z -10.8) |
| [[HOP62 (line)]] | alt | 30.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.508× (z -9.6) |
| [[J82 (line)]] | alt | 47.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.334× (z -16.3) |
| [[MIA PaCa-2 (line)]] | alt | 57.1 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.364× (z -9.7) |
| [[NCI-H2030 (line)]] | alt | 38.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.369× (z -12.8) |
| [[NCI-H23 (line)]] | alt | 52.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.409× (z -12.1) |
| [[NCI-H2347 (line)]] | alt | 58.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.363× (z -17.6) |
| [[NCI-H460 (line)]] | wt | 29.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.489× (z -10.3) |
| [[NCI-H661 (line)]] | alt | 49.2 | 0 | 1 | — | [[Thymol (drug)]] 0.5 µM 0.118× (z -9.0) |
| [[Panc 03.27 (line)]] | alt | 79.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.423× (z -12.2) |
| [[RKO (line)]] | wt | 39.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.327× (z -14.1) |
| [[SK-MEL-2 (line)]] | alt | 34.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.280× (z -14.4) |
| [[SW 1271 (line)]] | alt | 39.7 | 0 | 1 | — | [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM 0.0572× (z -9.1) |
| [[SW480 (line)]] | alt | 32.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 2.31× (z +9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~73% of this change | — |
| [[A498 (line)]] | wt | 17.6 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 24.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 46.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 40.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 30.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 33.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 39.4 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 41.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 40.7 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 30.6 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 37.9 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 30.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 31.5 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 42.8 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 41.0 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 40.9 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 35.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 31.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 35.9 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 36.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 33.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 38.9 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 34.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 26.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 30.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 44.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 57.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4538), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*58 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[METAP1]] | +0.71 | +0.84 / +0.57 | both halves | 1e-05 |  |
| [[TBC1D24]] | +0.68 | +0.70 / +0.51 | both halves | 1e-05 |  |
| [[RNF4]] | +0.67 | +0.74 / +0.59 | both halves | 7e-06 |  |
| [[SETD3]] | +0.66 | +0.70 / +0.58 | both halves | 8e-06 |  |
| [[COLGALT1]] | +0.66 | +0.68 / +0.60 | both halves | 7e-06 |  |
| [[BLTP2]] | +0.66 | +0.71 / +0.59 | both halves | 7e-06 |  |
| [[SLC25A39]] | +0.65 | +0.64 / +0.56 | both halves | 1e-05 |  |
| [[PLEKHA8]] | +0.65 | +0.67 / +0.58 | both halves | 7e-06 |  |
| [[KDM1A]] | +0.65 | +0.71 / +0.56 | both halves | 1e-05 |  |
| [[BPNT2]] | +0.64 | +0.66 / +0.63 | both halves | 7e-06 |  |
| [[NDC1]] | +0.64 | +0.70 / +0.57 | both halves | 1e-05 |  |
| [[ARHGEF7]] | +0.64 | +0.72 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*42 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LARP7]] | -0.66 | -0.69 / -0.54 | both halves | 1e-05 |  |
| [[NSRP1]] | -0.66 | -0.70 / -0.59 | both halves | 7e-06 |  |
| [[RBM23]] | -0.64 | -0.71 / -0.54 | both halves | 1e-05 |  |
| [[ZNF764]] | -0.64 | -0.78 / -0.45 | both halves | 3e-05 |  |
| [[BTN2A3P-1]] | -0.64 | -0.63 / -0.55 | both halves | 1e-05 |  |
| [[OCIAD1]] | -0.63 | -0.72 / -0.51 | both halves | 1e-05 |  |
| [[CCDC174]] | -0.63 | -0.64 / -0.59 | both halves | 7e-06 |  |
| [[HELQ]] | -0.62 | -0.72 / -0.54 | both halves | 1e-05 |  |
| [[ZC3HC1]] | -0.62 | -0.70 / -0.54 | both halves | 1e-05 |  |
| [[FCF1]] | -0.62 | -0.73 / -0.54 | both halves | 1e-05 |  |
| [[CDK3]] | -0.62 | -0.68 / -0.44 | both halves | 3e-05 |  |
| [[THG1L]] | -0.61 | -0.71 / -0.46 | both halves | 2e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 050]] — Extracellular matrix organization; 92 genes; every member is in the + arm (projection on the module's main direction 0.585). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.27; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-6.4, -18.9); signed map (-41.8, -12.1). **Vector** length 93.9, 19.9% of its response variance represented; |z| ≥ 3 in 746 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +3.3 | +3.7 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | +3.2 | +3.6 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | +2.7 | +3.5 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | +2.7 | +2.6 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~15% of this change | +2.6 | +4.5 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +2.0 | +1.2 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +1.7 | +0.6 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.5 µM |  | +1.6 | +0.9 |
|  | [[Lonafarnib (drug)]] 0.5 µM |  | +1.6 | +2.2 |
|  | [[Mebendazole (drug)]] 5 µM |  | +1.5 | +0.4 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -10.4 | -17.0 |
|  | [[Harringtonine (drug)]] 5 µM |  | -7.9 | -8.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -6.9 | -5.3 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.7 | -3.5 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.7 | -2.1 |
|  | [[Binimetinib (drug)]] 0.05 µM |  | -2.5 | -2.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -2.3 | -3.5 |
|  | [[Lactate (calcium) (drug)]] 0.5 µM |  | -1.9 | -1.2 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -1.6 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | WRN helicase interacting protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p25.2 — chr6:2,765,393-2,786,952 (+) |
| Ensembl biotype | protein_coding |
| Also known as | WHIP, FLJ22526, bA420G6.2, FAP93, CFAP93 |
| Gene groups (HGNC) | AAA ATPases; Cilia and flagella associated; Zinc fingers UBZ4 CCHC-type |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96S55](https://www.uniprot.org/uniprotkb/Q96S55) (ATPase WRNIP1):

> Functions as a modulator of initiation or reinitiation events during DNA polymerase delta-mediated DNA synthesis. In the presence of ATP, stimulation of DNA polymerase delta-mediated DNA synthesis is decreased. Also plays a role in the innate immune defense against viruses. Stabilizes the RIGI dsRNA interaction and promotes RIGI 'Lys-63'-linked polyubiquitination. In turn, RIGI transmits the signal through mitochondrial MAVS.

**Summary**, from NCBI Gene [56897](https://www.ncbi.nlm.nih.gov/gene/56897):

> Werner's syndrome is a rare autosomal recessive disorder characterized by accelerated aging that is caused by defects in the Werner syndrome ATP-dependent helicase gene (WRN). The protein encoded by this gene interacts with the exonuclease-containing N-terminal portion of the Werner protein. This protein has a ubiquitin-binding zinc-finger domain in the N-terminus, an ATPase domain, and two leucine zipper motifs in the C-terminus. It has sequence similarity to replication factor C family …

**Accessions** — [HGNC:20876](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20876) · Entrez [56897](https://www.ncbi.nlm.nih.gov/gene/56897) · UniProt [Q96S55](https://www.uniprot.org/uniprotkb/Q96S55) · Ensembl [ENSG00000124535](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000124535)

## Data

Gene col 4538: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4538); `tables/drug_effects.parquet` (14 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4538, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4538]; `tensor/DDL_lfc|DDL_z.npy` [4538]; `embed/gene_vectors.npy` [4538]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4538 or target_col == 4538). Every well: [[WRNIP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/WRNIP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
