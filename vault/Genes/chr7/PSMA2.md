---
symbol: "PSMA2"
type: "gene"
col: 2777
ensembl_id: "ENSG00000106588"
name: "proteasome 20S subunit alpha 2"
location: "7p14.1"
module: 72
arm: "+"
pooled_cpm: 70.5
n_lines_expressing: 50
n_dd_up: 23
n_dd_down: 1
n_dd_up_clean: 10
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/072"]
generated_by: "tahoemap"
---

# PSMA2

*proteasome 20S subunit alpha 2* — 7p14.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (13 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 0.5 µM: 3.08× (z +11.2, q 3e-26, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.766× (z -3.8, q 0.096, down in 32 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (AN3 CA 0.317×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PSMB3]] (+0.74, fdr 7e-06), [[PSMA6]] (+0.71, fdr 7e-06), [[PSMB4]] (+0.68, fdr 7e-06); moves opposite to [[THOC6]] (-0.52, fdr 6e-05), [[KDM6B]] (-0.50, fdr 3e-05), [[ENTR1]] (-0.49, fdr 4e-05).
> It is in [[Module 072]], a single-armed module (Degradation of DVL).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 13 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2777.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **3.08×** | +11.2 | 3e-26 | 48/48 (NCI-H460, HOP62, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **3.03×** | +11.0 | 8e-26 | 48/48 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **2.38×** | +8.1 | 8e-14 | 48/48 (AsPC-1, HT-29, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~75% of this change | **1.83×** | +6.0 | 3e-07 | 35/49 (PANC-1, J82, …) | all doses, stronger at high dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~46% of this change | **1.68×** | +5.2 | 3e-05 | 42/47 (AsPC-1, NCI-H1792, …) | inconsistent across doses | low cells (technical?) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~66% of this change | **1.60×** | +4.7 | 3e-04 | 35/48 (PANC-1, HOP62, …) | top dose only | position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~83% of this change | **1.62×** | +4.6 | 3e-04 | 28/43 (C-33 A, NCI-H1573, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.57×** | +4.5 | 5e-04 | 32/48 (NCI-H1573, PANC-1, …) | two highest doses | position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~52% of this change | **1.53×** | +4.1 | 0.003 | 33/47 (LoVo, HepG2/C3A, …) | top dose only |  |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.96×** | +4.0 | 0.004 | 41/48 (NCI-H2347, HEC-1-A, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **2.78×** | +3.9 | 0.006 | 35/49 (PANC-1, SW480, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~23% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~87% of this change | **1.45×** | +3.7 | 0.009 | 31/48 (PANC-1, KATO III, …) | rises with dose | composition shift |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.85×** | +3.6 | 0.013 | 36/49 (AsPC-1, NCI-H460, …) | all doses, flat | noisy plate (z scaled) |
| [[vincristine (drug)]] 0.5 µM |  | **1.78×** | +3.4 | 0.030 | 36/48 (HEC-1-A, HOP62, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.76×** | +3.3 | 0.034 | 35/47 (J82, AsPC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.38×** | +3.2 | 0.041 | 29/48 (C32, PANC-1, …) | top dose only |  |
| [[TAK-901 (drug)]] 0.5 µM |  | **1.63×** | +2.9 | 0.096 | 24/48 (MIA PaCa-2, PANC-1, …) | rises with dose | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 2777.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (AN3 CA 0.317×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.766×** | -3.8 | 0.096 | 32/48 (AN3 CA, SW480, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.37 per unit of S-phase module lfc, +0.38 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2777. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 77.7 | 4 (2 ⚠) | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 4.04× (z +11.3) | — |
| [[C32 (line)]] | wt | 35.4 | 2 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 4.65× (z +9.4) | — |
| [[COLO 205 (line)]] | alt | 37.7 | 2 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 5.27× (z +9.6) | — |
| [[H4 (line)]] | wt | 112 | 2 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 4.03× (z +9.1) | — |
| [[HEC-1-A (line)]] | alt | 76.7 | 2 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 3.19× (z +9.7) | — |
| [[HOP62 (line)]] | alt | 44.3 | 2 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 4.72× (z +11.4) | — |
| [[HT-29 (line)]] | alt | 69.1 | 2 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 4.45× (z +10.6) | — |
| [[hTERT-HPNE (line)]] | wt | 43.0 | 2 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 4.42× (z +8.9) | — |
| [[KATO III (line)]] | alt | 107 | 2 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 3.53× (z +10.0) | — |
| [[LoVo (line)]] | wt | 65.3 | 2 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 3.33× (z +9.2) | — |
| [[LOX-IMVI (line)]] | wt | 46.8 | 2 | 0 | [[Ixazomib citrate (drug)]] 5 µM 4.20× (z +9.8) | — |
| [[NCI-H1573 (line)]] | alt | 29.3 | 2 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 4.99× (z +10.2) | — |
| [[NCI-H2030 (line)]] | alt | 86.7 | 2 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 3.19× (z +9.1) | — |
| [[NCI-H23 (line)]] | alt | 69.9 | 2 | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.28× (z +8.8) | — |
| [[NCI-H460 (line)]] | wt | 54.8 | 2 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 4.31× (z +11.9) | — |
| [[SW480 (line)]] | alt | 84.6 | 2 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 3.23× (z +9.8) | — |
| [[A-427 (line)]] | wt | 90.7 | 1 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 2.88× (z +8.5) | — |
| [[AN3 CA (line)]] | alt | 113 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.317× (z -10.1) |
| [[C-33 A (line)]] | alt | 52.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.13× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~83% of this change | — |
| [[CFPAC-1 (line)]] | alt | 51.5 | 1 | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.33× (z +9.1) | — |
| [[Hs 766T (line)]] | wt | 58.8 | 1 | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.59× (z +8.8) | — |
| [[RPMI-7951 (line)]] | alt | 80.3 | 1 | 0 | [[Ixazomib citrate (drug)]] 5 µM 4.05× (z +10.1) | — |
| [[SK-MEL-2 (line)]] | alt | 57.3 | 1 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 3.21× (z +8.5) | — |
| [[SNU-1 (line)]] | wt | 60.0 | 1 | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.76× (z +8.8) | — |
| [[SNU-423 (line)]] | alt | 59.4 | 1 | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.64× (z +9.4) | — |
| [[A-172 (line)]] | wt | 98.7 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 132 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 60.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 67.4 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 84.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 56.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 53.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 42.7 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 77.6 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 54.1 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 66.1 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 71.2 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 39.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 50.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 84.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 61.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 76.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 70.4 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 64.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 72.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 79.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 55.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 66.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 85.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 84.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2777), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PSMB3]] | +0.74 | +0.77 / +0.66 | both halves | 7e-06 | same gene group; pathway: HALLMARK_MYC_TARGETS_V1; STRING 999 |
| [[PSMA6]] | +0.71 | +0.72 / +0.68 | both halves | 7e-06 | same gene group; pathway: HALLMARK_MYC_TARGETS_V1; STRING 999 |
| [[PSMB4]] | +0.68 | +0.68 / +0.64 | both halves | 7e-06 | same gene group; pathway: ABC transporter disorders; STRING 999 |
| [[PSMC6]] | +0.67 | +0.65 / +0.65 | both halves | 7e-06 | same gene group; pathway: HALLMARK_MYC_TARGETS_V1; STRING 999 |
| [[PSMB2]] | +0.65 | +0.79 / +0.54 | both halves | 1e-05 | same gene group; pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE; STRING 999 |
| [[NDUFS8]] | +0.65 | +0.58 / +0.61 | both halves | 7e-06 |  |
| [[TXNL1]] | +0.63 | +0.63 / +0.59 | both halves | 7e-06 |  |
| [[NDUFAB1]] | +0.62 | +0.64 / +0.57 | both halves | 1e-05 | pathway: HALLMARK_MYC_TARGETS_V1 |
| [[ZNF277]] | +0.60 | +0.57 / +0.52 | both halves | 1e-05 |  |
| [[PSMA3]] | +0.60 | +0.65 / +0.59 | both halves | 7e-06 | same gene group; pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE; STRING 999 |
| [[ANKRD39]] | +0.60 | +0.61 / +0.47 | both halves | 2e-05 |  |
| [[CENPX]] | +0.58 | +0.54 / +0.59 | both halves | 1e-05 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[THOC6]] | -0.52 | -0.38 / -0.51 | both halves | 6e-05 |  |
| [[KDM6B]] | -0.50 | -0.48 / -0.45 | both halves | 3e-05 |  |
| [[ENTR1]] | -0.49 | -0.48 / -0.42 | both halves | 4e-05 |  |
| [[SRRM2]] | -0.48 | -0.41 / -0.39 | both halves | 5e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 072]] — Degradation of DVL; 69 genes; every member is in the + arm (projection on the module's main direction 0.698). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-15.4, -10.0); signed map (-26.6, -24.1). **Vector** length 92.4, 34.9% of its response variance represented; |z| ≥ 3 in 671 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 5 µM |  | +8.9 | +11.0 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +8.9 | +8.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +8.8 | +11.2 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic | +4.3 | +2.9 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +3.6 | +3.6 |
|  | [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | +2.8 | +2.3 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +2.2 | +3.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.2 | +2.6 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -6.1 | -3.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | -3.3 | +2.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -3.3 | +2.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~83% of this change | -2.9 | +4.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.7 | +0.9 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | -1.9 | -1.5 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.9 | -0.4 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -1.7 | +0.0 |
|  | [[Hydroxyurea (drug)]] 5 µM |  | -1.6 | -2.0 |
|  | [[Decitabine (drug)]] 5 µM |  | -1.5 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | proteasome 20S subunit alpha 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7p14.1 — chr7:42,916,828-42,932,185 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MU, HC3, PMSA2 |
| Gene groups (HGNC) | Proteasome |
| Hallmark sets | INTERFERON_GAMMA_RESPONSE, MYC_TARGETS_V1 |
| Reactome | 171 pathways, smallest: Antigen processing: Ub, ATP-independent proteasomal degradation; Regulation of activated PAK-2p34 by proteasome mediated degradation; Regulation of ornithine decarboxylase (ODC) |
| Matched by | ensembl_id |

**Function**, from UniProt [P25787](https://www.uniprot.org/uniprotkb/P25787) (Proteasome subunit alpha type-2):

> Component of the 20S core proteasome complex involved in the proteolytic degradation of most intracellular proteins. This complex plays numerous essential roles within the cell by associating with different regulatory particles. Associated with two 19S regulatory particles, forms the 26S proteasome and thus participates in the ATP-dependent degradation of ubiquitinated proteins. The 26S proteasome plays a key role in the maintenance of protein homeostasis by removing misfolded or damaged …

**Summary**, from NCBI Gene [5683](https://www.ncbi.nlm.nih.gov/gene/5683):

> The proteasome is a multicatalytic proteinase complex with a highly ordered ring-shaped 20S core structure. The core structure is composed of 4 rings of 28 non-identical subunits; 2 rings are composed of 7 alpha subunits and 2 rings are composed of 7 beta subunits. Proteasomes are distributed throughout eukaryotic cells at a high concentration and cleave peptides in an ATP/ubiquitin-dependent process in a non-lysosomal pathway. An essential function of a modified proteasome, the …

**Accessions** — [HGNC:9531](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9531) · Entrez [5683](https://www.ncbi.nlm.nih.gov/gene/5683) · UniProt [P25787](https://www.uniprot.org/uniprotkb/P25787) · Ensembl [ENSG00000106588](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000106588)

## Data

Gene col 2777: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2777); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2777, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2777]; `tensor/DDL_lfc|DDL_z.npy` [2777]; `embed/gene_vectors.npy` [2777]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2777 or target_col == 2777). Every well: [[PSMA2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PSMA2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
