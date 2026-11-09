---
symbol: "FHIP2B"
type: "gene"
col: 8200
ensembl_id: "ENSG00000158863"
name: "FHF complex subunit HOOK interacting protein 2B"
location: "8p21.3"
module: 2
arm: "+"
pooled_cpm: 16.39
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 17
n_dd_up_clean: 4
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/002"]
generated_by: "tahoemap"
---

# FHIP2B

*FHF complex subunit HOOK interacting protein 2B* — 8p21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (1 with an alert ⚠); the strongest is [[Ipatasertib (drug)]] 0.5 µM: 1.61× (z +4.7, q 0.001, up in 28 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.577× (z -10.6, q 2e-23, down in 31 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF598]] (+0.61, fdr 7e-06), [[PLA2G4B]] (+0.61, fdr 7e-06), [[SLC39A13]] (+0.61, fdr 7e-06); moves opposite to [[YWHAE]] (-0.53, fdr 1e-05), [[YWHAZ]] (-0.53, fdr 5e-05), [[LEPROT]] (-0.52, fdr 1e-05).
> It sits in the **+** arm of [[Module 002]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 1 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8200.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.61×** | +4.7 | 0.001 | 28/44 (KATO III, LOX-IMVI, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Celecoxib (drug)]] 0.5 µM |  | **1.57×** | +4.5 | 0.002 | 17/47 (NCI-H2030, NCI-H460, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.48×** | +3.9 | 0.018 | 14/44 (MIA PaCa-2, A498, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.46×** | +3.7 | 0.027 | 15/46 (SW480, SK-MEL-2, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **1.85×** | +3.4 | 0.089 | 8/33 (MIA PaCa-2, J82, …) | top dose only | noisy plate (z scaled) |
| [[PH-797804 (drug)]] 0.5 µM |  | 1.36× | +3.0 | 0.22 | 7/45 (AsPC-1, LOX-IMVI, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 8 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8200.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.577×** | -10.6 | 2e-23 | 31/47 (A-172, HS-578T, …) | rises with dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.530×** | -9.1 | 3e-17 | 40/48 (A549, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.563×** | -8.2 | 3e-14 | 30/46 (C32, SW48, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM |  | **0.577×** | -7.9 | 5e-13 | 34/47 (NCI-H23, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~22% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.240×** | -7.8 | 6e-13 | 31/48 (MIA PaCa-2, LOX-IMVI, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~5% here); composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.604×** | -7.2 | 5e-11 | 33/48 (NCI-H23, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **0.647×** | -5.7 | 8e-07 | 16/35 (NCI-H460, PANC-1, …) | inconsistent across doses | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.668×** | -5.6 | 2e-06 | 24/44 (Panc 03.27, C-33 A, …) | top dose only | cell-cycle shift (explains ~20% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.695×** | -5.0 | 3e-05 | 20/47 (HS-578T, LoVo, …) | rises with dose | cell-cycle shift (explains ~19% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | **0.705×** | -4.8 | 8e-05 | 13/30 (NCI-H460, NCI-H1792, …) | inconsistent across doses | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.669×** | -4.5 | 3e-04 | 21/47 (HS-578T, A498, …) | rises with dose | cell-cycle shift (explains ~2% here); noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.444×** | -4.5 | 4e-04 | 21/44 (HOP62, PANC-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.741×** | -4.3 | 8e-04 | 19/47 (NCI-H460, SW480, …) | two highest doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.759×** | -4.0 | 0.003 | 16/48 (AN3 CA, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~12% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | 0.838× | -3.3 | 0.035 | 19/47 (J82, HS-578T, …) | top dose only |  |
| [[Benproperine (phosphate) (drug)]] 0.05 µM |  | **0.797×** | -3.0 | 0.082 | 8/47 (HEC-1-A, LS 180, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.21 per unit of S-phase module lfc, -0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8200. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[J82 (line)]] | alt | 6.53 | 0 | 3 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0980× (z -11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~68% of this change |
| [[NCI-H460 (line)]] | wt | 11.8 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.224× (z -10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change |
| [[Hs 766T (line)]] | wt | 16.1 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.144× (z -11.3) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[NCI-H1573 (line)]] | alt | 16.9 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.143× (z -12.4) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.305× (z -10.0) |
| [[A-172 (line)]] | wt | 26.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.298× (z -12.0) |
| [[A-427 (line)]] | wt | 22.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.254× (z -10.4) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[A549 (line)]] | wt | 24.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.253× (z -10.3) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[HS-578T (line)]] | alt | 28.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.320× (z -11.4) |
| [[LOX-IMVI (line)]] | wt | 12.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.269× (z -10.5) |
| [[MIA PaCa-2 (line)]] | alt | 28.1 | 0 | 1 | — | [[TAK-901 (drug)]] 5 µM 0.0520× (z -9.4) |
| [[NCI-H1792 (line)]] | alt | 16.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.160× (z -10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change |
| [[NCI-H23 (line)]] | alt | 21.2 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.238× (z -9.3) |
| [[NCI-H2347 (line)]] | alt | 21.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.398× (z -9.7) |
| [[Panc 03.27 (line)]] | alt | 12.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.182× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SW 900 (line)]] | alt | 17.4 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.185× (z -9.1) ⚠ cell-cycle shift, explains ~38% of this change |
| [[A498 (line)]] | wt | 25.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 20.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 20.7 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 24.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 8.87 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 7.05 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 16.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 8.39 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 17.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 13.9 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 5.70 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 22.1 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 17.4 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 15.6 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 21.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 20.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 7.72 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 24.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 21.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 20.8 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 8.66 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 8.07 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 18.6 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 12.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8200), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF598]] | +0.61 | +0.61 / +0.67 | both halves | 7e-06 |  |
| [[PLA2G4B]] | +0.61 | +0.59 / +0.58 | both halves | 7e-06 |  |
| [[SLC39A13]] | +0.61 | +0.59 / +0.61 | both halves | 7e-06 |  |
| [[ARFGAP1]] | +0.60 | +0.65 / +0.60 | both halves | 7e-06 |  |
| [[MAP2K2]] | +0.59 | +0.59 / +0.60 | both halves | 7e-06 |  |
| [[RNF166]] | +0.59 | +0.39 / +0.64 | both halves | 5e-05 |  |
| [[UCKL1]] | +0.59 | +0.67 / +0.53 | both halves | 1e-05 |  |
| [[NSUN5P1-1]] | +0.57 | +0.55 / +0.53 | both halves | 1e-05 |  |
| [[SDHAP1-1]] | +0.57 | +0.62 / +0.52 | both halves | 1e-05 |  |
| [[CDC34]] | +0.57 | +0.60 / +0.64 | both halves | 7e-06 |  |
| [[FXR2]] | +0.56 | +0.50 / +0.57 | both halves | 1e-05 |  |
| [[TAF12]] | +0.56 | +0.35 / +0.62 | both halves | 1e-04 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[YWHAE]] | -0.53 | -0.49 / -0.58 | both halves | 1e-05 |  |
| [[YWHAZ]] | -0.53 | -0.39 / -0.53 | both halves | 5e-05 |  |
| [[LEPROT]] | -0.52 | -0.53 / -0.51 | both halves | 1e-05 |  |
| [[ATP7A]] | -0.51 | -0.49 / -0.53 | both halves | 1e-05 |  |
| [[FAHD1]] | -0.50 | -0.54 / -0.39 | both halves | 5e-05 |  |
| [[NXT2]] | -0.49 | -0.46 / -0.55 | both halves | 2e-05 |  |
| [[DNAH7]] | -0.49 | -0.54 / -0.37 | both halves | 8e-05 |  |
| [[STAG2]] | -0.47 | -0.39 / -0.49 | both halves | 6e-05 | same gene group |
| [[CUL4B]] | -0.47 | -0.33 / -0.51 | both halves | 1e-04 |  |
| [[EID1]] | -0.47 | -0.41 / -0.46 | both halves | 4e-05 |  |
| [[CHRAC1]] | -0.47 | -0.38 / -0.53 | both halves | 6e-05 |  |
| [[ABLIM1]] | -0.47 | -0.36 / -0.49 | both halves | 9e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 002]]; 248 genes; this gene is in the **+** arm (projection on the module's main direction 0.487). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.21).
- **Nodal map** (x, y) = (-10.3, -23.5); signed map (-27.6, 1.4). **Vector** length 76.1, 15.2% of its response variance represented; |z| ≥ 3 in 713 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ipatasertib (drug)]] 0.5 µM |  | +3.8 | +4.7 |
|  | [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | +2.9 | +3.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.6 | +0.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | +2.6 | +2.7 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +2.5 | +3.7 |
|  | [[Thymol (drug)]] 0.5 µM |  | +2.4 | +2.4 |
|  | [[Celecoxib (drug)]] 0.5 µM |  | +2.4 | +4.5 |
| fall | [[Auranofin (drug)]] 5 µM |  | -3.9 | -8.2 |
|  | [[TAK-901 (drug)]] 5 µM |  | -3.8 | -7.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.5 | -4.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | -2.4 | -5.7 |
|  | [[Afatinib (drug)]] 0.5 µM |  | -2.2 | -1.6 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -2.2 | -1.7 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | -2.1 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | FHF complex subunit HOOK interacting protein 2B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8p21.3 — chr8:22,089,150-22,104,911 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ21801; previously RAI16, FAM160B2 |
| Gene groups (HGNC) | Armadillo like helical domain containing; FHF complex |
| Matched by | ensembl_id |

**Function**, from UniProt [Q86V87](https://www.uniprot.org/uniprotkb/Q86V87) (FHF complex subunit HOOK-interacting protein 2B):

> Able to activate MAPK/ERK and TGFB signaling pathways. May regulate the activity of genes involved in intestinal barrier function and immunoprotective inflammation (By similarity). May play a role in cell proliferation.

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:16492](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16492) · Entrez [64760](https://www.ncbi.nlm.nih.gov/gene/64760) · UniProt [Q86V87](https://www.uniprot.org/uniprotkb/Q86V87) · Ensembl [ENSG00000158863](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000158863)

## Data

Gene col 8200: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8200); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8200, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8200]; `tensor/DDL_lfc|DDL_z.npy` [8200]; `embed/gene_vectors.npy` [8200]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8200 or target_col == 8200). Every well: [[FHIP2B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FHIP2B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
