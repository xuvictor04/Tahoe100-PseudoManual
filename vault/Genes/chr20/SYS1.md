---
symbol: "SYS1"
type: "gene"
col: 12809
ensembl_id: "ENSG00000204070"
name: "SYS1 golgi trafficking protein"
location: "20q13.12"
module: 188
arm: "+"
pooled_cpm: 18.73
n_lines_expressing: 50
n_dd_up: 19
n_dd_down: 3
n_dd_up_clean: 14
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/188"]
generated_by: "tahoemap"
---

# SYS1

*SYS1 golgi trafficking protein* — 20q13.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.58× (z +14.4, q 4e-44, up in 31 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (none with an alert); the strongest is [[Verteporfin (drug)]] 5 µM: 0.773× (z -5.5, q 2e-05, down in 21 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RAB8A]] (+0.55, fdr 2e-05), [[JUNB]] (+0.55, fdr 1e-05), [[KLF4]] (+0.55, fdr 1e-05); moves opposite to [[FAR1]] (-0.57, fdr 2e-05), [[SNX4]] (-0.57, fdr 2e-05), [[MBD2]] (-0.55, fdr 1e-05).
> It is in [[Module 188]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 6 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12809.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.58×** | +14.4 | 4e-44 | 31/47 (A498, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.95×** | +14.3 | 8e-44 | 35/47 (A498, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift; position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.78×** | +12.8 | 3e-35 | 40/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift; position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.59×** | +10.2 | 2e-22 | 32/46 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.37×** | +10.0 | 3e-21 | 27/47 (NCI-H2347, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.53×** | +9.4 | 6e-19 | 30/47 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.51×** | +9.2 | 4e-18 | 33/48 (SW480, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.50×** | +9.0 | 2e-17 | 29/47 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.47×** | +8.5 | 1e-15 | 25/47 (A498, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.43×** | +8.0 | 8e-14 | 27/48 (SW480, KATO III, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[TAK-901 (drug)]] 5 µM |  | **1.74×** | +6.4 | 6e-09 | 21/48 (SW480, NCI-H2347, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~14% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.33×** | +6.4 | 1e-08 | 18/48 (A498, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~33% of this change | **1.29×** | +5.6 | 1e-06 | 22/42 (NCI-H2347, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.28×** | +5.5 | 1e-06 | 16/47 (MIA PaCa-2, KATO III, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **1.28×** | +5.4 | 2e-06 | 18/47 (KATO III, C32, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.37×** | +3.7 | 0.008 | 13/44 (SW480, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.24×** | +3.4 | 0.021 | 6/46 (SW1417, KATO III, …) | two highest doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | 1.15× | +2.9 | 0.097 | 7/47 (PANC-1, A498, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, none with an alert. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 12809.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Verteporfin (drug)]] 5 µM |  | **0.773×** | -5.5 | 2e-05 | 21/47 (A498, NCI-H1573, …) | rises with dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **0.813×** | -4.6 | 0.001 | 15/48 (BT-474, RKO, …) | two highest doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.829×** | -4.0 | 0.011 | 17/46 (HS-578T, CHP-212, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Cyclosporin A (drug)]] 5 µM |  | 0.857× | -3.5 | 0.079 | 7/47 (NCI-H2030, CFPAC-1, …) | top dose only |  |
| [[Sodium Salicylate (drug)]] 5 µM |  | 0.906× | -3.1 | 0.19 | 5/48 (NCI-H661, H4, …) | rises with dose |  |
| [[Acetohexamide (drug)]] 5 µM |  | 0.910× | -3.0 | 0.24 | 8/48 (NCI-H661, PANC-1, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.14 per unit of S-phase module lfc, +0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12809. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 21.2 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.17× (z +17.9) | — |
| [[PANC-1 (line)]] | alt | 15.6 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.33× (z +15.9) | [[Selinexor (drug)]] 5 µM 0.462× (z -10.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 12.3 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.92× (z +16.2) | — |
| [[HEC-1-A (line)]] | alt | 14.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.36× (z +13.3) | — |
| [[hTERT-HPNE (line)]] | wt | 10.9 | 0 | 2 | — | [[Menadione (drug)]] 0.05 µM 0.0872× (z -9.6) |
| [[NCI-H1573 (line)]] | alt | 18.6 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.52× (z +10.4) | — |
| [[BT-474 (line)]] | alt | 14.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.11× (z +8.6) | — |
| [[H4 (line)]] | wt | 14.1 | 0 | 1 | — | [[Saquinavir (drug)]] 5 µM 0.252× (z -8.9) |
| [[HepG2_C3A (line)]] | wt | 33.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.17× (z +13.5) | — |
| [[J82 (line)]] | alt | 22.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.56× (z +14.5) | — |
| [[NCI-H2347 (line)]] | alt | 12.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.81× (z +11.1) | — |
| [[NCI-H460 (line)]] | wt | 16.7 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.73× (z +8.7) | — |
| [[SNU-1 (line)]] | wt | 18.7 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.137× (z -9.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SNU-423 (line)]] | alt | 17.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.96× (z +9.8) | — |
| [[A-427 (line)]] | wt | 17.3 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 13.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 20.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 26.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 21.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 11.3 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 16.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 32.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 28.8 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 29.2 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 26.6 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 14.1 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 12.2 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 12.4 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 18.2 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 23.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 21.4 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 22.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 24.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 19.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 44.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 13.2 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 24.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12809), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*68 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RAB8A]] | +0.55 | +0.47 / +0.51 | both halves | 2e-05 |  |
| [[JUNB]] | +0.55 | +0.55 / +0.50 | both halves | 1e-05 |  |
| [[KLF4]] | +0.55 | +0.52 / +0.56 | both halves | 1e-05 |  |
| [[SLC39A1]] | +0.54 | +0.56 / +0.41 | both halves | 4e-05 |  |
| [[BLOC1S3]] | +0.54 | +0.49 / +0.47 | both halves | 2e-05 |  |
| [[ZNF335]] | +0.54 | +0.50 / +0.50 | both halves | 1e-05 |  |
| [[CDKN2AIP]] | +0.53 | +0.46 / +0.54 | both halves | 2e-05 |  |
| [[SGK1]] | +0.53 | +0.53 / +0.47 | both halves | 2e-05 |  |
| [[ZC3H11A]] | +0.53 | +0.50 / +0.51 | both halves | 1e-05 |  |
| [[SERTAD1]] | +0.53 | +0.56 / +0.45 | both halves | 3e-05 |  |
| [[IBA57]] | +0.53 | +0.60 / +0.39 | both halves | 5e-05 |  |
| [[DPH1-AS1]] | +0.52 | +0.52 / +0.44 | both halves | 3e-05 |  |

## Genes that move opposite

*32 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FAR1]] | -0.57 | -0.58 / -0.46 | both halves | 2e-05 |  |
| [[SNX4]] | -0.57 | -0.56 / -0.49 | both halves | 2e-05 |  |
| [[MBD2]] | -0.55 | -0.56 / -0.49 | both halves | 1e-05 |  |
| [[NAPB]] | -0.55 | -0.55 / -0.45 | both halves | 3e-05 | pathway: Intra-Golgi and retrograde Golgi-to-ER traffic; STRING 501 |
| [[MFSD14B]] | -0.54 | -0.51 / -0.54 | both halves | 1e-05 |  |
| [[HDAC2]] | -0.53 | -0.45 / -0.52 | both halves | 3e-05 |  |
| [[RTCA]] | -0.51 | -0.52 / -0.44 | both halves | 3e-05 |  |
| [[RAB18]] | -0.51 | -0.54 / -0.46 | both halves | 3e-05 | pathway: Intra-Golgi and retrograde Golgi-to-ER traffic |
| [[SACM1L]] | -0.51 | -0.49 / -0.42 | both halves | 4e-05 |  |
| [[NAP1L4]] | -0.50 | -0.52 / -0.45 | both halves | 3e-05 |  |
| [[OLA1]] | -0.50 | -0.50 / -0.37 | both halves | 8e-05 |  |
| [[REPS1]] | -0.50 | -0.54 / -0.40 | both halves | 5e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 188]]; 18 genes; every member is in the + arm (projection on the module's main direction -0.563). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.45; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-8.6, -10.6); signed map (4.6, 22.3). **Vector** length 64.5, 9.72% of its response variance represented; |z| ≥ 3 in 968 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM |  | +4.3 | +14.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | +3.3 | +12.8 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +3.1 | +14.4 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +2.9 | +6.4 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | +2.8 | +9.4 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +1.6 | +3.4 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.4 | +0.8 |
|  | [[Omeprazole (drug)]] 0.05 µM |  | +1.4 | +1.0 |
|  | [[Gefitinib (drug)]] 5 µM |  | +1.4 | +2.5 |
|  | [[Entrectinib (drug)]] 5 µM |  | +1.3 | +2.2 |
| fall | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -3.1 | -4.0 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.6 | -5.5 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -2.6 | -1.9 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.5 | -0.8 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.8 | -1.4 |
|  | [[Brivudine (drug)]] 0.5 µM |  | -1.3 | -2.0 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -1.2 | +0.1 |
|  | [[Neratinib (drug)]] 5 µM |  | -1.2 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | SYS1 golgi trafficking protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20q13.12 — chr20:45,361,937-45,376,798 (+) |
| Ensembl biotype | protein_coding |
| Also known as | dJ453C12.4; previously C20orf169 |
| Reactome | 4 pathways, smallest: Retrograde transport at the Trans-Golgi-Network; Intra-Golgi and retrograde Golgi-to-ER traffic; Membrane Trafficking |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8N2H4](https://www.uniprot.org/uniprotkb/Q8N2H4) (Protein SYS1 homolog):

> Involved in protein trafficking. May serve as a receptor for ARFRP1.

**Summary**, from NCBI Gene [90196](https://www.ncbi.nlm.nih.gov/gene/90196):

> SYS1 forms a complex with ADP-ribosylation factor-related protein ARFRP1 (MIM 604699) and targets ARFRP1 to the Golgi apparatus (Behnia et al., 2004 [PubMed 15077113]).[supplied by OMIM, Aug 2009]

**Accessions** — [HGNC:16162](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16162) · Entrez [90196](https://www.ncbi.nlm.nih.gov/gene/90196) · UniProt [Q8N2H4](https://www.uniprot.org/uniprotkb/Q8N2H4) · Ensembl [ENSG00000204070](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000204070)

## Data

Gene col 12809: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12809); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12809, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12809]; `tensor/DDL_lfc|DDL_z.npy` [12809]; `embed/gene_vectors.npy` [12809]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12809 or target_col == 12809). Every well: [[SYS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SYS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
