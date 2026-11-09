---
symbol: "MAEA"
type: "gene"
col: 1617
ensembl_id: "ENSG00000090316"
name: "macrophage erythroblast attacher, E3 ubiquitin ligase"
location: "4p16.3"
module: 83
arm: "+"
pooled_cpm: 34.3
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 2
n_dd_up_clean: 10
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/083"]
generated_by: "tahoemap"
---

# MAEA

*macrophage erythroblast attacher, E3 ubiquitin ligase* — 4p16.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.70× (z +10.6, q 3e-23, up in 33 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (2 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.683× (z -5.1, q 2e-04, down in 22 of 38 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 1 line (NCI-H1573 0.141×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change); [[Selinexor (drug)]] 0.5 µM in 1 line (Hs 766T 0.213×); [[Imiquimod (hydrochloride) (drug)]] 5 µM in 1 line (hTERT-HPNE 0.193×; ⚠ toxic).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PIGG]] (+0.68, fdr 7e-06), [[ACAD9]] (+0.67, fdr 1e-05), [[PSKH1]] (+0.66, fdr 1e-05); moves opposite to [[DENND4C]] (-0.60, fdr 1e-05), [[PGAP1]] (-0.60, fdr 1e-05), [[PAFAH1B3]] (-0.60, fdr 3e-05).
> It sits in the **+** arm of [[Module 083]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 1 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1617.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.70×** | +10.6 | 3e-23 | 33/47 (LOX-IMVI, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **3.88×** | +10.0 | 5e-21 | 44/49 (SW480, NCI-H23, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **3.37×** | +8.9 | 8e-17 | 41/48 (SW480, NCI-H1573, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.81×** | +8.4 | 7e-15 | 34/47 (SW480, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.34×** | +5.9 | 5e-07 | 30/48 (NCI-H2347, AsPC-1, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.47×** | +5.4 | 6e-06 | 35/48 (NCI-H2030, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.39×** | +4.6 | 3e-04 | 28/48 (SW480, PANC-1, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.38×** | +4.5 | 4e-04 | 30/47 (PANC-1, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.36×** | +4.3 | 9e-04 | 26/48 (A-172, RPMI-7951, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.33×** | +3.9 | 0.005 | 22/47 (SK-MEL-2, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.25×** | +3.2 | 0.070 | 13/47 (HT-29, NCI-H1573, …) | rises with dose | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 2 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1617.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 1 line (NCI-H1573 0.141×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change); [[Selinexor (drug)]] 0.5 µM in 1 line (Hs 766T 0.213×); [[Imiquimod (hydrochloride) (drug)]] 5 µM in 1 line (hTERT-HPNE 0.193×; ⚠ toxic).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **0.683×** | -5.1 | 2e-04 | 22/38 (NCI-H1573, LoVo, …) | rises with dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | **0.752×** | -4.0 | 0.018 | 21/44 (LS 180, HT-29, …) | rises with dose | composition shift |
| [[Arbutin (drug)]] 5 µM |  | 0.798× | -3.0 | 0.45 | 14/47 (A498, J82, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.11 per unit of S-phase module lfc, -0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1617. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 37.0 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.59× (z +13.5) | — |
| [[NCI-H2030 (line)]] | alt | 24.2 | 3 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 5.61× (z +12.3) | — |
| [[LOX-IMVI (line)]] | wt | 45.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.59× (z +17.9) | — |
| [[NCI-H1573 (line)]] | alt | 48.9 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 3.34× (z +9.5) | [[Dinaciclib (drug)]] 5 µM 0.141× (z -14.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[NCI-H23 (line)]] | alt | 41.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.25× (z +16.4) | — |
| [[NCI-H460 (line)]] | wt | 25.1 | 2 | 0 | [[Homoharringtonine (drug)]] 0.05 µM 3.20× (z +10.4) | — |
| [[A-172 (line)]] | wt | 34.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.57× (z +11.1) | — |
| [[A-427 (line)]] | wt | 43.2 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 4.48× (z +12.5) | — |
| [[A549 (line)]] | wt | 28.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.38× (z +9.1) | — |
| [[AsPC-1 (line)]] | alt | 38.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.78× (z +11.4) | — |
| [[C32 (line)]] | wt | 28.0 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.54× (z +8.5) | — |
| [[CFPAC-1 (line)]] | alt | 36.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.11× (z +8.8) | — |
| [[HOP62 (line)]] | alt | 37.3 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 7.13× (z +8.6) | — |
| [[Hs 766T (line)]] | wt | 23.9 | 0 | 1 | — | [[Selinexor (drug)]] 0.5 µM 0.213× (z -10.0) |
| [[HT-29 (line)]] | alt | 58.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.29× (z +9.9) | — |
| [[hTERT-HPNE (line)]] | wt | 29.2 | 0 | 1 (1 ⚠) | — | [[Imiquimod (hydrochloride) (drug)]] 5 µM 0.193× (z -9.4) ⚠ toxic |
| [[LS 180 (line)]] | wt | 42.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.366× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change |
| [[MIA PaCa-2 (line)]] | alt | 27.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.67× (z +14.9) | — |
| [[NCI-H1792 (line)]] | alt | 27.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.42× (z +8.6) | — |
| [[PANC-1 (line)]] | alt | 31.6 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.89× (z +9.9) | — |
| [[A498 (line)]] | wt | 39.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 35.9 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 30.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 39.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 34.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 42.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 35.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 44.2 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 35.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 25.4 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 24.3 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 56.4 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 35.2 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 32.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 33.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 35.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 33.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 23.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 30.2 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 28.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 24.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 32.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 25.8 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 28.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 25.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 37.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 31.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 24.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 33.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1617), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*77 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PIGG]] | +0.68 | +0.62 / +0.63 | both halves | 7e-06 |  |
| [[ACAD9]] | +0.67 | +0.58 / +0.52 | both halves | 1e-05 | pathway: Aerobic respiration and respiratory electron transport |
| [[PSKH1]] | +0.66 | +0.51 / +0.58 | both halves | 1e-05 |  |
| [[LTO1]] | +0.66 | +0.53 / +0.53 | both halves | 1e-05 |  |
| [[TSTD2]] | +0.65 | +0.52 / +0.57 | both halves | 1e-05 |  |
| [[PTCD1]] | +0.64 | +0.62 / +0.44 | both halves | 3e-05 |  |
| [[MAPKAPK5]] | +0.62 | +0.55 / +0.48 | both halves | 2e-05 |  |
| [[ZNF26]] | +0.61 | +0.54 / +0.52 | both halves | 1e-05 |  |
| [[SMIM15-AS1]] | +0.60 | +0.45 / +0.49 | both halves | 3e-05 |  |
| [[CTBP1]] | +0.60 | +0.61 / +0.55 | both halves | 1e-05 | ⚠ same locus (39.6 kb: neighbours can correlate without regulation) |
| [[BRD1]] | +0.59 | +0.43 / +0.55 | both halves | 3e-05 |  |
| [[UBAP1L]] | +0.59 | +0.53 / +0.46 | both halves | 3e-05 |  |
| [[CHTF8]] | +0.58 | +0.54 / +0.35 | both halves | 1e-04 |  |

## Genes that move opposite

*23 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DENND4C]] | -0.60 | -0.51 / -0.67 | both halves | 1e-05 |  |
| [[PGAP1]] | -0.60 | -0.55 / -0.49 | both halves | 1e-05 |  |
| [[PAFAH1B3]] | -0.60 | -0.46 / -0.44 | both halves | 3e-05 |  |
| [[HPF1]] | -0.59 | -0.26 / -0.59 | both halves | 3e-04 |  |
| [[SPATA6]] | -0.56 | -0.41 / -0.45 | both halves | 4e-05 |  |
| [[RALGAPA2]] | -0.56 | -0.46 / -0.43 | both halves | 3e-05 |  |
| [[NUP62CL]] | -0.56 | -0.51 / -0.46 | both halves | 3e-05 |  |
| [[PCCA]] | -0.55 | -0.33 / -0.51 | both halves | 1e-04 |  |
| [[ARL15]] | -0.53 | -0.46 / -0.59 | both halves | 3e-05 |  |
| [[HMGN3]] | -0.52 | -0.45 / -0.38 | both halves | 7e-05 |  |
| [[CDC73]] | -0.52 | -0.46 / -0.46 | both halves | 3e-05 |  |
| [[FAM102B]] | -0.52 | -0.55 / -0.33 | both halves | 1e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 083]]; 53 genes; this gene is in the **+** arm (projection on the module's main direction 0.682). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.40).
- **Nodal map** (x, y) = (-7.5, 18.6); signed map (28.6, -19.7). **Vector** length 85.2, 18.3% of its response variance represented; |z| ≥ 3 in 913 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.4 | +5.9 |
|  | [[TAK-901 (drug)]] 5 µM |  | +5.5 | +10.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.6 | +4.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.5 | +8.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +3.9 | +2.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.7 | +1.8 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +2.9 | +2.8 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.9 | +2.9 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -3.2 | -1.9 |
|  | [[Selinexor (drug)]] 0.5 µM |  | -3.1 | -2.6 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -2.9 | -0.7 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.8 | -2.4 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.6 | -1.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.5 | -2.7 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.0 | -1.6 |
|  | [[Arbutin (drug)]] 5 µM |  | -2.0 | -3.0 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.7 | -1.1 |
|  | [[EX229 (drug)]] 5 µM |  | -1.6 | -0.5 |

## What is on record

|  |  |
|---|---|
| Name | macrophage erythroblast attacher, E3 ubiquitin ligase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4p16.3 — chr4:1,289,887-1,340,147 (+) |
| Ensembl biotype | protein_coding |
| Also known as | EMP, GID9, p44EMLP, HLC-10 |
| Gene groups (HGNC) | U-box domain containing; CTLH complex subunits |
| Reactome | 3 pathways, smallest: Regulation of pyruvate metabolism; Pyruvate metabolism; Aerobic respiration and respiratory electron transport |
| Matched by | ensembl_id |

**Function**, from UniProt [Q7L5Y9](https://www.uniprot.org/uniprotkb/Q7L5Y9) (E3 ubiquitin-protein transferase MAEA):

> Core component of the CTLH E3 ubiquitin-protein ligase complex that selectively accepts ubiquitin from UBE2H and mediates ubiquitination and subsequent proteasomal degradation of the transcription factor HBP1. MAEA and RMND5A are both required for catalytic activity of the CTLH E3 ubiquitin-protein ligase complex. MAEA is required for normal cell proliferation. The CTLH E3 ubiquitin-protein ligase complex is not required for the degradation of enzymes involved in gluconeogenesis, such as FBP1. …

**Summary**, from NCBI Gene [10296](https://www.ncbi.nlm.nih.gov/gene/10296):

> This gene encodes a protein that mediates the attachment of erythroblasts to macrophages. This attachment promotes terminal maturation and enucleation of erythroblasts, presumably by suppressing apoptosis. The encoded protein is an integral membrane protein with the N-terminus on the extracellular side and the C-terminus on the cytoplasmic side of the cell. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Jul 2014]

**Accessions** — [HGNC:13731](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13731) · Entrez [10296](https://www.ncbi.nlm.nih.gov/gene/10296) · UniProt [Q7L5Y9](https://www.uniprot.org/uniprotkb/Q7L5Y9) · Ensembl [ENSG00000090316](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000090316)

## Data

Gene col 1617: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1617); `tables/drug_effects.parquet` (14 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1617, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1617]; `tensor/DDL_lfc|DDL_z.npy` [1617]; `embed/gene_vectors.npy` [1617]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1617 or target_col == 1617). Every well: [[MAEA — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MAEA.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
